
class Sequence_Controller():

	def __init__(self, sequencer, sequence_view):
		self.sequence_view = sequence_view
		self.sequencer = sequencer

	def set_active_sequence(self, active_sequence):
		self.sequence_view.refresh_pattern(active_sequence.pattern.steps)

	def set_step(self, step_pos):
		active_sequence = self.sequencer.get_active_sequence()
		active_sequence.pattern.change_step(step_pos)
		print(active_sequence.pattern.steps)
		self.sequence_view.refresh_pattern(active_sequence.pattern.steps)
		
		