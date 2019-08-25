import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	def __init__(self, ai_set, screen, ship):
		
		# create a bullet object
		super().__init__()
		self.screen = screen
		
		# create a bullet rect at (0,0) and the correct the position
		self.rect = pygame.Rect(0, 0, ai_set.bullet_width, 
			ai_set.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#store the position as a decimal value
		self.y = float(self.rect.y)
		
		self.color = ai_set.bullet_color
		self.speed = ai_set.bullet_speed
		
	
	def update(self):
		#changes the position value, then  updates it
		self.y -= self.speed
		
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
