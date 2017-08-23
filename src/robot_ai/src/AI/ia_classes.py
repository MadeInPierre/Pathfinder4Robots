#!/usr/bin/python
from anytree import Node


#/*====================================
#=            Base classes            =
#====================================*/

class ItemStatus:
    TODO, STARTED, PENDING, COMPLETED, PAUSED, ERROR, CRITICAL = range(7)

class ListHierarchyType:
	LINEAR, FASTEST, MOST_SCORE, RANDOM = range(4)

class AI_TASK(object):
	def __init__(self, name, status = ItemStatus.TODO):
		self.Status = status
		self.Name = ""

	def __name__(self):
		return self.Name


#/*=====  End of Base classes  ======*/







class Strategy(AI_TASK):
	def __init__(self, name, initdict):
		super(Strategy, self).__init__(name)
		self.loadStrategy(initdict)

	def loadStrategy(self, initdict):
		pass

class ActionsList():
	def __init__(self, initdict):
		pass


class Objective(AI_TASK):
	def __init__(self, name, initdict):
		super(Objective, self).__init__(name)




class Action(AI_TASK):
	def __init__(self, name, initdict):
		super(Action, self).__init__(name)







#/*========================================
#=            Embedded Actions            =
#========================================*/
class wheels(Action):
	pass

class action_actuator(Action):
	pass

class action_wheels(Action):
	pass

class action_robotarm(Action):
	pass


#/*=====  End of Embedded Actions  ======*/
