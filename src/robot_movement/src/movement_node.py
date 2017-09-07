#!/usr/bin/python
import rospy
from robot_ai.srv import AIGenericCommand, AIGenericCommandResponse

def callback(msg):
    rospy.loginfo("Command '{}' with params: {}".format(msg.command, msg.params))

def on_generic_command(req):
	print "\n---\nDepartment: {}\nDestination : {}\nCommand : {}\nParams:{}".format(req.department, req.destination, req.command, req.params)

	success = 200 if bool(input("Send success or not ? ")) else 404
	reason = "<reason>"
	
	print "Sending response."
	return AIGenericCommandResponse(success, reason)

def listener():
    rospy.init_node('robot_movement_node', anonymous = True, log_level = rospy.DEBUG)
    #rospy.Subscriber("ai_commands", AICommand, callback)

    rospy.Service('robot_movement', AIGenericCommand, on_generic_command)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    l = listener()