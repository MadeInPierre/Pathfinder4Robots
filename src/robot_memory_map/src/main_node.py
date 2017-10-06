#!/usr/bin/python
import rospy
from loader import MapLoader
from markers_node import MarkersPublisher

class Map():
    def __init__(self):
        self.NODE = rospy.init_node('map', log_level=rospy.DEBUG)
        MapDict = MapLoader().load("Definitions/map_2018.yml")
        markers = MarkersPublisher(MapDict)
        
        r = rospy.Rate(1)
        while not rospy.is_shutdown():
            markers.publishObjects(MapDict)
            r.sleep()

if __name__ == "__main__":
    Map()
