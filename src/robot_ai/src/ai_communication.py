import rospy
import robot_ai.srv

class AICommunication():
	def __init__(self):
		pass

	def SendGenericCommand(self, msg_dest, msg_command, msg_params):
		# Send a simple command service, with string command and params. Expecting a bool and string for response
		rospy.wait_for_service("generic_commands")
		service = rospy.ServiceProxy("generic_commands", robot_ai.srv.AIGenericCommand)
		return service(msg_dest, msg_command, msg_params)

	def ServiceRequest(self):
		#Send a service (waiting for a response)
		pass