
class Sequence_List_Controller():

	def __init__(self, sequencer, sequence_list_view):
		self.sequencer = sequencer
		self.sequence_list_view = sequence_list_view
		self.active_sequence_controller = None

	def add_sequence(self):
		self.sequencer.add_sequence()
		self.sequence_list_view.refresh(self.sequencer.sequence_list, self.sequencer.player.active_sequence)

	def set_active_sequence(self, sequence):
		self.sequencer.change_active_sequence(sequence)
		print('active',self.sequencer.player.active_sequence)
		self.sequence_list_view.refresh(self.sequencer.sequence_list, self.sequencer.player.active_sequence)
		self.active_sequence_controller.set_active_sequence(self.sequencer.player.active_sequence)
		