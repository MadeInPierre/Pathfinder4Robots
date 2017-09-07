#!/usr/bin/python
import rospy, time

from robot_ai.srv import *
from robot_ai.msg import *

class TimerNode():
	def __init__(self):
		self.DepartmentName = "robot_ai_timer"
		self.node = rospy.init_node(self.DepartmentName, log_level=rospy.DEBUG)
		self.service = rospy.Service(self.DepartmentName, AIGenericCommand, self.on_request)

	def on_request(self):
		pass

if __name__ == "__main__":
	timer = TimerNode()