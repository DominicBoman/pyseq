BPM_DEFAULT = 90
MINUTE = 60

class Clock():
	def __init__(self, bpm=BPM_DEFAULT):
		self.set_bpm(bpm)

	def set_bpm(self, bpm):
		self.bpm = bpm
		self.step_interval = (MINUTE / self.bpm)