from sequencer.sequence import Sequence
from sequencer.player import Player

class Sequencer():
	def __init__(self):
		self.active_sequence = Sequence()
		self.sequence_list = [self.active_sequence]
		self.player = Player(self.active_sequence)

	def change_active_sequence(self, seq_pos):
		self.player.stop()
		self.player.active_sequence = self.sequence_list[seq_pos]

	def remove_sequence(self, seq_pos):
		del self.sequence_list[seq_pos]

	def add_sequence(self):
		self.sequence_list.append(Sequence())