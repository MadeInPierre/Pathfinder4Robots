from objects import *

import numpy as np
import cv2

from matplotlib import pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

class MapVisualizer():
	def __init__(self):
		self.CONFIG = {
			"WindowRes": (1920, 1080),
			"colors": {
				"free": (255, 255, 255),
				"walls": (0, 0, 0),

				"zones": (145, 255, 172),
				"waypoints": (255, 100, 20),

				"entities": (255, 50, 50),

				"fixed_objects": (50, 50, 255),
				"dynamic_objects": (50, 255, 50)
			},
			"scale": {
				"waypoints_size": 30
			},
			"filters": {
				"show_objects": True,
				"show_trajectories": False
			}
		}



	def Draw(self, map):
		walls_img = map.MapDict["terrain"]["walls"]["viz_img"]

		# Zones
		for zone in map.MapDict["terrain"]["zones"]:
			z = map.MapDict["terrain"]["zones"][zone]
			self.draw_shape(walls_img, z.Position, z.Shape, color = self.CONFIG["colors"]["zones"])

		# Waypoints
		for waypoint in map.MapDict["terrain"]["waypoints"]:
			w = map.MapDict["terrain"]["waypoints"][waypoint]
			shape = Shape( {"type": "circle", "radius": self.CONFIG["scale"]["waypoints_size"]})
			self.draw_shape(walls_img, w.Position, shape, color = self.CONFIG["colors"]["waypoints"])

		# Entities
		for entity in map.MapDict["entities"]:
			e = map.MapDict["entities"][entity]
			self.draw_shape(walls_img, e.Position, e.Shape, color = self.CONFIG["colors"]["entities"])

		# Objects
		for obj in map.MapDict["objects"]:
			o = map.MapDict["objects"][obj]
			self.draw_shape(walls_img, o.Position, o.Shape, color = o.Shape.viz_color.RGB)	

			if o.Type == "container":
				cv2.putText(walls_img, str(len(o.Chest)), o.Position.tuple2(translation = (-15, 15)), cv2.FONT_HERSHEY_SIMPLEX, 1.5, o.Shape.viz_color.textColor(), thickness = 5)		


		plt.imshow(walls_img)
		plt.show()


	def draw_shape(self, img, position, shape, color = (255, 0, 0), width = -1): # width = -1 -> fill shape.
		if   shape.Type == "rect":
			if position.angle() == 0:
				self.draw_rect(img, position.x, position.y, shape.width, shape.height, color, width)
			else:
				self.draw_poly(img, position.x, position.y, shape.rotated(position.angle()), color, width)
		elif shape.Type == "circle":
			self.draw_circle(img, position.x, position.y, shape.radius, color, width)
		elif shape.Type == "polygon":
			self.draw_poly(img, position.x, position.y, shape.rotated(position.angle()), color, width)

	def draw_rect(self, img, x, y, w, h, color = (255, 0, 0), width = -1):
		cv2.rectangle(img, (x, y), (x+w, y+h), color, width)
	def draw_circle(self, img, x, y, rad, color = (255, 0, 0), width = -1):
		cv2.circle(img, (x, y), rad, color, width)
	def draw_poly(self, img, x, y, points, color = (255, 0, 0), width = -1):
		pts = [(p[0] + x, p[1] + y) for p in points]
		pts = np.array(pts, np.int32)
		pts = pts.reshape((-1,1,2))

		if width == -1:
			cv2.fillPoly(img, [pts], color)
		else:
			cv2.polylines(img, [pts], True, color)
		pass