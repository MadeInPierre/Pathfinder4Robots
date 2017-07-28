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