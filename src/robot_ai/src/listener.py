#!/usr/bin/python
import rospy
from robot_ai.msg import AICommand
from robot_ai.srv import AIGenericCommand, AIGenericCommandResponse

def callback(msg):
    rospy.loginfo("Command '{}' with params: {}".format(msg.command, msg.params))

def on_generic_command(req):
	print "Destination : {}\nCommand : {}\nParams:{}".format(req.destination, req.command, req.params)
	success = bool(input("Send success or not ? "))
	reason = ""
	if not success:
		reason = "Timeout"
	res = AIGenericCommandResponse(success, reason)

	print "Sending response."
	return res

def listener():
    rospy.init_node('custom_listener', anonymous = True, log_level = rospy.DEBUG)
    #rospy.Subscriber("ai_commands", AICommand, callback)

    rospy.Service('generic_commands', AIGenericCommand, on_generic_command)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()