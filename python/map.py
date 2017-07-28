import json


class Map():
	def __init__(self):
		self.MAP_SIZE = (3000, 2000) # units in mm
		
		self.TERRAIN = 0
		self.ENTITIES = 0
		self.OBJECTS

		self.MAP_OBJECTS = {

		}


class JSON_decoder()
	def GetMapDict(self, filename):
		
		with open(filename) as f:    
    		data = json.load(f)
		return {} # return a python dict ready to be given to the Map





map_dict = {
	"terrain": {
		"img_path": "",
		"img": 0
	},
	"entities": {

	},
	"objects": {

	}
}