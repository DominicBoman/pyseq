import tkinter as tk

class Sequence_List_View():

	def __init__(self, master):
		self.frame = tk.Frame(master)
		self.frame.pack()
		self.controller = None
		self.refresh()

	def refresh(self, sequence_list=None, active_sequence=None):
		num = 1
		print('SEQUENCE LIST',sequence_list)

		if sequence_list:
			for child in self.frame.winfo_children():
				child.destroy()
			
			for i in range(len(sequence_list)):
				sequence_frame = tk.Frame(master=self.frame,height=40, relief=tk.RAISED, borderwidth=5, bg="white")
				sequence_frame.pack(fill=tk.X, side=tk.TOP)
				main_label = tk.Label(master=sequence_frame, text="sequence {}".format(num))
				main_label.bind("<Button-1>", lambda click_event, selected_sequence=sequence_list[i]: self.select_sequence(selected_sequence))
				main_label.pack()
	
				num = num + 1

		if not sequence_list or len(sequence_list) <= 10:
			add_button = tk.Button(master=self.frame, text ="ADD", command=self.add_sequence)
			add_button.pack()

	def add_sequence(self):
		if self.controller:
			self.controller.add_sequence()
		
	def select_sequence(self, selected_sequence):
		print(selected_sequence)
		if self.controller:
			self.controller.set_active_sequence(selected_sequence)