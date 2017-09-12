#!/usr/bin/python
import rospy
from lidar_services import *

class Lidar():
	def __init__(self):
		self.DepartmentName, self.PackageName = "movement", "lidar"
		
		self.Node     = rospy.init_node(self.PackageName, log_level = rospy.INFO)
		self.Services = LidarServices(self.DepartmentName, self.PackageName)

		rospy.spin()


if __name__ == "__main__":
	Lidar()