import json, copy, cv2, time
import numpy as np
from visualizer import *
from objects import *
from pathfinder import Pathfinder

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
		self.renderer = Renderer()
		self.MapDict = self.load_initfile(initfile_path)
		self.Dirty = False # Each time an object is modified, this flag is set to True

	def load_initfile(self, filename):
		# Reads the JSON map init file to fill MapDict at its initial state.
		MapDict = {}
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
			MapDict["terrain"]["walls"]["img"] = self.renderer.resizeImage(MapDict["terrain"]["walls"]["img"], (3000, 2000)) # TODO automate size

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

	def dirty(self):
		self.Dirty = True
		#TODO redraw and/or log changes
		self.Dirty = False

	#/*===========================================
	#=            Getters and Setters            =
	#===========================================*/

	def getMapSize(self):
		return (self.MapDict["terrain"]["map_size"]["width"], self.MapDict["terrain"]["map_size"]["height"])

	def getTerrainImg(self):
		return self.MapDict["terrain"]["walls"]["img"]
	def getVizImg(self):
		return self.MapDict["terrain"]["walls"]["viz_img"]
	def setVizImg(self, img):
		self.MapDict["terrain"]["walls"]["viz_img"] = img
	def getCollisionImg(self):
		return self.MapDict["terrain"]["walls"]["pathfinder_img"]
	def setCollisionImg(self, img):
		self.MapDict["terrain"]["walls"]["pathfinder_img"] = img

	def getZones(self):
		return self.MapDict["terrain"]["zones"]
	def getZone(self, zonename):
		return self.getZones()[zonename] if zonename in self.getZones() else None

	def getWaypoints(self):
		return self.MapDict["terrain"]["waypoints"]
	def getWaypoint(self, waypointname):
		return self.getWaypoints()[waypointname] if waypointname in self.getWaypoints() else None

	def getEntities(self):
		return self.MapDict["entities"]
	def getEntity(self, entityname):
		return self.getEntities()[entityname] if entityname in self.getEntities() else None

	def getObjects(self):
		return self.MapDict["objects"]
	def getObject(self, objectname):
		return self.getObjects()[objectname] if objectname in self.getObjects() else None
	
	#/*=====  End of Getters and Setters  ======*/
	


	def containerTransfer(self, containerFrom, containerDestination, objectname):
		'''
		A container (e.g. a tower of modules, the robot's balls container...) has a list of objects.
			The fucntion moves an object from a container to another.
		'''
		if isinstance(containerFrom, dict) and isinstance(containerDestination, dict) and objectname in containerFrom:
			containerDestination[objectname] = containerFrom[objectname]
			del containerFrom[objectname]
			self.dirty()
		else:
			raise KeyError


	#/*==================================
	#=            Generators             =
	#===================================*/
	
	def updateVizImg(self):
		self.setVizImg(self.renderer.generateDebugImg(self))
	def updateCollisionImg(self, offset):
		self.setCollisionImg(self.renderer.generateCollisionImg(self, offset))

	
	#/*=====  End of Generators  ======*/
	

