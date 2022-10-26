from threading import Thread
import time

class Player_Controller():

	def __init__(self, player, player_view):
		self.player = player
		self.player_view = player_view
		update_thread = Thread(target=self.step_counter_update)
		update_thread.start()

	def step_counter_update(self):
		while True:
			if self.player.active_sequence:
				self.player_view.step_counter.config(text='{}/{}'.format(self.player.current_step, self.player.active_sequence.pattern.get_length()))
				time.sleep(.1)
		
	def play(self):
		if not self.player.is_playing:
			player_thread = Thread(target=self.player.play)
			player_thread.start()

	def stop(self):
		if self.player.is_playing:
			self.player.stop()

	def reset(self):
		self.player.reset()

	def change_bpm(self, new_bpm):
		self.player.clock.set_bpm(new_bpm)
		