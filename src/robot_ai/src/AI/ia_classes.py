#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
import rospy, time
import copy

'''
GENERAL TODO
	- Pending state to lists CAUTION should still execute like if it was free.
	- Parameters
	- ExecutionOrder
	- Conditions (chest, needsprevious..)

WARNINGS
	- Paused tasks re-activation not implemented 
'''

# utf-8 boxes link : http://jrgraphix.net/r/Unicode/2500-257F

#/*====================================
#=            Base classes            =
#====================================*/

class TaskStatus:
	CRITICAL            = ('CRITICAL'			, '💔')	# Fatal error, system will shutdown.
	WAITINGFORRESPONSE  = ('WAITINGFORRESPONSE'	, '💬')	# Order sent service or action message, waiting for response callback.
	PENDING             = ('PENDING'            , '⋯')	# For lists only. Active when one or not all child tasks are still active.
	FREE                = ('FREE'				, '⬜')	# Free task, not activated yet.
	PAUSED              = ('PAUSED'				, '🔶')	# TODO
	ERROR               = ('ERROR'				, '⛔', "error_msg")	# Error. Order couldn't be done, AI will try to find an alternative path of orders in the tree.
	BLOCKED             = ('BLOCKED'			, '◼')	# Node can't execute because conditions aren't fully satisfied.
	SUCCESS             = ('SUCCESS'			, '🆗', 0.0)	# Order and lists complete.
	def toEmoji(status):
		return status[1]

class ExecutionMode():
	ALL                 = ('all'				, '⚫')	# All tasks in the list must be executed.
	ONE                 = ('one'				, '1')	# Only one task in the list must be executed.
	ATLEASTONE          = ('+'					, '+')	# At least one task in the list must be executed, will try to execute all.
	@staticmethod
	def toEmoji(mode):
		return mode[1]
	@staticmethod
	def fromText(text):
		if text == 'all'           : return ExecutionMode.ALL
		elif text == 'one'         : return ExecutionMode.ONE
		elif text == '+'           : return ExecutionMode.ATLEASTONE
		else: raise ValueError, "ExecutionMode '{}' not recognized.".format(text)

class ExecutionOrder():
	LINEAR              = ('linear'				, '⬇')	# Will follow linearly the order given in the XML file.
	RANDOM              = ('random'				, '🌀')	# Will pick a random free task.
	SIMULTANEOUS        = ('simultaneous'		, '⇶')	# Will activate all tasks at once.
	FASTEST             = ('fastest'			, '🕒')	# Will sort the tasks from least Duration to most.
	MOSTREWARD          = ('mostreward'			, '⚡')	# Will sort the tasks from most Reward to least.
	@staticmethod
	def toEmoji(order):
		return order[1]
	@staticmethod
	def fromText(text):
		print text
		if text == 'linear'        : return ExecutionOrder.LINEAR
		elif text == 'random'      : return ExecutionOrder.RANDOM
		elif text == 'simultaneous': return ExecutionOrder.SIMULTANEOUS
		elif text == 'fastest'     : return ExecutionOrder.FASTEST
		elif text == 'mostreward'  : return ExecutionOrder.MOSTREWARD
		else: raise ValueError, "ExecutionOrder '{}' not recognized.".format(text)


class Task(object):
	def __init__(self, xml, status = TaskStatus.FREE):
		self.Reward = int(xml.attrib["reward"]) if "reward" in xml.attrib else 0
		self.Status = status
		self.Parent = None

	def getReward(self):
		return self.Reward
	
	def setParent(self, parent):
		self.Parent = parent
	def setStatus(self, new_status):
		if self.Status != new_status:
			self.Status = new_status
			#print "set status to " + str(self.getStatus(text = True)) + " " + str(self.Parent)
			if self.Parent:
				self.Parent.refreshStatus()
	def getStatus(self, text = False):
		return self.Status if not text else self.Status[0]

	def getStatusEmoji(self):
		return self.Status[1]
	def prettyprint(self, indentlevel):
		rospy.logdebug("\033[0m" + "  ║ " * (indentlevel - 1) + "  ╠═" + self.__repr__())
	def __repr__(self):
		return "<Task with No Name>"

class GameProperties():
	GAME_DURATION = None

#/*=====  End of Base classes  ======*/







class Strategy(Task):
	def __init__(self, xml, actions, orders):
		super(Strategy, self).__init__(xml)
		self.Name = xml.attrib["name"]
		self.loadxml(xml, actions, orders)

	def loadxml(self, xml, actions, orders):
		# Game Properties
		GameProperties.GAME_DURATION = int(xml.find('game').find("time").text) # Save game duration in seconds

		# Fill actions
		self.TASKS = ActionList(xml.find("actions"), actions, orders)
		self.TASKS_ONFINISH = ActionList(xml.find("actions_onfinish"), actions, orders)

	def canContinue(self):
		return self.getStatus() in [TaskStatus.FREE, TaskStatus.PENDING, TaskStatus.WAITINGFORRESPONSE]
	def getNext(self): # Returns the next free task (ActionList, Action or Order).
		return self.TASKS.getNext()

	def getStatus(self):
		return self.TASKS.getStatus()

	def PrettyPrint(self): # Updates and then prints
		#self.updateStatus()
		rospy.logdebug('[STRATEGY] ' + self.__repr__())
		self.TASKS.prettyprint(1)
		self.TASKS_ONFINISH.prettyprint(1)
	def __repr__(self):
		return self.Name






