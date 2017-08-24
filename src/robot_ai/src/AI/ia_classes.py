#!/usr/bin/python
# -*- coding: utf-8 -*-
from anytree import Node
import rospy
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
	FAIL                = ('FAIL '              , '⛔')
	SUCCESS             = ('SUCCESS'            , '🆗')

class Task(object):
	def __init__(self, xml, status = TaskStatus.FREE):
		self.Status = status

	def updateStatus(self):
		return self.getStatus()

	def getStatus(self):
		return self.Status
	'''
	def getStatusCode(self):
		return self.Status[0]
	def getStatusString(self):
		return self.Status[1]
	'''
	def getStatusEmoji(self):
		return self.Status[1]
	def prettyprint(self, indentlevel):
		rospy.loginfo("  ║ " * (indentlevel - 1) + "  ╠═" + self.__repr__())
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

	def updateStatus(self):
		self.TASKS.updateStatus()
	def getStatus(self):
		return self.TASKS.getStatus()

	def PrettyPrint(self):
		rospy.loginfo('[STRATEGY] ' + self.__repr__())
		self.TASKS.prettyprint(1)
		self.TASKS_ONFINISH.prettyprint(1)
	def __repr__(self):
		return self.Name

class ActionList(Task):
	def __init__(self, xml, actions, orders):
		super(ActionList, self).__init__(xml)
		self.Name = xml.attrib["name"] if "name" in xml.attrib else xml.tag
		self.ExecutionMode    = xml.attrib["exec"]    if "exec"    in xml.attrib else 'linear'
		self.SuccessCondition = xml.attrib["success"] if "success" in xml.attrib else 'all'
		self.Conditions = xml.find("conditions") if "conditions" in xml else None # Conditions that must be true before executing the actions.

		self.TASKS = None
		self.loadxml(xml, actions, orders)

	def loadxml(self, xml, actions, orders):
		self.TASKS = []
		for task_xml in xml:
			if task_xml.tag == "actionlist":
				self.TASKS.append(ActionList(task_xml, actions, orders))
			elif task_xml.tag == "actionref":
				instances = [action for action in actions if action.Ref == task_xml.attrib["ref"]]
				if len(instances) != 1:
					raise KeyError, "{} action instance(s) found with the name '{}'.".format(len(instances), task_xml.attrib["ref"])
				self.TASKS.append(copy.deepcopy(instances[0]))
			elif task_xml.tag == "orderref":
				instances = [order for order in orders if order.Ref == task_xml.attrib["ref"]]
				if len(instances) != 1:
					raise KeyError, "{} order instance(s) found with the name '{}'.".format(len(instances), task_xml.attrib["ref"])
				self.TASKS.append(copy.deepcopy(instances[0]))
			elif task_xml.tag == "action":
				self.TASKS.append(None)
			elif task_xml.tag == "order":
				self.TASKS.append(None)#Order(task_xml.attrib["ref"], task_xml.find("params")))
			else:
				rospy.logwarn("WARNING Task skipped because '{}' type was not recognized.".format(task_xml.tag))

	def getBest(self):
		return None

	def updateStatus(self):
		if self.SuccessCondition == 'all':
			priorityList = [TaskStatus.SUCCESS, TaskStatus.FAIL, TaskStatus.PAUSED, 
							TaskStatus.FREE, TaskStatus.WAITINGFORRESPONSE, TaskStatus.CRITICAL]
		elif self.SuccessCondition == 'one':
			priorityList = [TaskStatus.FAIL, TaskStatus.SUCCESS, TaskStatus.PAUSED, 
							TaskStatus.FREE, TaskStatus.WAITINGFORRESPONSE, TaskStatus.CRITICAL]
		elif self.SuccessCondition == 'last':
			self.Status = self.TASKS[-1].updateStatus()
			return super(ActionList, self).updateStatus()
		else:
			raise ValueError, "CRITICAL ActionList has no success condition!"
		#print "---" + self.__repr__()
		#print self.TASKS
		# Update status based on the tasks
		status = -1
		for i in xrange(len(self.TASKS)):
			s = priorityList.index(self.TASKS[i].updateStatus())
			if s > status: 
				status = s
		self.Status = priorityList[status]
		return super(ActionList, self).getStatus()

	def prettyprint(self, indentlevel, print_self = True):
		if print_self:
			super(ActionList, self).prettyprint(indentlevel)
		for task in self.TASKS:
			task.prettyprint(indentlevel + (1 if print_self else 0))
	def __repr__(self):
		return "\033[1m\033[91m[{0} ActionList] {1} [{2}]".format(self.getStatusEmoji(), self.Name, self.SuccessCondition) + "\033[0m"




class Action(Task):
	def __init__(self, xml, actions, orders):
		super(Action, self).__init__(xml)
		self.Ref = xml.attrib["ref"]
		self.loadxml(xml, actions, orders)

	def loadxml(self, xml, actions, orders):
		self.TASKS = ActionList(xml.find("actions"), actions, orders)

	def updateStatus(self):
		self.Status = self.TASKS.updateStatus()
		return super(Action, self).getStatus()
	def prettyprint(self, indentlevel):
		super(Action, self).prettyprint(indentlevel)
		self.TASKS.prettyprint(indentlevel + 1, print_self = False)
	def __repr__(self):
		return "\033[1m\033[95m[{0} Action]\033[0m\033[95m {1}".format(self.getStatusEmoji(), self.Ref) + "\033[0m"




class Order(Task):
	def __init__(self, xml):
		super(Order, self).__init__(xml)
		self.Ref = xml.attrib["ref"]

		self.ETL = xml.find("ai").find("ETL").text # Manually estimated time to execute this action
		self.Reward = xml.find("ai").find("reward") if "reward" in xml.find("ai") else 0
		
		#self.ParamsNeededCount = len(xml.find("message").find("params").findall("param"))
		self.Message = Message(xml.find("message"))

	def execute(self, params_dict):
		'''if len(kwargs) != len(self.NeededParamsIDs):
			raise ValueError, "ERROR missing or too many parameters for message."'''
		self.Status = TaskStatus.INPROGRESS

	def __repr__(self):
		return "\033[1m[{0} Order]\033[0m {1}".format(self.getStatusEmoji(), self.Ref)



class Message():
	def __init__(self, xml):
		self.DestinationNode = xml.attrib["dest"]
		self.Command = xml.find("command")
		
		# Save which parameters are needed for the message
		self.NeededParamsIDs = []
		for param in xml.find("params").findall("param"):
			self.NeededParamsIDs.append(param.attrib["id"])


		self.Parameters = {}
		for param in xml.find("params"):
			pass#print param.tag #TODO

	def send(self, params_dict):
		body = {
			"dest": self.DestinationNode,
			"command": self.Command,
			"params": {}
		}
		for param_id in self.NeededParamsIDs:
			body["params"].append(params_dict[param_id]) #TODO
		return False #bool if sent successfully or not

'''
{
	"command": "ldkjfgh",
	"params": {
		"position": {
			"x": 2000,
			"y": 2400,
			"a": false
		}
	}
}
'''







#/*========================================
#=                 Orders                 =
#========================================*/
class wheels(Order):
	pass

class order_actuator(Order):
	pass

class order_wheels(Order):
	pass

class order_robotarm(Order):
	pass


#/*==========  End of Orders  ===========*/
