#!/usr/bin/python
import rospy, time
from ai_communication import AICommunication
from ai_services import AIServices
from AI import RobotAI, TaskStatus

from robot_ai.msg import AICommand
from robot_mapping_pathfinder.srv import *
from geometry_msgs.msg import Pose2D

class AINode():
	def __init__(self):
		self.NODE = rospy.init_node('ai_node', log_level = rospy.INFO)
		self.communication = AICommunication()

		self.wait_for_departments()

		self.AI = RobotAI("Strategy 1", self.communication)
		self.services = AIServices(self.AI)

		#self.AI.Strategy.PrettyPrint()
		while True:
			if self.AI.Strategy.canContinue():
				self.AI.Strategy.getNext().execute(self.communication)
			else:
				self.AI.Strategy.PrettyPrint()
				rospy.loginfo("[AI] In-Game actions finished!")
				break
			# self.AI.Strategy.PrettyPrint()

	def wait_for_departments(self):
		pass #TODO wait for all services to be ready.

if __name__ == "__main__":
	node = AINode()