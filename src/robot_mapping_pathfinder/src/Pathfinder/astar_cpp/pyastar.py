import ctypes, cv2
from time import time
import numpy as np
import os

class PyAstarCPP():
	def __init__(self):
		lib = ctypes.cdll.LoadLibrary(os.path.dirname(__file__) + '/main.so') #TODO danger
		self.ASTAR = lib.astar
		ndmat_f_type = np.ctypeslib.ndpointer(dtype=np.uint8, ndim=1, flags='C_CONTIGUOUS')
		ndmat_i_type = np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='C_CONTIGUOUS')
		self.ASTAR.restype = ctypes.c_bool
		self.ASTAR.argtypes = [ndmat_f_type, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool, ndmat_i_type]


	def findPath(self, collision_map, start, goal, simplify = True):
		height, width = collision_map.shape[:2]
		start_idx = np.ravel_multi_index(start[::-1], (height, width))
		goal_idx = np.ravel_multi_index(goal[::-1], (height, width))

		#paths = np.full(height * width, -1, dtype = np.int32)
		paths = np.full(500, -1, dtype = np.int32) # TODO Optimize

		success =  self.ASTAR(collision_map.flatten(), 100, 150, start_idx, goal_idx, simplify, paths) # paths is the output parameter
		#print "success : {0}, path : {1}".format(success, paths)


		if not success:
			return np.array([])

		coordinates = []
		for p_idx in paths:
			if p_idx == -1:
				break
			pi, pj = np.unravel_index(p_idx, (height, width))
			coordinates.append((pj, pi)) # revert back to x, y

		if coordinates and coordinates[0] == goal: # if the end coordinate is not the goal, return an empty path
			return np.array(coordinates[::-1])
		else:
			print " | ERROR : Invalid path."
			return np.array([])

		return []