import random, time
from DouglasPeucker import DouglasPeucker
from astar_cpp2 import PyAstar

class Pathfinder():
	def __init__(self):
		self.PYASTAR = PyAstar()

	def Execute(self, map_img, start_mm, goal_mm, map_size): # stat and end in original map size coordinates (e.g. 3000x2000)
		gridSize = map_img.shape[1::-1] # y, x

		# Scale start and end to pathfinding coordinates (e.g. 150x100)
		start = self.mm_pos_to_pathfinding_coords(start_mm, map_size, gridSize)
		goal  = self.mm_pos_to_pathfinding_coords(goal_mm , map_size, gridSize)

		#Pathfinder call
		path = self.PYASTAR.findPath(map_img, start, goal)
		
		# Convert path to the original map resolution && y, x -> x, y
		for i in xrange(len(path)):
			path[i] = self.pathfinding_to_mm_pos_coords(path[i], gridSize, map_size) #(path[i][1] * map_size[1] / grid.height, path[i][0] * map_size[0] / grid.width)
		return path
		return self.simplify_path(path) if len(path) > 0 else path



	def simplify_path(self, path):
		simplified_path = DouglasPeucker(path, tolerance = 1) # no tolerance, just remove aligned points
		#print "simplified path : {0}".format(simplified_path)
		return simplified_path
	
	def mm_pos_to_pathfinding_coords(self, pos, mm_size, pathfinder_size):
		return (pos[0] * pathfinder_size[0] / mm_size[0], pos[1] * pathfinder_size[1] / mm_size[1]) # x, y
	def pathfinding_to_mm_pos_coords(self, pos, pathfinder_size, mm_size):
		return (pos[0] * mm_size[0] / pathfinder_size[0], pos[1] * mm_size[1] / pathfinder_size[1]) # x, y





'''
		# Generate grid
		grid = self.map_to_grid(map_img)
		engine = Engine(grid)

		#Scale start and end to pathfinding coordinates (e.g. 150x100)
		start = self.mm_pos_to_pathfinding_coords(start, map_size, grid.getSizexy())
		goal  = self.mm_pos_to_pathfinding_coords(goal , map_size, grid.getSizexy())

		# Perform search
		path, t = engine.update_path((start[1], start[0]), (goal[1], goal[0])) # the engine wants y then x. Path is returned that way too.

		# Debug
		print "pure pathfinding time taken : {0}ms".format(str(t))
		#print "Map size : {0}, grid size : {1}".format(map_size, (grid.width, grid.height))


		# Convert path to the original map resolution && y, x -> x, y
		grid_res = (grid.width, grid.height)
		for i in xrange(len(path)):
			path[i] = self.pathfinding_to_mm_pos_coords(path[i][::-1], grid.getSizexy(), map_size) #(path[i][1] * map_size[1] / grid.height, path[i][0] * map_size[0] / grid.width)
		#print "resized path : " + str(path)

		path = self.simplify_path(path) # remove points that are aligned with an existing line
		return path




	def map_to_grid(self, map_img):
		cells = [[Cell(min(pixel[0], 1)) for pixel in line] for line in map_img]
		return Grid(cells)

	def GetPath_Waypoints(self):
		pass

	def GetPath_Curve(self):
		pass


























#/*=========================================
#=            PATHFINDER ENGINE            =
#=========================================*/

# Author: Christian Careaga (christian.careaga7@gmail.com)
# A* Pathfinding in Python (2.7)
# Please give credit if used
# Source : http://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/

import numpy
from heapq import *

class ASTAR():
	def execute(self, array, start, goal):
		print array
		def heuristic(a, b):
			return 14 if abs(b[0] - a[0]) == abs(b[1] - a[1]) else 10 # 14 if diagonal, 10 straight line
			#return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

		neighbors = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

		close_set = set()
		came_from = {}
		gscore = {start:0}
		fscore = {start:heuristic(start, goal)}
		oheap = []

		heappush(oheap, (fscore[start], start))
		
		while oheap:
			current = heappop(oheap)[1]

			if current == goal:
				data = []
				while current in came_from:
					data.append(current)
					current = came_from[current]
				return data[::-1]

			close_set.add(current)
			for i, j in neighbors:
				neighbor = current[0] + i, current[1] + j            
				tentative_g_score = gscore[current] + heuristic(current, neighbor)
				if 0 <= neighbor[0] < array.shape[0]:
					if 0 <= neighbor[1] < array.shape[1]:                
						if array[neighbor[0]][neighbor[1]][0] == 0:
							continue
					else:
						# array bound y walls
						continue
				else:
					# array bound x walls
					continue
					
				if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
					continue
					
				if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
					came_from[neighbor] = current
					gscore[neighbor] = tentative_g_score
					fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
					heappush(oheap, (fscore[neighbor], neighbor))
					
		return []
'''

'''Here is an example of using my algo with a numpy array,
   astar(array, start, destination)
   astar function returns a list of points (shortest path)'''
'''
nmap = numpy.array([
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[1,1,1,1,1,1,1,1,1,1,1,1,0,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[1,0,1,1,1,1,1,1,1,1,1,1,1,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[1,1,1,1,1,1,1,1,1,1,1,1,0,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[1,0,1,1,1,1,1,1,1,1,1,1,1,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[1,1,1,1,1,1,1,1,1,1,1,1,0,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
	
print astar(nmap, (0,0), (10,13))
'''