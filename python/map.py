import json
import numpy as np
import cv2
from visualizer import *
from objects import *

'''
The Map class keeps a Dict containing everything in the environment.
The final output can be an image representing all objects and terrain.
'''

'''
JSON FILE map_init.json COMMENTS : 
	- Terrain contains non-interactive features :
		- Walls
		- Pre-defined zones (e.g. Goal zone, danger zone, etc)
		- Positions 

Positions :
	- Type : fixed (no pos update, can't move), TODO movable AND/or dynamic ?
		If the movement is dynamic, keep track of position modifications.
'''


class MapManager():
	def __init__(self, initfile_path):
		self.MapDict = self.load_initfile(initfile_path)
		self.Dirty = False # Each time an object is modified, this flag is set to True

	def load_initfile(self, filename):
		# Reads the JSON map init file to fill MapDict at its initial state.
		MapDict = {
		}
		with open(filename) as f:
			json_str = f.read()

			MapDict = json.loads(json_str) # transform the map_init json into the main MapDict skeleton.
			print json.dumps(MapDict, indent = 4, sort_keys = False)

			# Next, replace init values with actual python object classes :
			# -------- Terrain
			zones = MapDict["terrain"]["zones"]
			for zone in zones:
				zones[zone] = Zone(zone, zones[zone])

			waypoints = MapDict["terrain"]["waypoints"]
			for waypoint in waypoints:
				waypoints[waypoint] = Waypoint(waypoint, waypoints[waypoint])

			MapDict["terrain"]["walls"]["img"] = cv2.imread(MapDict["terrain"]["walls"]["img_path"])
			MapDict["terrain"]["walls"]["viz_img"] = cv2.resize(MapDict["terrain"]["walls"]["img"], (3000, 2000), interpolation = cv2.INTER_NEAREST)

			# -------- Entities
			entities = MapDict["entities"]
			for entity in entities:
				entities[entity] = Entity(entity, entities[entity])

			# -------- Objects
			objects = MapDict["objects"]
			for obj in objects:
				objects[obj] = Object(obj, objects[obj])

		self.Dirty = True
		return MapDict


	def getObject(self, objectname):
		pass

	def containerTransfer(self, container1, container2, objectname):
		'''
		A container (e.g. a tower of modules, the robot's balls container...) has a list of objects.
			The transfer function moves an object from a container to another.
		'''
		pass




map = MapManager("map_init.json")
viz = MapVisualizer()
viz.Draw(map)