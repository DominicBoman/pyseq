import tkinter as tk
from threading import Thread
from gui.util.icon_loader import *
import time

class Player_View():

	def __init__(self, master_frame, player):
		self.player = player
		self.build(master_frame)
		update_thread = Thread(target=self.update)
		update_thread.start()

	def build(self, master_frame):
		play_icon = load_icon(PLAY_ICON)
		play_button = tk.Button(master_frame, image=play_icon, width=55, height=55, relief=tk.FLAT, command=self.play)
		play_button.pack(side=tk.LEFT)
		play_button.image = play_icon

		stop_icon = load_icon(STOP_ICON)
		stop_button = tk.Button(master_frame, image=stop_icon, width=55, height=55, relief=tk.FLAT, command=self.stop)
		stop_button.image = stop_icon
		stop_button.pack(side=tk.LEFT)

		reset_icon = load_icon(RESET_ICON)
		reset_button = tk.Button(master_frame, image=reset_icon, width=55 ,height=55 ,relief=tk.FLAT, command=self.reset)
		reset_button.image = reset_icon
		reset_button.pack(side=tk.LEFT)

		self.step_counter = tk.Label(master=master_frame, text='{}/{}'.format(self.player.current_step, self.player.active_sequence.pattern.get_length()))
		self.step_counter.pack(side=tk.RIGHT)

	def update(self):
		while True:
			self.step_counter.config(text='{}/{}'.format(self.player.current_step, self.player.active_sequence.pattern.get_length()))
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
		