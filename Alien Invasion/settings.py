import pygame

class Settings():

	def __init__(self, screen):
		#screen settings
		self.screen = screen

		self.screen_rect = screen.get_rect()
		self.width = self.screen_rect.width
		self.height = self.screen_rect.height

		self.bg = (0,0,0)

		#ship settings
		self.ship_speed = 6
		self.ship_limit = 3

		#bullet settings
		self.bullet_speed = 4.5
		self.bullet_width = 4
		self.bullet_height = 20
		self.bullet_color = (255,255,0)
		self.max_bullet = 0

		#alien settings
		self.alien_speed = 2
		self.fleet_drop = 10 # drops by 10 pixels
		self.fleet_dir = 1 # '1' for right, '-1' for left
		self.alien_points = 10

	def reset(self):
		#resets values
		self.alien_speed = 2
		self.fleet_dir = 1 # '1' for right, '-1' for left
