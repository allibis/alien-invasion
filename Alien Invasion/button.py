import pygame.font


class Button():
	def __init__(self, ai_set, screen, msg):
		#button attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#button properties
		self.width, self.height = 200, 70
		self.button_color = (0, 0, 0)
		
		self.rim_w, self.rim_h = 210, 80
		self.rim_color = (8, 146, 208)

		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont("dejavusansmono", 48)
		
		#button's rect
		self.centery = self.screen_rect.centery + 200
		
		self.rim = pygame.Rect(0, 0, self.rim_w, self.rim_h)
		self.rim.centerx = self.screen_rect.centerx
		self.rim.centery = self.centery
		
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.centery 
		
		
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		#render the message into a image
		self.msg_img = self.font.render(msg, True, self.text_color,
							self.button_color)
										
		self.msg_img_rect = self.msg_img.get_rect()
		self.msg_img_rect.center = self.rect.center
		
	def draw_button(self):
		#draw blank button, then the message
		self.screen.fill(self.rim_color, self.rim)
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_img, self.msg_img_rect)
