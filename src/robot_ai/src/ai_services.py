#!/usr/bin/python
import rospy, time
from robot_ai.msg import AICommand
from robot_ai.srv import AIGenericCommand, AIGenericCommandResponse


class AIServices():
	def __init__(self, AI):
		self.DepartmentName = "robot_ai"
		rospy.Service(self.DepartmentName, AIGenericCommand, self.on_generic_command)

		self.AI = AI
	
	def on_generic_command(self, req):
		rospy.logdebug("[AI] NEW GENERIC COMMAND\nDepartment: {}\nDestination : {}\nCommand : {}\nParams:{}".format(
						req.department, req.destination, req.command, req.params))

		if req.department != self.DepartmentName:
			rospy.logerr("[AI] ERROR service received goes to department '{}', this is '{}'!".format(req.department, self.DepartmentName))
			return None

		if req.destination:
			if req.destination == "robot_ai":
				if req.command == "ai_delay":
					rospy.loginfo("[AI] Sleeping for {} seconds...".format(int(req.params)))
					time.sleep(int(req.params))
					res_code, reason = 200, ""
				else:
					rospy.logerr("robot_ai got non-recognized command '{}'.".format(req.command))
					res_code, reason = 404, "command not recognized"
			else:
				res_code, reason = self.sendServiceToModule(req)
		else:
			raise KeyError, "ERROR Destination not valid !"

		rospy.logdebug("[AIServices] Sending response for command '{}'".format(req.command))
		return AIGenericCommandResponse(res_code, reason)


	def sendServiceToModule(self, srv):
		rospy.wait_for_service(srv.destination)
		service = rospy.ServiceProxy(srv.destination, AIGenericCommand)
		response = service(srv.department, srv.destination, srv.command, srv.params)

		return response.response_code, response.reason


	def service_start_timer(self, params):
		self.AI.Timer.start()
		return 200, ""

	def service_delay(self, params):
		time.sleep(int(params))
		return 200, ""


if __name__ == '__main__':
	s = AIServices()
