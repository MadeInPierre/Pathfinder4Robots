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



	def Draw(self, img):
		plt.imshow(img, interpolation = 'none')
		plt.show()