import random, time
from DouglasPeucker import DouglasPeucker

class Pathfinder():
	def __init__(self):
		pass

	def Execute(self, map_img, start, goal, map_size): # stat and end in original map size coordinates (e.g. 3000x2000)

		# Generate grid
		grid = self.map_to_grid(map_img)
		engine = Engine(grid)

		#Scale start and end to pathfinding coordinates (e.g. 150x100)
		start = self.mm_pos_to_pathfinding_coords(start, map_size, grid.getSizexy())
		goal  = self.mm_pos_to_pathfinding_coords(goal , map_size, grid.getSizexy())

		# Perform search
		path, t = engine.update_path((start[1], start[0]), (goal[1], goal[0])) # the engine wants y then x. Path is returned that way too.

		# Debug
		#print "pathfinding time taken : {0}ms".format(str(t))
		#print "Map size : {0}, grid size : {1}".format(map_size, (grid.width, grid.height))


		# Convert path to the original map resolution && y, x -> x, y
		grid_res = (grid.width, grid.height)
		for i in xrange(len(path)):
			path[i] = self.pathfinding_to_mm_pos_coords((path[i][1], path[i][0]), grid.getSizexy(), map_size) #(path[i][1] * map_size[1] / grid.height, path[i][0] * map_size[0] / grid.width)
		#print "resized path : " + str(path)

		path = self.simplify_path(path) # remove points that are aligned with an existing line
		return path


	def simplify_path(self, path):
		simplified_path = DouglasPeucker(path, tolerance = 1) # no tolerance, just remove aligned points
		#print "simplified path : {0}".format(simplified_path)
		return simplified_path


	def map_to_grid(self, map_img):
		cells = [[Cell(min(pixel[0], 1)) for pixel in line] for line in map_img]
		return Grid(cells)
	def mm_pos_to_pathfinding_coords(self, pos, mm_size, pathfinder_size):
		return (pos[0] * pathfinder_size[0] / mm_size[0], pos[1] * pathfinder_size[1] / mm_size[1]) # x, y
	def pathfinding_to_mm_pos_coords(self, pos, pathfinder_size, mm_size):
		return (pos[0] * mm_size[0] / pathfinder_size[0], pos[1] * mm_size[1] / pathfinder_size[1]) # x, y

	def GetPath_Waypoints(self):
		pass

	def GetPath_Curve(self):
		pass


























#/*=========================================
#=            PATHFINDER ENGINE            =
#=========================================*/

class Cell(object):
	def __init__(self, char):
		self.char = char
		self.tag = 0
		self.index = 0
		self.neighbors = None

class Grid(object):
	def __init__(self, cells):
		self.height, self.width = len(cells), len(cells[0])
		self.cells = cells

	def __contains__(self, pos):
		y, x = pos
		return 0 <= y < self.height and 0 <= x < self.width

	def __getitem__(self, pos):
		y, x = pos
		return self.cells[y][x]

	def neighbors(self, y, x):
		for dy, dx in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),
					   (1, 0), (1, 1)):
			if (y + dy, x + dx) in self:
				yield y + dy, x + dx

	def getSizexy(self):
		return (self.width, self.height) # x, y

class Engine(object):
	def __init__(self, grid):
		self.grid = grid
		self.limit = (grid.height * grid.width) // 2
		self.nodes = {}
		self.path = []

	def update_path(self, startpos, goalpos):
		start_time = time.time() * 1000
		self.goal = goalpos
		self.start = startpos
		def neighbors(pos):
			cell = self.grid[pos]
			if cell.neighbors is None:
				y, x = pos
				cell.neighbors = []
				for neighbor_y, neighbor_x in self.grid.neighbors(y, x):
					if self.grid[neighbor_y, neighbor_x].char != 0: # 0 = wall, 1 = free
						cell.neighbors.append((neighbor_y, neighbor_x))
			return cell.neighbors
		def goal(pos):
			return pos == self.goal
		def cost(from_pos, to_pos):
			from_y, from_x = from_pos
			to_y, to_x = to_pos
			return 14 if to_y - from_y and to_x - from_x else 10
		def estimate(pos):
			y, x = pos
			goal_y, goal_x = self.goal
			dy, dx = abs(goal_y - y), abs(goal_x - x)
			return min(dy, dx) * 14 + abs(dy - dx) * 10
		def debug(nodes):
			self.nodes = nodes
		self.path = ASTAR(startpos, neighbors, goal, 0, cost,
						  estimate, self.limit, debug)
		self.time_taken = int(time.time() * 1000 - start_time)
		return self.path, self.time_taken


