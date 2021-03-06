import math
import pyclipper
from visualization_msgs.msg import Marker
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
		self.Visual = Visual(initdict["visual"])
		self.Type = initdict["type"]

		self.Chest = initdict["chest"] if "chest" in initdict else False # TODO
		self.UserData = initdict["userdata"]

class Entity():
	def __init__(self, name, initdict):
		self.Name = name
		self.Position = Position(initdict["position"])
		self.Shape = Shape(initdict["shape"])

		self.Chest = initdict["chest"] if "chest" in initdict else False # TODO
		self.Trajectory = Trajectory(initdict["trajectory"])
		self.CurrentPath = []

	def setCurrentPath(self, path):
		self.CurrentPath = path

class Zone():
	def __init__(self, name, initdict):
		self.Name = name
		self.Position = Position(initdict["position"])
		self.Shape = Shape(initdict["shape"])

		self.Walkable = initdict["properties"]["walkable"]
		'''
		self.Properties = {
			"walkable": None,
			"TODO_define_more": None
		}
		for key in self.Properties:
			try:
				self.Properties[key] = initdict["properties"][key]
			except KeyError:
				pass
		'''

class Waypoint():
	def __init__(self, name, initdict):
		self.Name = name
		self.Position = Position(initdict["position"])




'''
LOW LEVEL DEFINITION CLASSES
'''
class Position():
	def __init__(self, initdict):
		self.frame_id = initdict["frame_id"]
		self.x = float(initdict["x"])
		self.y = float(initdict["y"])

		try:
			self.a = float(initdict["a"])
			self.has_angle = True
		except KeyError:
			self.has_angle = False

		self.CollisionType = initdict["type"]

	def transform(self, add_x, add_y):
		p = Position({"x": self.x + add_x, "y": self.y + add_y, "type": self.CollisionType})
		if self.has_angle:
			p.a = self.a
			self.has_angle = True
		return p
	def angle(self):
		return self.a if self.has_angle else 0.0
	def tuple2(self):
		return (self.x, self.y)
	def tuple3(self):
		return (self.x, self.y, self.a) if self.has_angle else None

class Shape():
	def __init__(self, initdict):
		self.Type = initdict["type"]
		if "viz_color" in initdict:
			self.viz_color = Color(initdict["viz_color"])

		if self.Type == "rect":
			self.width  = initdict["width"]
			self.height = initdict["height"]
			self.points = [(0,0), (self.width, 0), (self.width, self.height), (0, self.height)]
			'''
			self.points =  [(- self.width / 2.0, - self.height / 2.0),
							(  self.width / 2.0, - self.height / 2.0),
							(  self.width / 2.0,   self.height / 2.0),
							(- self.width / 2.0,   self.height / 2.0)] # corners centered around the middle
			'''
		elif self.Type == "circle":
			self.radius = initdict["radius"]
		elif self.Type == "polygon":
			self.points = initdict["points"]
		elif self.Type == "line":
			self.start = initdict["start"]
			self.end = initdict["end"]

	def rotated(self, theta):
		"""Rotates the given polygon which consists of corners represented as (x,y),
		around the ORIGIN, clock-wise, theta degrees"""
		if theta == 0:
			return self.points
		if self.Type not in ["rect", "polygon", "polyline"]:
			raise TypeError("This shape ({0}) cannot be rotated.".format(self.Type))

		rotatedPolygon = []
		for corner in self.points:
			rotatedPolygon.append((corner[0]*math.cos(theta)-corner[1]*math.sin(theta) , corner[0]*math.sin(theta)+corner[1]*math.cos(theta)) )
		return rotatedPolygon

	def inflate(self, offset):
		#returns a new shape bigger/smaller to the original one, given the offset amount.
		if offset == 0:
			return self

		if self.Type == "circle":
			return Shape({"type": "circle", "radius": self.radius + offset})
		elif self.Type == "rect":
			return Shape({"type": "rect", "width": self.width + offset, "height": self.height + offset})
		elif self.Type == "polygon":
			clipper = pyclipper.PyclipperOffset()
			clipper.AddPath(self.points, pyclipper.JT_MITER, pyclipper.ET_CLOSEDPOLYGON)
			solution = clipper.Execute(offset)[0]
			return Shape({"type": "polygon", "points": solution})
		else:
			raise TypeError, "Can't inflate this shape type."

class Visual():
	def __init__(self, initdict):
		self.NS = initdict["ns"]
		self.ID = initdict["id"]
		markerType = {
			"cube": Marker.CUBE,
            "sphere": Marker.SPHERE
			#TODO To Complete
		}
		self.Type           = markerType[initdict["type"]]
		self.z              = initdict["z"]
		self.Scale          = initdict["scale"]
		self.Orientation    = initdict["orientation"]
		self.Color          = initdict["color"]

class Trajectory():
	def __init__(self, initdict):
		pass

class Color():
	def __init__(self, color):
		self.RGB = tuple(color)

		if color == "blue":
			self.RGB = (50, 50, 255)
		if color == "yellow":
			self.RGB = (255, 246, 0)
		if color == "gray":
			self.RGB = (175, 175, 175)

		self.R = self.RGB[0]
		self.G = self.RGB[1]
		self.B = self.RGB[2]

	def textColor(self):
		lum = 1 - ( 0.299 * self.R + 0.587 * self.G + 0.114 * self.B)/255 #https://stackoverflow.com/questions/1855884/determine-font-color-based-on-background-color
		return (255, 255, 255) if lum > 0.5 else (0, 0, 0)




'''
import math, pyclipper

class Object():
	def __init__(self):
		self.Pos = [0, 0, 0] # x, y, theta
		self.Shape = Shape("circle", [20, 20, 150])
		self.CollisionShape = self.updateCollisionShape(self.Shape) # shape with brim for safety distance

	def updateShape(self, new_shape):
		pass
	def updateCollisionShape(self, shape, offset):
		clipper = pyclipper.PyclipperOffset()
		clipper.AddPath(shape.GetPolygon(), pyclipper.JT_ROUND, pyclipper.ET_CLOSEDPOLYGON)

		solution = clipper.Execute(offset)



class Shape():
	def __init__(self, shape_type, shape_args):
		self.Polygon = []
		if shape_type == "circle":    # shape_args : [x, y, radius]
			self.Polygon = self._circle_to_polygon((shape_args[0], shape_args[1]), shape_args[2])
		elif shape_type == "polygon": # shape_args : [(vert1x, vert1y), ...]
			self.Polygon = shape_args

	def GetPolygon():
		return self.Polygon

	def _circle_to_polygon(self, pos, radius, sides = 8):
		polygon = []
		a_step = 2*math.pi / float(sides)
		a = 0
		for i in range(sides):
			polygon.append((pos[0] + radius * math.cos(a), pos[1] + radius * math.sin(a)))
			a += a_step
		return polygon
'''
