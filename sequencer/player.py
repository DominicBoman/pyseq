from sequencer.clock import Clock
import time

class Player():

	def __init__(self, active_sequence=None):
		self.is_playing = False
		self.clock = Clock(90)
		self.active_sequence=active_sequence
		self.current_step = 0

	def play(self):
		print('play')
		self.is_playing = True

		while (self.is_playing):
			start_ms = time.time()
			if self.active_sequence.pattern.step_enabled(self.current_step):
				print('play sample in pos', self.current_step)
			else:
				print('step disabled in pos', self.current_step)
			
			if self.current_step < self.active_sequence.pattern.get_length() - 1:
				self.current_step += 1
			else:
				self.current_step = 0

			loop_time = (time.time() - start_ms)
			sleep_time = self.clock.step_interval - loop_time
			print('loop time', loop_time)
			print('sleep time', sleep_time)
			time.sleep(sleep_time)

	def stop(self):
		print('stopping')
		self.is_playing = False

	def reset(self):
		self.current_step = 0

		