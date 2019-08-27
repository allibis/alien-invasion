import pygame

class Logo():
	def __init__(self, screen, logo_img):
		#logo's properties
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.logo_img = logo_img
		self.logo_rect = self.logo_img.get_rect()
		self.logo_rect.centerx  = self.screen_rect.centerx
		self.logo_rect.y = -self.logo_rect.y
		
		#logo's rect
		self.rect = self.logo_img.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.y = self.rect.height/2
		
		
	def draw_logo(self):
		self.screen.blit(self.logo_img, self.rect)
