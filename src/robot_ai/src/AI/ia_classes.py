#!/usr/bin/python
from anytree import Node


#/*====================================
#=            Base classes            =
#====================================*/

class TaskStatus:
    FREE, PENDING, WAITINGFORRESPONSE, COMPLETED, PAUSED, ERROR, CRITICAL = range(7)

class ListHierarchyType:
	LINEAR, FASTEST, MOST_SCORE, RANDOM = range(4)

class Task(object):
	def __init__(self, xml, status = TaskStatus.FREE):
		self.Status = status
	def getStatus(self):
		return self.Status
	def __repr__(self):
		return "<No Name>"

class GameProperties():
	GAME_DURATION = None

#/*=====  End of Base classes  ======*/


class Strategy(Task):
	def __init__(self, xml):
		super(Strategy, self).__init__(xml)
		self.loadxml(xml)

	def loadxml(self, xml):
		# Game Properties
		GameProperties.GAME_DURATION = int(xml.find('game').find("time").text) # Save game duration in seconds

		# Fill actions
		self.TASKS = ActionsList(xml.find("actions"))
		print "---"
		self.TASKS_ONFINISH = ActionsList(xml.find("actions_onfinish"))

class ActionList(Task):
	def __init__(self, xml, actions, orders):
		super(ActionList, self).__init__(xml)
		self.Name = xml.attrib["name"]
		self.TASKS = None
		self.loadxml(xml)

	def loadxml(self, xml, actions, orders):
		self.TASKS = []
		for task_xml in xml:
			if task_xml.tag == "actionlist":
				self.TASKS.append(ActionList(task_xml))
			elif task_xml.tag == "action":
				self.TASKS.append(None)
			elif task_xml.tag == "order":
				self.TASKS.append(None)#Order(task_xml.attrib["ref"], task_xml.find("params")))
			else:
				print "WARNING Task skipped because '{}' type was not recognized.".format(task_xml.tag)

	def getBest(self):
		return None

	def __repr__(self):
		return self.Name




class Action(Task):
	def __init__(self, xml, actions, orders):
		super(Action, self).__init__(xml)
		self.Ref = xml.attrib["ref"]
		self.loadxml(xml, actions, orders)

	def loadxml(self, xml, actions, orders):
		self.TASKS = ActionList(xml.find("actions"), actions, orders)

	def __repr__(self):
		return self.Rep




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
		return self.Ref



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
