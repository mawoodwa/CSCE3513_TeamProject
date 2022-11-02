class EditGameState:
	PlayerSelect = 0
	PlayerName = 1
	AskUsePrevCode = 2
	CodeName = 3
	DeleteDB = 4
	PlayConfirm = 5

	def __init__(self, state):
		state = None
		self.state = state
		if state == None:
			self.state = self.PlayerSelect

	def getState(self):
		return self.state
	
	def setState(self, state):
		if state >= self.PlayerSelect and state <= self.PlayConfirm:
			self.state = state
			return True
		if state < self.PlayerSelect or state > self.PlayConfirm:
			self.state = state
			return False