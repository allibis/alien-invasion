""" pyinstaller-friendly module """

import os
import sys
import pygame
import game_func as gf
import resource_path as rp


from ship import Ship
from logo import Logo
from alien import Alien
from button import Button
from pygame.locals import *
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():

	# initialize game
	pygame.mixer.pre_init(22050, -16, 2, 64)
	pygame.mixer.init()
	pygame.init()

	screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	screen_rect = screen.get_rect()


	# images import
	ship_img = pygame.image.load(rp.path("resources/ship.bmp"))
	alien_img = pygame.image.load(rp.path("resources/alien.bmp"))
	logo_img = pygame.image.load(rp.path("resources/logo.png"))
	icon = pygame.image.load(rp.path("resources/icon.jpeg"))
	back_img = pygame.image.load(rp.path("resources/background.png"))
	backg = pygame.transform.scale(back_img, (screen_rect.width,
											screen_rect.height))

	# soundtrack
	pygame.mixer.music.load(rp.path("resources/Starlight.ogg"))
	pygame.mixer.music.play(loops=-1)  # -1 = loop


	#sound effects
	laser_shot = pygame.mixer.Sound(rp.path("resources/laser-shoot.ogg"))
	alien_exp = pygame.mixer.Sound(rp.path("resources/alien-explosion-1.ogg"))

	pygame.display.set_icon(icon)

	# class istances
	aliens = Group()
	bullets = Group()
	ai_set = Settings(screen)
	stats = GameStats(ai_set)
	logo = Logo(screen, logo_img)
	sb = Scoreboard(screen, stats, ship_img, ai_set)
	ship = Ship(screen, ai_set, ship_img)
	play_b = Button(ai_set, screen, "Play")



	# functions
	pygame.display.set_caption("Alien Invasion")
	gf.create_fleet(ai_set, screen, aliens, ship, alien_img)

	# main loop
	while True:
		screen.blit(backg, (0, 0))
		gf.check_events(ai_set, screen, aliens, ship, stats,
						bullets, play_b, alien_img, laser_shot, sb)

		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, ai_set, screen,
							ship, alien_exp, alien_img, stats, sb)


			gf.update_aliens(ai_set, stats, screen,
							 aliens, ship, bullets, alien_img, sb)

		gf.update_screen(ai_set, screen, ship, aliens,
						 bullets, play_b, stats, logo, sb)

	pygame.quit()


run_game()
pygame.quit()
