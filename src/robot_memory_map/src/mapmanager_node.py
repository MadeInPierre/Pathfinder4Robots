#!/usr/bin/python

import rospy
from MapManager import MapManager, MapVisualizer
from std_msgs.msg import String
import os


class MapManager_node():
	def __init__(self):
		self.node = rospy.init_node('mapmanager', log_level= rospy.INFO)

		#self.publisher = pub = rospy.Publisher("mapmanager", String, queue_size = 10)
		'''TODO
		self.mapman = MapManager(os.path.dirname(__file__) + "/" + "Definitions/map.json")
		self.mapman.updateVizImg()
		
		viz = MapVisualizer()
		viz.Draw(self.mapman.getVizImg(), self.mapman.getCollisionImg())
		'''
		rospy.spin()

if __name__ == "__main__":
	mapmanager_node = MapManager_node()