class ActionList(Task):
	def __init__(self, xml, actions, orders):
		super(ActionList, self).__init__(xml)
		self.Name = xml.attrib["name"] if "name" in xml.attrib else xml.tag
		self.executionMode    = ExecutionMode.fromText( xml.attrib["exec"])  if "exec"  in xml.attrib else ExecutionMode.ALL
		self.executionOrder   = ExecutionOrder.fromText(xml.attrib["order"]) if "order" in xml.attrib else ExecutionOrder.LINEAR
		self.Conditions = xml.find("conditions") if "conditions" in xml else None # Conditions that must be true before executing the actions.

		self.TASKS = None
		self.loadxml(xml, actions, orders)

	def loadxml(self, xml, actions, orders):
		self.TASKS = []
		for task_xml in xml:
			if task_xml.tag == "actionlist":
				i = ActionList(task_xml, actions, orders)
				i.setParent(self)
				self.TASKS.append(i)
			elif task_xml.tag == "actionref":
				instances = [action for action in actions if action.Ref == task_xml.attrib["ref"]]
				if len(instances) != 1:
					raise KeyError, "{} action instance(s) found with the name '{}'.".format(len(instances), task_xml.attrib["ref"])
				i = copy.deepcopy(instances[0])
				i.setParent(self)
				self.TASKS.append(i)
			elif task_xml.tag == "orderref":
				instances = [order for order in orders if order.Ref == task_xml.attrib["ref"]]
				if len(instances) != 1:
					raise KeyError, "{} order instance(s) found with the name '{}'.".format(len(instances), task_xml.attrib["ref"])
				i = copy.deepcopy(instances[0])
				i.setParent(self)
				self.TASKS.append(i)
			else:
				rospy.logwarn("WARNING Task skipped because '{}' type was not recognized.".format(task_xml.tag))

	def getReward(self):
		return self.Reward + sum([task.getReward() for task in self.TASKS])
	def getDuration(self):
		return sum([task.getDuration() for task in self.TASKS])
	def getNext(self):
		if   self.executionOrder == ExecutionOrder.LINEAR:
			for task in self.TASKS:
				if task.getStatus() in [TaskStatus.FREE, TaskStatus.PENDING]: return task
		elif self.executionOrder == ExecutionOrder.RANDOM:
			for task in self.TASKS:
				if task.getStatus() == TaskStatus.PENDING:
					return task
			free_tasks = [task for task in self.TASKS if task.getStatus() == TaskStatus.FREE]
			return free_tasks[randint(0, len(free_tasks) - 1)]
		elif self.executionOrder == ExecutionOrder.SIMULTANEOUS:
			return [task for task in self.TASKS if task.getStatus() in [TaskStatus.FREE, TaskStatus.PENDING]]
		elif self.executionOrder == ExecutionOrder.FASTEST:
			record, result = 10000000, None
			for task in self.TASKS:
				if task.getDuration() < record:
					record = task.getDuration()
					result = task
			return result
		elif self.executionOrder == ExecutionOrder.MOSTREWARD:
			record, result = -1, None
			for task in self.TASKS:
				if task.getReward() > record:
					record = task.getReward()
					result = task
			return result

	def execute(self, communicator):
		if self.getStatus() in [TaskStatus.FREE, TaskStatus.PENDING]:
			self.getNext().execute(communicator)
		else:
			raise ValueError, "ERROR asked to execute a task that's not free"

	def refreshStatus(self):
		child_statuses = [task.getStatus() for task in self.TASKS]
		# The order of conditions do count!
		if TaskStatus.CRITICAL in child_statuses:
			self.setStatus(TaskStatus.CRITICAL);return
		if TaskStatus.WAITINGFORRESPONSE in child_statuses:
			self.setStatus(TaskStatus.WAITINGFORRESPONSE);return

		if self.executionMode == ExecutionMode.ONE:
			if len([1 for c in child_statuses if c == TaskStatus.SUCCESS]) == 1:
				self.setStatus(TaskStatus.SUCCESS)
				#TODO block all dependent tasks too
				for task in self.TASKS:
					if task.getStatus() in [TaskStatus.FREE, TaskStatus.PENDING]:
						task.setStatus(TaskStatus.BLOCKED)
				return

		if TaskStatus.PAUSED in child_statuses:
			self.setStatus(TaskStatus.PAUSED);return
		if TaskStatus.PENDING in child_statuses:
			self.setStatus(TaskStatus.PENDING);return
		if TaskStatus.FREE in child_statuses:
			self.setStatus(TaskStatus.PENDING);return

		if self.executionMode == ExecutionMode.ALL:
			if len([1 for c in child_statuses if c == TaskStatus.SUCCESS]) == len(child_statuses):
				self.setStatus(TaskStatus.SUCCESS);return
		elif self.executionMode == ExecutionMode.ATLEASTONE:
			if len([1 for c in child_statuses if c == TaskStatus.SUCCESS]) >= 1:
				self.setStatus(TaskStatus.SUCCESS);return

		if TaskStatus.ERROR in child_statuses:
			self.setStatus(TaskStatus.ERROR);return
		
	def prettyprint(self, indentlevel, print_self = True):
		if print_self:
			super(ActionList, self).prettyprint(indentlevel)
		for task in self.TASKS:
			task.prettyprint(indentlevel + (1 if print_self else 0))
	def __repr__(self):
		return "\033[1m\033[91m[{0} ActionList] {1} [{2} {3}{4}{5}]".format(self.getStatusEmoji(), 
																self.Name, ExecutionMode.toEmoji(self.executionMode),
																ExecutionOrder.toEmoji(self.executionOrder),
																", {}⚡".format(self.getReward()) if self.getReward() else "",
																", ~{}⌛".format(int(self.getDuration())) if self.getDuration() else "") \
																+ "\033[0m"





