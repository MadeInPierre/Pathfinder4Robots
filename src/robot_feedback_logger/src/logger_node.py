#!/usr/bin/python
import rospy

class Node():
	def __init__(self):
		self.DepartmentName, self.PackageName = "feedback", "server"
		self.NODE = rospy.init_node(self.PackageName, log_level = rospy.DEBUG)
		while not rospy.is_shutdown():
			rospy.spin()