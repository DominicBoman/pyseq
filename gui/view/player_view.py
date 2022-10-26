import tkinter as tk
from config import IMAGE_PATH
from util.image_loader import *
import time

class Player_View():

	def __init__(self, master_frame):
		self.build(master_frame)
		self.controller = None

	def build(self, master_frame):
		play_icon = load_image(IMAGE_PATH['PLAY'])
		play_button = tk.Button(master_frame, image=play_icon, width=55, height=55, relief=tk.FLAT, command=self.play_command)
		play_button.pack(side=tk.LEFT)
		play_button.image = play_icon

		stop_icon = load_image(IMAGE_PATH['STOP'])
		stop_button = tk.Button(master_frame, image=stop_icon, width=55, height=55, relief=tk.FLAT, command=self.stop_command)
		stop_button.image = stop_icon
		stop_button.pack(side=tk.LEFT)

		reset_icon = load_image(IMAGE_PATH['RESET'])
		reset_button = tk.Button(master_frame, image=reset_icon, width=55 ,height=55 ,relief=tk.FLAT, command=self.reset_command)
		reset_button.image = reset_icon
		reset_button.pack(side=tk.LEFT)

		self.step_counter = tk.Label(master=master_frame, text='0/0')
		self.step_counter.pack(side=tk.RIGHT)
		
	def play_command(self):
		if self.controller:
			self.controller.play()

	def stop_command(self):
		if self.controller:
			self.controller.stop()

	def reset_command(self):
		if self.controller:
			self.controller.reset()

	def change_bpm_command(self, new_bpm):
		if self.controller:
			self.controller.change_bpm(new_bpm)
		