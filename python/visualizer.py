from objects import *

import numpy as np
import cv2

from matplotlib import pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

class MapVisualizer():
	def __init__(self):
		pass

	def Draw(self, debugView, collisionView):
		plt.imshow(debugView,     interpolation = 'none')
		#plt.figure()
		#plt.imshow(collisionView, interpolation = 'none')
		plt.show()