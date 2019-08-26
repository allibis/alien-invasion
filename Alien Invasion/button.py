import pygame.font


class Button():
	def __init__(self, ai_set, screen, msg):
		#button attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#button properties
		self.width, self.height = 200, 70
		self.button_color = (50, 0, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont("dejavusansmono", 48)
		
		#button's rect
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		#render the message into a image
		self.msg_img = self.font.render(msg, True, self.text_color,
							self.button_color)
										
		self.msg_img_rect = self.msg_img.get_rect()
		self.msg_img_rect.center = self.rect.center
		
	def draw_button(self):
		#draw blank button, then the message
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_img, self.msg_img_rect)
