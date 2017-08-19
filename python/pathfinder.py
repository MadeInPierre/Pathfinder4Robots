import random, time
from DouglasPeucker import DouglasPeucker
from astar_cpp import PyAstarCPP

class Pathfinder():
	def __init__(self):
		self.PYASTAR = PyAstarCPP()




	def Execute(self, map_manager, start_mm, goal_mm): # stat and end in original map size coordinates (e.g. 3000x2000)
		print "\n[PATHFINDING]"
		t = time.time() * 1000 # DEBUG Benchmarking start

		map_size = map_manager.getMapSize()
		map_manager.updateCollisionImg(offset = 160)

		gridSize = map_manager.getCollisionImg().shape[1::-1] # y, x

		# Scale start and end to pathfinding coordinates (e.g. 150x100)
		start = self.mm_pos_to_pathfinding_coords(start_mm, map_size, gridSize)
		goal  = self.mm_pos_to_pathfinding_coords(goal_mm , map_size, gridSize)

		#Pathfinder call
		path = self.PYASTAR.findPath(map_manager.getCollisionImg(), start, goal, simplify = True)
		
		# Convert path to the original map resolution && y, x -> x, y
		for i in xrange(len(path)):
			path[i] = self.pathfinding_to_mm_pos_coords(path[i], gridSize, map_size)

		print " | TOTAL TIME : {0}ms\n".format(int(time.time() * 1000 - t))
		return path




	def mm_pos_to_pathfinding_coords(self, pos, mm_size, pathfinder_size):
		return (pos[0] * pathfinder_size[0] / mm_size[0], pos[1] * pathfinder_size[1] / mm_size[1]) # x, y
	def pathfinding_to_mm_pos_coords(self, pos, pathfinder_size, mm_size):
		return (pos[0] * mm_size[0] / pathfinder_size[0], pos[1] * mm_size[1] / pathfinder_size[1]) # x, y