# Copyright (c) 2008 Mikael Lind
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from heapq import heappush, heappop
from sys import maxint


# Represent each node as a list, ordering the elements so that a heap of nodes
# is ordered by f = g + h, with h as a first, greedy tie-breaker and num as a
# second, definite tie-breaker. Store the redundant g for fast and accurate
# calculations.

F, H, NUM, G, POS, OPEN, VALID, PARENT = xrange(8)


def ASTAR(start_pos, neighbors, goal, start_g, cost, heuristic, limit=maxint,
		  debug=None):

	"""Find the shortest path from start to goal.

	Arguments:

	  start_pos      - The starting position.
	  neighbors(pos) - A function returning all neighbor positions of the given
					   position.
	  goal(pos)      - A function returning true given a goal position, false
					   otherwise.
	  start_g        - The starting cost.
	  cost(a, b)     - A function returning the cost for moving from one
					   position to another.
	  heuristic(pos) - A function returning an estimate of the total cost
					   remaining for reaching goal from the given position.
					   Overestimates can yield suboptimal paths.
	  limit          - The maximum number of positions to search.
	  debug(nodes)   - This function will be called with a dictionary of all
					   nodes.

	The function returns the best path found. The returned path excludes the
	starting position.
	"""

	# Create the start node.
	nums = iter(xrange(maxint))
	start_h = heuristic(start_pos)
	start = [start_g + start_h, start_h, nums.next(), start_g, start_pos, True,
			 True, None]

	# Track all nodes seen so far.
	nodes = {start_pos: start}

	# Maintain a heap of nodes.
	heap = [start]

	# Track the best path found so far.
	best = start

	while heap:

		# Pop the next node from the heap.
		current = heappop(heap)
		current[OPEN] = False

		# Have we reached the goal?
		if goal(current[POS]):
			best = current
			break

		# Visit the neighbors of the current node.
		for neighbor_pos in neighbors(current[POS]):
			neighbor_g = current[G] + cost(current[POS], neighbor_pos)
			neighbor = nodes.get(neighbor_pos)
			if neighbor is None:

				# Limit the search.
				if len(nodes) >= limit:
					continue

				# We have found a new node.
				neighbor_h = heuristic(neighbor_pos)
				neighbor = [neighbor_g + neighbor_h, neighbor_h, nums.next(),
							neighbor_g, neighbor_pos, True, True, current[POS]]
				nodes[neighbor_pos] = neighbor
				heappush(heap, neighbor)
				if neighbor_h < best[H]:

					# We are approaching the goal.
					best = neighbor

			elif neighbor_g < neighbor[G]:

				# We have found a better path to the neighbor.
				if neighbor[OPEN]:

					# The neighbor is already open. Finding and updating it
					# in the heap would be a linear complexity operation.
					# Instead we mark the neighbor as invalid and make an
					# updated copy of it.

					neighbor[VALID] = False
					nodes[neighbor_pos] = neighbor = neighbor[:]
					neighbor[F] = neighbor_g + neighbor[H]
					neighbor[NUM] = nums.next()
					neighbor[G] = neighbor_g
					neighbor[VALID] = True
					neighbor[PARENT] = current[POS]
					heappush(heap, neighbor)

				else:

					# Reopen the neighbor.
					neighbor[F] = neighbor_g + neighbor[H]
					neighbor[G] = neighbor_g
					neighbor[PARENT] = current[POS]
					neighbor[OPEN] = True
					heappush(heap, neighbor)

		# Discard leading invalid nodes from the heap.
		while heap and not heap[0][VALID]:
			heappop(heap)

	if debug is not None:
		# Pass the dictionary of nodes to the caller.
		debug(nodes)

	# Return the best path as a list.
	path = []
	current = best
	while current[PARENT] is not None:
		path.append(current[POS])
		current = nodes[current[PARENT]]
	path.reverse()
	return path