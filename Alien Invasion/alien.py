import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""single alien class""" 
	
	def __init__(self, ai_set, screen):
		super().__init__()
		self.screen = screen
		self.ai_set = ai_set
		
		# load the image
		self.image = pygame.image.load("resources/alien.bmp")
		self.rect = self.image.get_rect()
		
		# each new alien is positioned at the top-left position
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store the exact position 
		self.x = float(self.rect.x)
	
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		# make the alien move
		self.x += (self.ai_set.alien_speed * self.ai_set.fleet_dir)
		self.rect.x = self.x
		
		
	def check_edges(self):
		#checks if the alien touches the border of the screen
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= screen_rect.left:
			return True
			
	
	
	
