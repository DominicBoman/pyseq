import tkinter as tk

class Sequence_View():

	def __init__(self, master_frame):
		self.controller = None
		self.step_check_buttons = []
		self.build(master_frame)

	def build(self, master_frame):
		self.sequence_frame = tk.Frame(master_frame)
		self.sequence_settings_frame = tk.Frame(master=self.sequence_frame,height=50, relief=tk.RAISED, borderwidth=5, bg="white")
		self.sequence_settings_frame.pack(fill=tk.X, side=tk.LEFT)
		self.sequence_frame.pack()

	def refresh_pattern(self, steps):
		self.step_check_buttons = []
		
		for child in self.sequence_settings_frame.winfo_children():
			child.destroy()
		
		for i in range(len(steps)):
			print(i)
			check_button = tk.Checkbutton(master=self.sequence_settings_frame, variable=0, command=lambda step_pos=i: self.set_step_command(step_pos))
			check_button.pack(side=tk.LEFT)

	def set_step_command(self, step_pos):
		print(step_pos)
		if self.controller:
			self.controller.set_step(step_pos)

		
		