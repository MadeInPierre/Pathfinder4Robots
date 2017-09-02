#!/usr/bin/python

import rospy
from MapManager import MapManager, MapVisualizer
from std_msgs.msg import String
import os


class MapManager_node():
	def __init__(self):
		self.mapman = MapManager(os.path.dirname(__file__) + "/" + "Definitions/map.json")

		self.publisher = pub = rospy.Publisher("mapmanager", String, queue_size = 10)
		self.node = rospy.init_node('mapping_mapmanager', log_level= rospy.INFO)

		self.mapman.updateVizImg()
		viz = MapVisualizer()
		viz.Draw(self.mapman.getVizImg(), self.mapman.getCollisionImg())


if __name__ == "__main__":
	mapmanager_node = MapManager_node()