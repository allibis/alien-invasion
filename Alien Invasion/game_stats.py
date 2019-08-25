class GameStats():
	# tracks game statistics
	def __init__(self, ai_set):
		self.ai_set = ai_set
		self.reset_stats()
		self.game_active = True
		
		
	def reset_stats(self):
		self.ship_left = self.ai_set.ship_limit
