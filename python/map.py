import json


class Map():
	def __init__(self):
		self.MAP_SIZE = (3000, 2000) # units in mm
		
		self.TERRAIN = 0
		self.ENTITIES = 0
		self.OBJECTS

		self.MAP_OBJECTS = {

		}


class JSON_decoder():
	def GetInitMapDict(self, filename):
		MapDict = { # Will be filled with the JSON file.
			"terrain":  {}, # PNG. black pixel is wall, white is free space,
			"lidar":    {}, # latest lidar scan. can be added to the pathfinding map for live object avoidance.
			"entities": {}, # robots : position, shape for collision planning...,
			"objects":  {}, # game objects (collectable and moving things)
			"unknown":  {}  # things the lidar detects that are not recognised but considered as obstacles.
		}
		with open(filename) as f:
			data = json.load(f)

			# Load terrain
			terrain_path = data["terrain"]["fixed_map"]["img_path"]
			MapDict.terrain["img_path"] = terrain_path
			matrix = numpy.asarray(cv.LoadImageM(terrain_path, 1)).tolist()


		return MapDict # returns a python dict ready to be given to the Map





map_dict = {
	"terrain": {
		"img_path": "",
		"img": 0
	},
	"entities": {
		"robot_GR": {
			"position": (0, 0, 0),
			"shape": Shape()
		}
	},
	"objects": {
		"modules": {
			"list": [
				{
					"position": (0, 0, 0),
					"color": 0
				},
				{
					"position": (0, 0, 0),
					"color": 0
				}
			]
		},

		"module_towers": {

		}
	}
}