import rospy, time

class Timer():
	def __init__(self, duration_sec, cb = None):
		self.NODE = rospy.init_node("robot_ai_timer", log_level = rospy.DEBUG)
		self.SUB = rospy.Subscriber("game_timer", queue_size = 10, on_)
		self.duration_sec = duraction_sec

	def start(self):
		self.starttime = time.time() * 1000

	def elapsed_time():
		return (time.time() * 1000 - self.starttime)/1000.0 # return elapsed time in seconds
	def time_left(self):
		return self.duration_sec - self.elapsed_time()
	def is_finished(self):
		return True if self.time_left() < 0 else False

