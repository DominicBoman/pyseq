import tkinter as tk
from gui.view.root_view import Root_View
from gui.view.player_view import Player_View
from gui.view.sequence_view import Sequence_View
from gui.view.sequence_list_view import Sequence_List_View

class App_Window():

	def __init__(self, sequencer):
		self.open = True
		self.sequencer = sequencer
		self.player = self.sequencer.player
		#self.playerThread = Thread(tar)
		self.run()
		print('app window created')

	def run(self):
		window = tk.Tk()
		window.geometry('640x400')

		self.gui_setup(window)

		window.mainloop()

	def gui_setup(self, window):
		root_view = Root_View(window)
		player_view = Player_View(root_view.header_frame, self.player)
		sequence_list_view = Sequence_List_View(root_view.sequence_list_frame, self.sequencer.sequence_list, self.sequencer.active_sequence)
		sequence_view = Sequence_View(root_view.sequence_frame)

		#player_frame = tk.Frame()
		#label_a = tk.Label(master=player_frame, text="player")
		#label_a.config(bg= "gray51", fg= "white")
		#label_a.pack()
		#
		#sequence_list_frame = tk.Frame()
		#label_b = tk.Label(master=sequence_list_frame, text="sequence_list")
		#label_b.pack()
#
		#sequence_settings_frame = tk.Frame()
		#label_c = tk.Label(master=sequence_settings_frame, text="sequence_settings")
		#label_c.pack()
		#
		## Swap the order of `frame_a` and `frame_b`
		#player_frame.pack()
		#sequence_list_frame.pack()
		#sequence_settings_frame.pack()