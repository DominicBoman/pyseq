from util.audio_loader import *
from config import SAMPLE_PATH

class Sample():
	
	def __init__(self, src_path=SAMPLE_PATH['TEST']):
		self.audio_path = src_path
		self.audio = load_audio(src_path)
		self.name = 'TEST'

	def set_audio(self, src_path):
		self.audio = load_audio(src_path)

	def play(self):
		if self.audio:
			self.audio.play()
		
