import json

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

			# -------- Entities
			entities = MapDict["entities"]
			for entity in entities:
				entities[entity] = Entity(entity, entities[entity])

			# -------- Objects
			objects = MapDict["objects"]
			for obj in objects:
				objects[obj] = Object(obj, objects[obj])


		return MapDict


	def getObject(self, objectname):
		pass





'''
HIGH LEVEL DEFINITION CLASSES
'''

'''TODO
class obj():
	def __init(self, initdict):
		self.Name = name
		self.Position = Position(initdict["position"])
'''
class Object():
	def __init__(self, name, initdict):
		self.Name = name
		self.Position = Position(initdict["position"])
		self.Shape = Shape(initdict["shape"])
		
		self.Chest = True if "chest" in initdict else None # TODO
		self.UserData = initdict["userdata"]

class Entity():
	def __init__(self, name, initdict):
		self.Name = name
		self.Position = Position(initdict["position"])
		self.Shape = Shape(initdict["shape"])

		self.Chest = True if "chest" in initdict else None # TODO
		self.Trajectory = Trajectory(initdict["trajectory"])

class Zone():
	def __init__(self, name, initdict):
		self.Name = name
		self.Position = Position(initdict["position"])
		self.Shape = Shape(initdict["shape"])

		self.Properties = {
			"walkable": None,
			"TODO_define_more": None
		}
		for key in self.Properties:
			try:
				self.Properties[key] = initdict["properties"][key]
			except KeyError:
				pass

class Waypoint():
	def __init__(self, name, initdict):
		self.Name = name
		self.Position = Position(initdict["position"])

'''
LOW LEVEL DEFINITION CLASSES
'''
class Position():
	def __init__(self, initdict):
		self.x = int(initdict["x"])
		self.y = int(initdict["y"])

		try:
			self.a = float(initdict["a"])
			self.has_angle = True
		except KeyError:
			self.has_angle = False

		self.CollisionType = initdict["type"]

class Shape():
	def __init__(self, initdict):
		type = initdict["type"]

		self.Type = type
		if type == "rect":
			self.width  = initdict["width"]
			self.height = initdict["height"]
		elif type == "circle":
			self.radius = initdict["radius"]
		elif type == "polygon":
			self.points = initdict["points"]

class Trajectory():
	def __init__(self, initdict):
		pass






'''
class JSON_decoder():
	def GetInitMapDict(self, filename):
		MapDict = { # Will be filled with the JSON file.
			"terrain":    {},  # PNG. black pixel is wall, white is free space,
			"lidar":      {},  # latest lidar scan. can be added to the pathfinding map for live object avoidance.
			"entities":   {},  # robots : position, shape for collision planning...,
			"objects":    {},  # game objects (collectable and moving things)
			"unknown":    {},  # things the lidar detects that are not recognised but considered as obstacles.

			"trajectory": {}   # Keeps records of the moves the robot made.
		}
		with open(filename) as f:
			data = json.load(f)

			# Load terrain
			terrain_path = data["terrain"]["fixed_map"]["img_path"]
			MapDict.terrain["img_path"] = terrain_path
			matrix = numpy.asarray(cv.LoadImageM(terrain_path, 1)).tolist()


		return MapDict # returns a python dict ready to be given to the Map
'''




map_dict = {
	"terrain": {
		"map_weigth": 3000,
		"map_height": 2000,
		"walls_img": {
			"path": "",
			"data": 0
		},
		"zones": {
			"goal": {
				"shape": {
					"type": "rect",
					"data": "0,0,3,3"
				}
			}
		},
		"points": {

		}
	},
	"entities": {
		"robot_GR": {
			"position": (0, 0, 0),
			"shape": 0 
		}
	},
	"objects": {
		"fixed": {

		},
		"dynamic": {

		}
	}
}

map = MapManager("map_init.json")
