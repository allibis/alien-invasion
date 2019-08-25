import pygame

class Settings():
	
	def __init__(self):
		#screen settings
		self.width = 800
		self.height = 600
		self.bg = (0,0,0)
		
		#ship settings
		self.ship_speed = 3
		self.ship_limit = 3
		
		#bullet settings
		self.bullet_speed = 4.5
		self.bullet_width = 3	# 3
		self.bullet_height = 15	# 15
		self.bullet_color = (255,255,0)
		self.max_bullet = 4
		
		#alien settings
		self.alien_speed = 1
		self.fleet_drop = 100 # drops by 10 pixels
		self.fleet_dir = 1 # '1' for right, '-1' for left
