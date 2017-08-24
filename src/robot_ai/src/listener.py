#!/usr/bin/python
import rospy
from robot_ai.msg import AICommand

def callback(msg):
    rospy.loginfo("Command '{}' with params: {}".format(msg.command, msg.params))

def listener():
    rospy.init_node('custom_listener', anonymous = True, log_level = rospy.DEBUG)
    rospy.Subscriber("ai_commands", AICommand, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()