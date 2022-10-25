import tkinter as tk

class Sequence_List_View():

	def __init__(self, master, sequence_list, active_sequence):
		self.frame = tk.Frame(master)
		self.sequence_list = sequence_list
		self.active_sequence = active_sequence
		self.update()

	def update(self):
		num = 1
		print(self.sequence_list)
		for sequence in self.sequence_list:
			sequence_frame = tk.Frame(master=self.frame,height=50, relief=tk.RAISED, borderwidth=5, bg="white")
			sequence_frame.pack(fill=tk.X, side=tk.TOP)
			main_label = tk.Label(master=sequence_frame, text="sequence {num}")
			main_label.pack()
			num = num + 1

		self.frame.pack()
		
		