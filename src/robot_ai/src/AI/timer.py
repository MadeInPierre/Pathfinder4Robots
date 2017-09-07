import rospy, time

'''
Wrapper and communication for the Timer node (located in robot_ai/src/timer_node.py)
'''
class AITimer():
	#TODO create a wrapper for the ai_timer_node service.
	def __init__(self, duration_sec = 0):
		#self.NODE = rospy.init_node("robot_ai_timer", log_level = rospy.DEBUG)
		#self.SUB = rospy.Subscriber("game_timer", queue_size = 10)
		self.duration_sec = duration_sec

	def start(self):
		self.starttime = time.time() * 1000

	def elapsed_time(ms = False):
		return (time.time() * 1000 - self.starttime)/ 1000.0 if not ms else 1.0 # return elapsed time in seconds
	def time_left(self):
		return self.duration_sec - self.elapsed_time()
	def is_finished(self):
		return True if self.time_left() < 0 else False

