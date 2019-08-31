import pygame
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	def __init__(self, screen, stats, ship_img, ai_set):
		#score visualization
		self.screen_rect = screen.get_rect()
		self.screen = screen
		self.stats = stats
		self.ship_img = ship_img
		self.ai_set = ai_set


		# text settings
		self.text_color = (223, 194, 194)
		self.font = pygame.font.SysFont("dejavusansmono", 30)

		#renders the score box
		self.prep_score()
		self.prep_high()
		self.prep_ship()

	def prep_score(self):
		#renders the score box

		#round the score e.g.  10000 -> 10,000
		round_score = round(self.stats.score, -1)
		score_str = str("Score: " + str("{:,}".format(round_score)))
		self.score_img = self.font.render(score_str, True,
					  					self.text_color, None)

		#creates the score rectangle
		self.score_rect = self.score_img.get_rect()
		self.score_rect.left = self.screen_rect.left + 5 # show the full score
		self.score_rect.top = self.screen_rect.top

	def prep_high(self):
		#highscore render
		round_high = round(self.stats.highscore, -1)
		high_str = "{:,}".format(round_high)
		self.high_img = self.font.render(high_str, True, self.text_color)

		#highscore box
		self.high_rect = self.high_img.get_rect()
		self.high_rect.centerx = self.screen_rect.centerx
		self.high_rect.top = self.screen_rect.top



	def prep_ship(self):
		self.ships = Group()
		for ship_num in range(self.stats.ship_left):
			ship = Ship(self.screen, self.ai_set, self.ship_img)
			ship.rect.x = self.screen_rect.width-(ship_num+1)*ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def show_score(self):
		#draws the score
		self.ships.draw(self.screen)
		self.screen.blit(self.high_img, self.high_rect)
		self.screen.blit(self.score_img, self.score_rect)
