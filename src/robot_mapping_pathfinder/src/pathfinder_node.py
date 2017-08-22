#!/usr/bin/python

import rospy
import Pathfinder
from std_msgs.msg import String
import os


class MapManager_node():
	def __init__(self):
		self.pathfinder = Pathfinder()

		self.publisher = pub = rospy.Publisher("pathfinder", String, queue_size = 10)
		self.node = rospy.init_node('mapping_pathfinder', log_level= rospy.INFO)


if __name__ == "__main__":
	mapmanager_node = MapManager_node()