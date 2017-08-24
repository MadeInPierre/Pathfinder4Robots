#!/usr/bin/python
# -*- coding: utf-8 -*-
from anytree import Node


#/*====================================
#=            Base classes            =
#====================================*/

class TaskStatus:
	FREEA, PENDING, WAITINGFORRESPONSE, COMPLETED, PAUSED, ERROR, CRITICAL = range(7)
	FREE     = (0, 'FREE'    , '⬜')
	PENDING  = (0, 'PENDING' , '🔄')
	WAITING  = (2, 'WAITING' , '💬')
	SUCCESS  = (3, 'SUCCESS' , '🆗')
	PAUSED   = (4, 'PAUSED'  , '🔶')
	ERROR    = (5, 'ERROR'   , '⛔')
	CRITICAL = (6, 'CRITICAL', '💔')

class ListHierarchyType:
	LINEAR, FASTEST, MOST_SCORE, RANDOM = range(4)

class Task(object):
	def __init__(self, xml, status = TaskStatus.FREE):
		self.Status = status
	def getStatus(self):
		return self.Status[0]
	def getStatusString(self):
		return self.Status[1]
	def getStatusEmoji(self):
		return self.Status[2]

	def prettyprint(self, indentlevel):
		print "  ║ " * (indentlevel - 1) + "  ╠═" + self.__repr__()
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
		print "---"
		self.TASKS_ONFINISH = ActionList(xml.find("actions_onfinish"), actions, orders)

	def getStatus(self):
		return self.TASKS.getStatus()

	def PrettyPrint(self):
		print 'STRATEGY'
		self.TASKS.prettyprint(1)
		self.TASKS_ONFINISH.prettyprint(1)
	def __repr__(self):
		return self.Name

class ActionList(Task):
	def __init__(self, xml, actions, orders, name = None):
		super(ActionList, self).__init__(xml)
		self.Name = name if name else xml.attrib["name"]
		self.ExecutionMode    = xml.attrib["exec"]    if "exec"    in xml.attrib else 'none'
		self.SuccessCondition = xml.attrib["success"] if "success" in xml.attrib else 'none'

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
				self.TASKS.append(instances[0])
			elif task_xml.tag == "orderref":
				instances = [order for order in orders if order.Ref == task_xml.attrib["ref"]]
				if len(instances) != 1:
					raise KeyError, "{} order instance(s) found with the name '{}'.".format(len(instances), task_xml.attrib["ref"])
				self.TASKS.append(instances[0])
			elif task_xml.tag == "action":
				self.TASKS.append(None)
			elif task_xml.tag == "order":
				self.TASKS.append(None)#Order(task_xml.attrib["ref"], task_xml.find("params")))
			else:
				print "WARNING Task skipped because '{}' type was not recognized.".format(task_xml.tag)

	def getBest(self):
		return None

	def getStatus(self):
		return self.TASKS[0].getStatus() #TODO

	def prettyprint(self, indentlevel):
		super(ActionList, self).prettyprint(indentlevel)
		for task in self.TASKS:
			task.prettyprint(indentlevel + 1)
	def __repr__(self):
		return "[{0} ActionList] {1}".format(self.getStatusEmoji(), self.Name)




class Action(Task):
	def __init__(self, xml, actions, orders):
		super(Action, self).__init__(xml)
		self.Ref = xml.attrib["ref"]
		self.loadxml(xml, actions, orders)

	def loadxml(self, xml, actions, orders):
		self.TASKS = ActionList(xml.find("actions"), actions, orders, name = "Action Tasks")

	def prettyprint(self, indentlevel):
		print "  ║ " * (indentlevel - 1) + "  ╠═" + self.__repr__()
		self.TASKS.prettyprint(indentlevel + 1)
	def __repr__(self):
		return "[{0} Action] {1}".format(self.getStatusEmoji(), self.Ref)




class Order(Task):
	def __init__(self, xml):
		super(Order, self).__init__(xml)
		self.Ref = xml.attrib["ref"]
		
		#self.ParamsNeededCount = len(xml.find("message").find("params").findall("param"))
		self.Message = Message(xml.find("message"))

	def execute(self, params_dict):
		'''if len(kwargs) != len(self.NeededParamsIDs):
			raise ValueError, "ERROR missing or too many parameters for message."'''
		self.Status = TaskStatus.INPROGRESS

	def __repr__(self):
		return "[{0} Order] {1}".format(self.getStatusEmoji(), self.Ref)



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
