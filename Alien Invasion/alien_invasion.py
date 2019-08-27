import os
import sys
import pygame
import game_func as gf


from ship import Ship
from logo import Logo
from alien import Alien
from button import Button
from pygame.locals import *
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats





def run_game():
	#initialize game
	pygame.init()
	
	screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

	ship_img = pygame.image.load("resources/ship.bmp")
	alien_img = pygame.image.load("resources/alien.bmp")
	logo_img = pygame.image.load("resources/logo.png")
	icon = pygame.image.load("resources/icon.jpeg")
	backg = pygame.image.load("resources/background.png")

	
	
	

	pygame.display.set_icon(icon)
	
	#class istances
	ai_set = Settings(screen)
	ship = Ship(screen, ai_set, ship_img)
	stats = GameStats(ai_set)
	bullets = Group()
	aliens = Group()
	play_b = Button(ai_set, screen, "Play")
	logo = Logo(screen, logo_img)
	
	
	#functions
	pygame.display.set_caption("Alien Invasion")
	gf.create_fleet(ai_set, screen, aliens, ship, alien_img)
	
	#main loop
	while True:
		screen.blit(backg, (0,0))
		gf.check_events(ai_set, screen, aliens, ship, stats, bullets, 
				play_b, alien_img)
				
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, ai_set, screen, ship)
			gf.update_aliens(ai_set, stats, screen, aliens, ship, bullets)
			

		
		gf.update_screen(ai_set, screen, ship, aliens, bullets, play_b,
			stats, logo)

run_game()
