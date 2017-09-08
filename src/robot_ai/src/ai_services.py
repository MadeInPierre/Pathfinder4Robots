#!/usr/bin/python
import rospy, time
from robot_ai.msg import AICommand
from robot_ai.srv import AIGenericCommand, AIGenericCommandResponse


class AIServices():
	def __init__(self, AI):
		self.DepartmentName = "ai"
		self.PackageName = "main"
		rospy.Service(self.PackageName, AIGenericCommand, self.on_generic_command)

		self.AI = AI
	
	def on_generic_command(self, req):
		rospy.loginfo("[AI] NEW GENERIC COMMAND\nDepartment: {}\nDestination : {}\nCommand : {}\nParams:{}".format(
						req.department, req.destination, req.command, req.params))

		if req.department != self.DepartmentName:
			rospy.logerr("[AI] ERROR service received goes to department '{}', this is '{}'!".format(req.department, self.DepartmentName))
			return None

		if req.destination:
			if req.destination == self.PackageName:
				if req.command == "ai_delay":
					res_code, reason = self.service_delay(req.params)
				else:
					rospy.logerr("robot_ai got non-recognized command '{}'.".format(req.command))
					res_code, reason = 404, "command not recognized"
			else:
				res_code, reason = 400, "service does not belong to this handler"
		else:
			raise KeyError, "ERROR No destination !"

		rospy.logdebug("[AIServices] Sending response for command '{}'".format(req.command))
		return AIGenericCommandResponse(res_code, reason)



#/*==========================================
#=            Service executions            =
#==========================================*/
	'''
	def sendServiceToModule(self, srv):
		rospy.logwarn("sending to child ")
		rospy.wait_for_service(srv.destination)
		service = rospy.ServiceProxy(srv.destination, AIGenericCommand)
		response = service(srv.department, srv.destination, srv.command, srv.params)
		return response.response_code, response.reason
	'''
	def service_delay(self, params):
		rospy.loginfo("[AI] Sleeping for {} seconds...".format(int(params)))
		time.sleep(int(params))
		return 200, ""

#/*=====  End of Service executions  ======*/




if __name__ == '__main__':
	s = AIServices()
