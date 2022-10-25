import tkinter as tk

class Root_View():

	def __init__(self, master_frame):
		self.header_frame = self.create_header_frame(master_frame)
		self.body_frame = self.create_body_frame(master_frame)
		self.sequence_list_frame = self.create_sequence_list_frame(self.body_frame)
		self.sequence_frame = self.create_sequence_frame(self.body_frame)

	def create_header_frame(self, master_frame):
		header_frame = tk.Frame(master=master_frame,height=200, relief=tk.RAISED, borderwidth=1, bg="gray")
		header_frame.pack(fill=tk.X, side=tk.TOP)
		return header_frame
	
	def create_body_frame(self, master_frame):
		body_frame = tk.Frame(master=master_frame, relief=tk.GROOVE, borderwidth=1, bg="blue")
		body_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
		return body_frame
	
	def create_sequence_list_frame(self, master_frame):
		sequence_list_frame = tk.Frame(master=master_frame, bg="yellow")
		sequence_list_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
		return sequence_list_frame

	def create_sequence_frame(self, master_frame):	
		sequence_frame = tk.Frame(master=master_frame, bg="pink")
		sequence_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
		return sequence_frame