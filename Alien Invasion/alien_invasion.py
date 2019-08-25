import sys
import pygame
import game_func as gf

from ship import Ship
from alien import Alien
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats






def run_game():
	#initialize game
	pygame.init()
	ai_set = Settings()
	screen = pygame.display.set_mode((ai_set.width, ai_set.height))
	backg = pygame.image.load("resources/background.png")
	
	#class istances
	ai_set = Settings()
	ship = Ship(screen, ai_set)
	stats = GameStats(ai_set)
	bullets = Group()
	aliens = Group()
		
	#functions
	pygame.display.set_caption("Alien Invasion")
	gf.create_fleet(ai_set, screen, aliens, ship)
	
	#main loop
	while True:
		gf.check_events(ai_set, screen, ship, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, ai_set, screen, ship)
			gf.update_screen(ai_set, screen, ship, aliens, bullets, backg)
			gf.update_aliens(ai_set, stats, screen, aliens, ship, bullets)
		else:
			break
		
			


run_game()
