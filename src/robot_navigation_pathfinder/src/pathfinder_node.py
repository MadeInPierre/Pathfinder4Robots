#!/usr/bin/python

import rospy
from Pathfinder import Pathfinder
from std_msgs.msg import String
import os

from robot_mapping_pathfinder.srv import *
from geometry_msgs.msg import Pose2D


class MapManager_node():
	def __init__(self):
		self.pathfinder = Pathfinder()

		#self.publisher = pub = rospy.Publisher("pathfinder", String, queue_size = 10)
		self.NODE = rospy.init_node('mapping_pathfinder', log_level= rospy.DEBUG)

		# GetPath Service creation
		getpath_service = rospy.Service('MappingPathfinderGetPathService', MappingPathfinderGetPathService, self.handlesrv_GetPath)
		print "Initialized getpath service"
		rospy.spin()


	def handlesrv_GetPath(self, req):
		print "Asked to go from ({},{},{}) to ({},{},{})".format(req.startpos.x, req.startpos.y, req.startpos.theta,
																 req.endpos.x,   req.endpos.y,   req.endpos.theta)
		
		res = MappingPathfinderGetPathServiceResponse()
		res.waypoints = [Pose2D(1, 1, 1), Pose2D(2, 2, 2), Pose2D(3, 3, 3)]
		return res

if __name__ == "__main__":
	mapmanager_node = MapManager_node()




