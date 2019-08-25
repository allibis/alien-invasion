import pygame


class Ship():
	def __init__(self, screen, ai_set):
		self.screen = screen
		
		#movement flags
		self.move_right = False
		self.move_left = False
		
		
		#load the image and the rect
		self.image = pygame.image.load("resources/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#start new ship at the bottom center
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#position and speed
		self.center = float(self.rect.centerx)
		self.speed = ai_set.ship_speed
		
		
	def blitme(self):
		#draw the ship
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		# ship can move only in the screen boundaries
		
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.center += self.speed
		elif self.move_left and self.rect.left > 0:	
			self.center -= self.speed
			
		#updates center
		self.rect.centerx = self.center
		
	def ship_center(self):
		self.center = self.screen_rect.centerx
