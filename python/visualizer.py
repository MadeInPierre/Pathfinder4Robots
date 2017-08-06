import numpy as np
import cv2
from matplotlib import pyplot as plt

class MapVisualizer():
	def __init__(self):
		self.CONFIG = {
			"WindowRes": (1920, 1080),
			"colors": {
				"free": (255, 255, 255),
				"walls": (0, 0, 0),
				"zones": (120, 120, 255),
				"waypoints": (255, 140, 20),
				"fixed_objects": (50, 50, 255),
				"dynamic_objects": (50, 255, 50),
				"entities": (50, 120, 50)
			},
			"filters": {
				"show_objects": True,
				"show_trajectories": False
			}
		}



	def Draw(self, map):
		img = map.MapDict["terrain"]["walls"]["img"]

		# Zones
		for zone in map.MapDict["terrain"]["zones"]:
			z = map.MapDict["terrain"]["zones"][zone]
			cv2.rectangle(img, (z.Position.x, z.Position.y),  \
							   (z.Position.x + z.Shape.width, z.Position.y + z.Shape.height), self.CONFIG["colors"]["zones"], -1)

		# Waypoints
		for waypoint in map.MapDict["terrain"]["waypoints"]:
			w = map.MapDict["terrain"]["waypoints"][waypoint]
			cv2.rectangle(img, (w.Position.x - 25, w.Position.y - 25),  \
							   (w.Position.x + 50, w.Position.y + 50), self.CONFIG["colors"]["waypoints"], -1)
		plt.imshow(img)
		plt.show()