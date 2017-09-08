#!/usr/bin/python
import rospy, time

from robot_ai.srv import AIGenericCommand, AIGenericCommandResponse
from robot_ai.msg import ai_timer

'''
TIME UNIT IN SECONDS
'''
class TimerNode():
	def __init__(self):
		self.DepartmentName = "ai"
		self.PackageName = "timer"
		self.NODE = rospy.init_node(self.PackageName, log_level = rospy.INFO)
		self.SERV = rospy.Service(  self.PackageName, AIGenericCommand, self.on_srv_request)
		self.PUBL = rospy.Publisher("/timer", ai_timer, queue_size = 10)

		self.Duration = None
		self.Started = False

		self.run()

	def on_srv_request(self, req):
		res_code, reason = 200, ""
		if req.command == "timer_start":
			self.start()
		elif req.command == "timer_set_duration":
			self.Duration = int(req.params)
		else:
			rospy.logerr("robot_ai_timer got non-recognized command '{}'.".format(req.command))
			res_code, reason = 404, "command not recognized"
		return AIGenericCommandResponse(res_code, reason)

	def run(self):
		rate = rospy.Rate(10) # 10hz
		while not rospy.is_shutdown():
			if self.Started:
				msg = ai_timer()
				msg.elapsed_time = self.elapsed_time()
				msg.time_left = -1 if not self.Duration else self.time_left()
				msg.is_finished = self.is_finished()
				self.PUBL.publish(msg)
				rate.sleep()

	def start(self):
		self.starttime = time.time() * 1000
		self.Started = True

	def elapsed_time(self):
		return (time.time() * 1000 - self.starttime) / 1000.0 # return elapsed time in seconds
	def time_left(self):
		return self.Duration - self.elapsed_time()
	def is_finished(self):
		return True if self.time_left() < 0 else False


if __name__ == "__main__":
	timer = TimerNode()
