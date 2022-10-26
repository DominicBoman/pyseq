from sequencer.sequence import Sequence
from sequencer.player import Player

class Sequencer():
	def __init__(self):
		self.sequence_list = []
		self.player = Player()

	def change_active_sequence(self, sequence):
		self.player.stop()
		self.player.reset() ## TODO: REMOVE WHEN GLOBAL PATTERN SIZE ADDED
		self.player.active_sequence = sequence

	def remove_sequence(self, seq_pos):
		del self.sequence_list[seq_pos]

	def add_sequence(self):
		self.sequence_list.append(Sequence())

	def get_active_sequence(self):
		return self.player.active_sequence