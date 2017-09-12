#!/usr/bin/python
import rospy
from wheels_services import *

class Wheels():
	def __init__(self):
		self.DepartmentName, self.PackageName = "movement", "wheels"
		
		self.Node     = rospy.init_node(self.PackageName, log_level = rospy.INFO)
		self.Services = WheelsServices(self.DepartmentName, self.PackageName)

		rospy.spin()


if __name__ == "__main__":
	Wheels()