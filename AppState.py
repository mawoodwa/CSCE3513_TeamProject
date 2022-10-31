class AppState:
    S_SPLASH = 0
    S_EDITGAME = 1
    S_PLAYGAME = 2
    def __init__(self, state=None):
        self.state = self.S_SPLASH
	#removed some redundant code here
    
    def setState(self, state):
        if state >= self.S_SPLASH and state <= self.S_PLAYGAME:
            self.state = state
            return True
        else:
            return False
            
    def getState(self):
        return self.state