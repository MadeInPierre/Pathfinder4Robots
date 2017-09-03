#!/usr/bin/python
import rospy, time
from robot_ai.msg import AICommand
from robot_ai.srv import AIGenericCommand, AIGenericCommandResponse


class AIServices():
	def __init__(self, AI):
		self.DepartmentName = "robot_ai"
		rospy.Service(self.DepartmentName, AIGenericCommand, self.on_generic_command)

		self.AI = AI
	
	def on_generic_command(req):
		print "---\nDepartment: {}\nDestination : {}\nCommand : {}\nParams:{}".format(req.department, req.destination, req.command, req.params)

		if req.department != self.DepartmentName:
			rospy.logerr("ERROR service received goes to department '{}', this is '{}'.".format(req.department, self.DepartmentName))
			return None

		if req.command == "timer_start":
			success, reason = self.service_start_timer(req.params)
		if req.command == "ai_delay":
			success, reason = self.service_delay(req.params)
		else:
			success, reason = 200 if bool(input("Send success or not ? ")) else 404, "command_not_recognized"


		rospy.logdebug("[AIServices] Sending response for command '{}'".format(req.command))
		return AIGenericCommandResponse(success, reason)



	def service_start_timer(self, params):
		self.AI.Timer.start()
		return 200, ""

	def service_delay(self, params):
		time.sleep(int(params))
		return 200, ""


if __name__ == '__main__':
	s = AIServices()
