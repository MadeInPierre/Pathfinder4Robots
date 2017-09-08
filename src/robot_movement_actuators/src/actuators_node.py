#!/usr/bin/python
import rospy
from actuators_services import *

class Actuators():
	def __init__(self):
		self.DepartmentName, self.PackageName = "movement", "actuators"
		
		self.Node     = rospy.init_node(self.PackageName, log_level = rospy.INFO)
		self.Services = ActuatorsServices(self.DepartmentName, self.PackageName)

		rospy.spin()


if __name__ == "__main__":
	Actuators()