class Action(Task):
	def __init__(self, xml, actions, orders):
		super(Action, self).__init__(xml)
		self.Ref = xml.attrib["ref"]
		self.loadxml(xml, actions, orders)

	def loadxml(self, xml, actions, orders):
		self.TASKS = ActionList(xml.find("actions"), actions, orders)
		self.TASKS.setParent(self)

	def getDuration(self):
		return self.TASKS.getDuration()
	def getReward(self):
		return self.TASKS.getReward()
	def getNext(self):
		return self.TASKS.getNext()

	def refreshStatus(self):
		self.setStatus(self.TASKS.getStatus())

	def execute(self, communicator):
		if self.getStatus() in [TaskStatus.FREE, TaskStatus.PENDING]:
			self.getNext().execute(communicator)
		else:
			raise ValueError, "ERROR asked to execute a task that's not free"

	def prettyprint(self, indentlevel):
		super(Action, self).prettyprint(indentlevel)
		self.TASKS.prettyprint(indentlevel + 1, print_self = False)
	def __repr__(self):
		return "\033[1m\033[95m[{0} Action]\033[0m\033[95m {1} [{2} {3}{4}{5}]".format(self.getStatusEmoji(), 
																self.Ref, ExecutionMode.toEmoji(self.TASKS.executionMode),
																ExecutionOrder.toEmoji(self.TASKS.executionOrder),
															    ", {}⚡".format(self.TASKS.getReward()) if self.TASKS.getReward() else "",
																", ~{}⌛".format(int(self.TASKS.getDuration())) if self.TASKS.getDuration() else "") \
																+ "\033[0m"






class Order(Task):
	def __init__(self, xml):
		super(Order, self).__init__(xml)
		self.Ref = xml.attrib["ref"]

		self.Duration = float(xml.attrib["duration"]) if "duration" in xml.attrib else 0.0 # Manually estimated time to execute this action
		self.Reward   = int(xml.attrib["reward"]) if "reward" in xml.attrib else 0
		
		#self.ParamsNeededCount = len(xml.find("message").find("params").findall("param"))
		self.Message = Message(xml.find("message"))

		self.TimeTaken = None

	def getDuration(self):
		return self.Duration

	def execute(self, communicator):
		'''if len(kwargs) != len(self.NeededParamsIDs):
			raise ValueError, "ERROR missing or too many parameters for message."'''
		self.setStatus(TaskStatus.WAITINGFORRESPONSE)
		rospy.loginfo("Executing task : {}...".format(self.__repr__()))
		

		response, self.TimeTaken = self.Message.send(communicator)
		rospy.loginfo('got response ! reason : ' + response.reason)
		self.setStatus(TaskStatus.SUCCESS if response.success else TaskStatus.ERROR)

	def __repr__(self):
		return "\033[1m" + "[{0}{1} Order]\033[0m {2}{3}".format(self.getStatusEmoji(), 
														" , {0:.1f}⌛".format(self.TimeTaken) if self.getStatus() in [TaskStatus.SUCCESS, 
														TaskStatus.ERROR, TaskStatus.PAUSED, TaskStatus.CRITICAL] else "",
														self.Ref, 
														" [{}⚡]".format(self.Reward) if self.Reward else "")





class Message():
	def __init__(self, xml):
		self.DestinationNode = xml.attrib["dest"]
		self.Command = xml.find("command").text
		
		# Save which parameters are needed for the message
		self.NeededParamsIDs = []
		for param in xml.find("params").findall("param"):
			self.NeededParamsIDs.append(param.attrib["id"])


		self.Parameters = {}
		for param in xml.find("params"):
			pass

	def send(self, communicator):
		params = None #TODO
		self.startTime = time.time()
		response = communicator.SendGenericCommand(self.DestinationNode, self.Command, "params")
		self.TimeTaken = time.time() - self.startTime
		return response, self.TimeTaken