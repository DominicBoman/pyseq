import tkinter as tk
from config import SETTINGS
from gui.view.root_view import Root_View
from gui.view.player_view import Player_View
from gui.view.sequence_view import Sequence_View
from gui.view.sequence_list_view import Sequence_List_View
from gui.controller.player_controller import Player_Controller
from gui.controller.sequence_controller import Sequence_Controller
from gui.controller.sequence_list_controller import Sequence_List_Controller

class Sequencer_GUI():

	def __init__(self, sequencer):
		self.open = True
		self.sequencer = sequencer
		self.run()

	def run(self):
		gui = self.gui_setup()
		gui.mainloop()

	def gui_setup(self):
		gui = tk.Tk()
		gui.geometry('{}x{}'.format(SETTINGS['WIDTH'], SETTINGS['HEIGHT']))

		root_view = Root_View(gui)
		
		player_view = Player_View(root_view.header_frame)
		player_controller = Player_Controller(self.sequencer.player, player_view)
		player_view.controller = player_controller

		sequence_list_view = Sequence_List_View(root_view.sequence_list_frame)
		sequence_list_controller = Sequence_List_Controller(self.sequencer, sequence_list_view)
		sequence_list_view.controller = sequence_list_controller
		
		sequence_view = Sequence_View(root_view.sequence_frame)
		sequence_controller = Sequence_Controller(self.sequencer, sequence_view)
		sequence_view.controller = sequence_controller

		sequence_list_controller.active_sequence_controller = sequence_controller

		return gui