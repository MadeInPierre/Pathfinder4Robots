# -*- coding: utf-8 -*-
import rospy
import robot_ai.srv

class AICommunication():
	def __init__(self):
		pass

	def SendGenericCommand(self, msg_department, msg_dest, msg_command, msg_params):
		# Send a simple command service, with string command and params. Expecting a bool and string for response
		dest = "/{}/{}".format(msg_department, msg_dest)
		rospy.loginfo("sending service to service '{}'".format(dest))

		rospy.wait_for_service(dest)
		service = rospy.ServiceProxy(dest, robot_ai.srv.AIGenericCommand)
		return service(msg_department, msg_dest, msg_command, msg_params)

	def ServiceRequest(self):
		# Send a service (waiting for a response)
		pass



# THREADING THIS : https://stackoverflow.com/questions/6800984/python-how-to-pass-and-run-a-callback-method-in-python