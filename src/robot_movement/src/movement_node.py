#!/usr/bin/python
import rospy
from robot_ai.srv import AIGenericCommand, AIGenericCommandResponse

class Movement():
	def __init__(self):
		self.DepartmentName = "movement"
		self.PackageName = "main"
		rospy.init_node(self.PackageName, log_level = rospy.DEBUG)
		rospy.Service(self.PackageName, AIGenericCommand, self.on_generic_command)
		rospy.spin()
		
	def on_generic_command(self, req):
		rospy.logdebug("[Movement] NEW SERVICE REQUEST : \nDepartment: {}\nDestination : {}\nCommand : {}\nParams:{}".format(
			req.department, req.destination, req.command, req.params))

		res_code = 200 if bool(input("Send success or not ? ")) else 404
		reason = "<reason>"
		
		print "Sending response."
		return AIGenericCommandResponse(res_code, reason)


if __name__ == '__main__':
	l = Movement()