#!/usr/bin/python
import rospy
from robot_ai.srv import AIGenericCommand, AIGenericCommandResponse

def listener():
	rospy.init_node('robot_movement_node', log_level = rospy.DEBUG)
	rospy.Service('robot_movement', AIGenericCommand, on_generic_command)
	print "hi"
	rospy.spin()

def on_generic_command(req):
	print "seeervice"
	rospy.logwarn("NEW SERVICE REQUEST : \nDepartment: {}\nDestination : {}\nCommand : {}\nParams:{}".format(
		req.department, req.destination, req.command, req.params))

	res_code = 200 if bool(input("Send success or not ? ")) else 404
	reason = "<reason>"
	
	print "Sending response."
	return AIGenericCommandResponse(res_code, reason)


if __name__ == '__main__':
	l = listener()