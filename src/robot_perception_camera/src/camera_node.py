#!/usr/bin/python
from camera_services import *

class Movement():
	def __init__(self):
		self.DepartmentName, self.PackageName = "perception", "camera"
		
		self.Node     = rospy.init_node(self.PackageName, log_level = rospy.INFO)
		self.Services = MovementServices(self.DepartmentName, self.PackageName)

		rospy.spin()


if __name__ == "__main__":
	Movement()