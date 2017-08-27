#!/usr/bin/python
import rospy, time
from ai_communication import AICommunication
from AI import RobotAI, TaskStatus

from robot_ai.msg import AICommand
from robot_mapping_pathfinder.srv import *
from geometry_msgs.msg import Pose2D

class AINode():
	def __init__(self):
		self.NODE = rospy.init_node('ai_node', log_level = rospy.DEBUG)
		self.communication = AICommunication()

		self.AI = RobotAI("Strategy 1", self.communication)

		#self.AI.Strategy.TASKS.TASKS[0].TASKS.TASKS[0].setStatus(TaskStatus.SUCCESS)
		#self.AI.Strategy.TASKS.TASKS[0].TASKS.TASKS[1].setStatus(TaskStatus.ERROR)
		#self.AI.Strategy.getNext().setStatus(TaskStatus.WAITINGFORRESPONSE)
		self.AI.Strategy.PrettyPrint()
		while True:
			if self.AI.Strategy.canContinue():
				self.AI.Strategy.getNext().execute(self.communication)
			else:
				rospy.loginfo("[AI] In-Game actions finished!")
				break
			self.AI.Strategy.PrettyPrint()


		'''
		#test
		r = rospy.Rate(2)
		self.PUB = rospy.Publisher('ai_commands', AICommand, queue_size = 10)
		self.SER = rospy.Service('ai_service', AICommand, queue_size = 10)
		msg = AICommand()
		msg.command = "hello"
		msg.params = "params here"

		while not rospy.is_shutdown():
			self.PUB.publish(msg)
			r.sleep()
		

		#self.path()

	def path(self):
		rospy.wait_for_service('MappingPathfinderGetPathService')
		path_service = rospy.ServiceProxy('MappingPathfinderGetPathService', MappingPathfinderGetPathService)

		start = Pose2D(1, 2, 3)
		end = Pose2D(10, 11, 12)
		response = path_service(start, end)
		print response
		'''


node = AINode()

'''
SERVICE NODE

#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')

from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):
	print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
	return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
	rospy.init_node('add_two_ints_server')
	s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
	print "Ready to add two ints."
	rospy.spin()

if __name__ == "__main__":
	add_two_ints_server()
'''