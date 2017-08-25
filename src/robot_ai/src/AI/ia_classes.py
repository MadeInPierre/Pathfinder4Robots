#!/usr/bin/python
# -*- coding: utf-8 -*-
from anytree import Node
import rospy, time
import copy

# utf-8 boxes link : http://jrgraphix.net/r/Unicode/2500-257F

#/*====================================
#=            Base classes            =
#====================================*/

class TaskStatus:
	CRITICAL            = ('CRITICAL'           , '💔')
	WAITINGFORRESPONSE  = ('WAITINGFORRESPONSE' , '💬')
	FREE                = ('FREE'               , '⬜')
	PAUSED              = ('PAUSED'             , '🔶')
	ERROR               = ('ERROR '             , '⛔')
	BLOCKED             = ('BLOCKED'            , '◼')
	SUCCESS             = ('SUCCESS'            , '🆗')

class Task(object):
	def __init__(self, xml, status = TaskStatus.FREE):
		self.Reward = int(xml.attrib["reward"]) if "reward" in xml.attrib else 0
		self.Status = status
		self.Parent = None

	
	def setParent(self, parent):
		self.Parent = parent
	def setStatus(self, new_status):
		if self.Status != new_status:
			self.Status = new_status
			if self.Parent:
				self.Parent.refreshStatus()
	def getStatus(self):
		return self.Status

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
		self.ExecutionMode    = xml.attrib["exec"]    if "exec"    in xml.attrib else 'all' # all, one, +, last
		self.ExecutionOrder   = xml.attrib["order"] if "order" in xml.attrib else 'linear'
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

	def getNext(self):
		for task in self.TASKS:
			if task.getStatus() == TaskStatus.FREE:
				return task
		print "NO FREE TASK"
		return None

	def execute(self, communicator):
		if self.getStatus() == TaskStatus.FREE:
			self.getNext().execute(communicator)
		else:
			raise ValueError, "ERROR asked to execute a task that's not free"

	def refreshStatus(self):
		if self.ExecutionMode == 'all':
			priorityList = [TaskStatus.SUCCESS, TaskStatus.BLOCKED,            TaskStatus.ERROR,    TaskStatus.PAUSED, 
							TaskStatus.FREE,    TaskStatus.WAITINGFORRESPONSE, TaskStatus.CRITICAL]
		elif self.ExecutionMode == 'one' or self.ExecutionMode == '+': #TODO
			priorityList = [TaskStatus.ERROR, TaskStatus.BLOCKED,              TaskStatus.SUCCESS,  TaskStatus.PAUSED, 
							TaskStatus.FREE,  TaskStatus.WAITINGFORRESPONSE, TaskStatus.CRITICAL]
		elif self.ExecutionMode == 'last':
			self.setStatus(self.TASKS[-1].getStatus())
		else:
			raise ValueError, "CRITICAL ActionList has no success condition!"
		
		status = -1
		for task in self.TASKS:
			s = priorityList.index(task.getStatus())
			if s > status: 
				status = s
		self.setStatus(priorityList[status])


	def prettyprint(self, indentlevel, print_self = True):
		if print_self:
			super(ActionList, self).prettyprint(indentlevel)
		for task in self.TASKS:
			task.prettyprint(indentlevel + (1 if print_self else 0))
	def __repr__(self):
		return "\033[1m\033[91m[{0} ActionList] {1} [{2}, {3}{4}]".format(self.getStatusEmoji(), self.Name, self.ExecutionMode, self.ExecutionOrder,
																	 ", {}⚡".format(self.Reward) if self.Reward else "") + "\033[0m"





class Action(Task):
	def __init__(self, xml, actions, orders):
		super(Action, self).__init__(xml)
		self.Ref = xml.attrib["ref"]
		self.loadxml(xml, actions, orders)

	def loadxml(self, xml, actions, orders):
		self.TASKS = ActionList(xml.find("actions"), actions, orders)
		self.TASKS.setParent(self)

	def getNext(self):
		for task in self.TASKS.TASKS:
			if task.getStatus() == TaskStatus.FREE:
				return task

	def refreshStatus(self):
		self.setStatus(self.TASKS.getStatus())

	def execute(self, communicator):
		if self.getStatus() == TaskStatus.FREE:
			self.getNext().execute(communicator)
		else:
			raise ValueError, "ERROR asked to execute a task that's not free"

	def prettyprint(self, indentlevel):
		super(Action, self).prettyprint(indentlevel)
		self.TASKS.prettyprint(indentlevel + 1, print_self = False)
	def __repr__(self):
		return "\033[1m\033[95m[{0} Action]\033[0m\033[95m {1} [{2}, {3}{4}]".format(self.getStatusEmoji(), self.Ref, self.TASKS.ExecutionMode, self.TASKS.ExecutionOrder,
																	     ", {}⚡".format(self.Reward) if self.Reward else "") + "\033[0m"






class Order(Task):
	def __init__(self, xml):
		super(Order, self).__init__(xml)
		self.Ref = xml.attrib["ref"]

		self.ETL    = float(xml.attrib["time"]) # Manually estimated time to execute this action
		self.Reward = int(xml.attrib["reward"]) if "reward" in xml.attrib else 0
		
		#self.ParamsNeededCount = len(xml.find("message").find("params").findall("param"))
		self.Message = Message(xml.find("message"))


	def execute(self, communicator):
		'''if len(kwargs) != len(self.NeededParamsIDs):
			raise ValueError, "ERROR missing or too many parameters for message."'''
		self.setStatus(TaskStatus.WAITINGFORRESPONSE)
		rospy.loginfo("Executing task : {}...".format(self.__repr__()))
		

		response = self.Message.send(communicator)
		rospy.loginfo('got response ! reason : ' + response.reason)
		self.setStatus(TaskStatus.SUCCESS if response.success else TaskStatus.ERROR)

	def __repr__(self):
		return "\033[1m[{0} Order]\033[0m {1}{2}".format(self.getStatusEmoji(), self.Ref, 
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
		response = communicator.SendGenericCommand(self.DestinationNode, self.Command, "params")
		return response