class Renderer():
	def __init__(self):
		self.CONFIG = {
			"res":      (3000, 2000),
			"finalRes": (3000, 2000),
			"save_binary": False,
			"BW": False,
			"show_walkable": True,
			"show_HUD": True,
			"offset": 0,

			"terrain": {
				"showWalls": True,
			},
			"collisionmap": {
				"show": True
			},
			"zones": {
				"show": True,
				"color": (145, 255, 172)
			},
			"waypoints": {
				"show": True,
				"color": (255, 100, 20),
				"size": 10
			},
			"entities": {
				"show": True,
				"showCurrentPath": True,
				"blacklist": []
			},
			"objects": {
				"show": True
			}
		}

	def generateCollisionImg(self, mapmanager, offset):
		config = copy.deepcopy(self.CONFIG)
		config["finalRes"] = (150, 100)
		config["BW"] = True
		config["show_walkable"] = False
		config["show_HUD"] = False

		config["offset"] = offset

		config["collisionmap"]["show"] = False
		config["waypoints"]["show"]    = False
		config["entities"]["showCurrentPath"] = False # TODO generate it so that the robot avoids intercepting a moving robot if we know its path ?
		config["entities"]["blacklist"].append("ROBOT") # Don't draw the robot itself.

		return self.draw(mapmanager, config)

	def generateDebugImg(self, mapmanager):
		return self.draw(mapmanager, self.CONFIG)



	def draw(self, mapmanager, CONFIG):
		img = copy.deepcopy(mapmanager.getCollisionImg() if CONFIG["collisionmap"]["show"] else mapmanager.getTerrainImg())

		if CONFIG["res"] != (len(img[0]), len(img)): #TODO badly done
			img =  self.resizeImage(img, CONFIG["finalRes"])

		# Zones
		if CONFIG["zones"]["show"]:
			for zonename in mapmanager.getZones(): 
				z = mapmanager.getZone(zonename)
				if (CONFIG["show_walkable"] and z.Walkable) or not CONFIG["show_walkable"]:
					self.draw_shape(img, z.Position, z.Shape.inflate(CONFIG["offset"] if not z.Walkable else 0), 
									color = self.adjust_color(CONFIG["zones"]["color"], CONFIG))

		# Waypoints
		if CONFIG["waypoints"]["show"]:
			for waypointname in mapmanager.getWaypoints():
				w = mapmanager.getWaypoint(waypointname)
				shape = Shape( {"type": "circle", "radius": CONFIG["waypoints"]["size"]})
				self.draw_shape(img, w.Position, shape.inflate(CONFIG["offset"]), 
					color = self.adjust_color(CONFIG["waypoints"]["color"], CONFIG))

		# Entities
		if CONFIG["entities"]["show"]:
			for entityname in mapmanager.getEntities():
				if entityname not in CONFIG["entities"]["blacklist"]: # Don't draw blacklisted entities
					e = mapmanager.getEntity(entityname)
					self.draw_shape(img, e.Position, e.Shape.inflate(CONFIG["offset"]), 
									color = self.adjust_color(e.Shape.viz_color.RGB, CONFIG))
					if CONFIG["show_HUD"] and e.Chest:
						self.draw_shape(img, e.Position.transform(-40, -40), Shape({"type": "rect", "width": 80, "height": 80}), color = (0, 0, 0))
						self.draw_shape(img, e.Position.transform(-40, -40), Shape({"type": "rect", "width": 80, "height": 80}), color = (255, 255, 255), width = 2)
						cv2.putText(img, str(len(e.Chest)), e.Position.transform(0, 0).tuple2(), cv2.FONT_HERSHEY_SIMPLEX, 1.5, e.Shape.viz_color.textColor(), thickness = 5)						

					if CONFIG["entities"]["showCurrentPath"]:
						print "{0} path : {1}".format(entityname, e.CurrentPath)
						for i in xrange(len(e.CurrentPath) - 1):
							self.draw_shape(img, Position({"x": 0, "y": 0, "type": "ghost"}),
												 Shape({"type": "line", "start": e.CurrentPath[i], "end": e.CurrentPath[i+1]}),
												 color = (0, 255, 0), width = 8)

		# Objects
		if CONFIG["objects"]["show"]:
			for obj in mapmanager.getObjects():
				o = mapmanager.getObject(obj)
				self.draw_shape(img, o.Position, o.Shape.inflate(CONFIG["offset"]), 
								color = self.adjust_color(o.Shape.viz_color.RGB, CONFIG))

				if CONFIG["show_HUD"] and o.Type == "container":
					cv2.putText(img, str(len(o.Chest)), o.Position.transform(-15, 15).tuple2(), cv2.FONT_HERSHEY_SIMPLEX, 1.5, o.Shape.viz_color.textColor(), thickness = 5)		

		if CONFIG["finalRes"] != (len(img[0]), len(img)): #TODO badly done
			img =  self.resizeImage(img, CONFIG["finalRes"])
		if CONFIG["save_binary"]:
			img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1] #https://stackoverflow.com/questions/7624765/converting-an-opencv-image-to-black-and-white
		return img

	def adjust_color(self, color, CONFIG):
		return color if not CONFIG["BW"] else (0, 0, 0)


	#/*=======================================
	#=            Drawing helpers            =
	#=======================================*/
	def draw_shape(self, img, position, shape, color = (255, 0, 0), width = -1): # width = -1 -> fill shape.
		if shape.Type == "rect":
			if position.angle() == 0:
				self.draw_rect(img, position.x, position.y, shape.width, shape.height, color, width)
			else:
				self.draw_poly(img, position.x, position.y, shape.rotated(position.angle()), color, width)
		elif shape.Type == "circle":
			self.draw_circle(img, position.x, position.y, shape.radius, color, width)
		elif shape.Type == "polygon":
			self.draw_poly(img, position.x, position.y, shape.rotated(position.angle()), color, width)
		elif shape.Type == "line":
			self.draw_line(img, position.x, position.y, shape.start, shape.end, color, width)

	def draw_rect(self, img, x, y, w, h, color = (255, 0, 0), width = -1):
		cv2.rectangle(img, (x, y), (x+w, y+h), color, width)
	def draw_circle(self, img, x, y, rad, color = (255, 0, 0), width = -1):
		cv2.circle(img, (x, y), rad, color, width)
	def draw_poly(self, img, x, y, points, color = (255, 0, 0), width = -1):
		pts = [(p[0] + x, p[1] + y) for p in points]
		pts = np.array(pts, np.int32).reshape((-1,1,2))
		cv2.fillPoly(img, [pts], color) if width == -1 else cv2.polylines(img, pts, True, color, width = width)
	def draw_line(self, img, x, y, start, end, color = (255, 0, 0), width = 1):
		startpos = (start[0] + x, start[1] + y)
		endpos   = (end[0]   + x, end[1]   + y)
		cv2.line(img, startpos, endpos, color, thickness = width)
	#/*=====  End of Drawing helpers  ======*/


	#/*=============================================
	#=            Helpers            =
	#=============================================*/
	def resizeImage(self, img, new_size, AA = False):
		i = cv2.INTER_NEAREST if AA else cv2.INTER_NEAREST #TODO find the name for AntiAlliasing
		return cv2.resize(img, new_size, interpolation = i)


	#/*=====  End of Helpers  ======*/





t = time.time() * 1000

mapman = MapManager("map_init.json")
#map.containerTransfer(map.getObject("tower_1").Chest, map.getEntity("ROBOT").Chest, "module_1")

#Pathfinder
pfinder = Pathfinder()
mapman.updateCollisionImg(offset = 180)
mapman.getEntity("ROBOT").setCurrentPath(pfinder.Execute(mapman.getCollisionImg(), mapman.getEntity("ROBOT").Position.tuple2(), (2700, 1800), mapman.getMapSize()))

print "PATHFINDER CALC TOTAL TIME : {0}ms".format(time.time() * 1000 - t)
mapman.updateVizImg()


viz = MapVisualizer()
viz.Draw(mapman.getVizImg(), mapman.getCollisionImg())

