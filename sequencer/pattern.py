class Pattern():

	def __init__(self, lenght=16):
		self.steps = []
		self.set_lenght(lenght)
		print(self.steps)
		
	def set_lenght(self, lenght):
		for n in range(lenght):
			self.steps.append(False)

	def get_length(self):
		return len(self.steps)

	def step_enabled(self, step_pos):
		return self.steps[step_pos]

	def change_step(self, step_pos):
		self.steps[step_pos] = not self.steps[step_pos]