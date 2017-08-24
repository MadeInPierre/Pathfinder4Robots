#!/usr/bin/python
import rospy
from ai_communication import AICommunication
from AI import RobotAI

from robot_ai.msg import AICommand

class AINode():
	def __init__(self):
		self.NODE = rospy.init_node('ai_node', log_level = rospy.DEBUG)
		self.communication = AICommunication()
		self.AI = RobotAI("Strategy 1", self.communication)
		self.AI.Strategy.updateStatus()
		self.AI.Strategy.PrettyPrint()


		r = rospy.Rate(2)
		self.PUB = rospy.Publisher('ai_commands', AICommand, queue_size = 10)
		msg = AICommand()
		msg.command = "hello"
		msg.params = "params here heh"

		while not rospy.is_shutdown():
			self.PUB.publish(msg)
			r.sleep()



node = AINode()