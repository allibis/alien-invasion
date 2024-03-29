import sys
import pygame
import pygame.mixer

from logo import Logo
from time import sleep
from alien import Alien
from bullet import Bullet


def check_events(
	ai_set, screen, aliens, ship, stats,
	bullets, play_b, alien_img, laser_shot, sb
	):
	# watch for keyboard and mouse event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(
				event, ai_set, screen, ship, bullets, laser_shot, stats
			)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship, bullets)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(
				ai_set, screen,	aliens,	ship, stats, bullets,
				play_b,	mouse_x, mouse_y, alien_img, sb
			)


def check_keydown_events(
	event, ai_set, screen, ship, bullets, laser_shot, stats
):
	# check if the game is started
	if stats.game_active:
		""" move to the right or left"""
		if event.key == pygame.K_RIGHT:
			ship.move_right = True

		elif event.key == pygame.K_LEFT:
			ship.move_left = True

		elif event.key == pygame.K_SPACE:
			# if there are less than max_bullet
			fire_bullets(bullets, ai_set, screen, ship, laser_shot)

	if event.key == pygame.K_ESCAPE:
		sys.exit()


def check_keyup_events(event, ship, bullets):
	if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
		# stops
		ship.move_right = False
		ship.move_left = False


def check_play_button(
	ai_set, screen, aliens, ship, stats,
	bullets, play_b, mouse_x, mouse_y, alien_img, sb
):

	# check if the button is clicked and starts a new game
	buttonclicked = play_b.rect.collidepoint(mouse_x, mouse_y)

	if buttonclicked and not stats.game_active:
		# reset stats
		stats.reset_stats()
		stats.game_active = True

		#score init
		sb.prep_score()
		sb.prep_ship()

		# resets the screen
		aliens.empty()
		bullets.empty()

		# create a new fleet and center the ship
		create_fleet(ai_set, screen, aliens, ship, alien_img)
		ship.ship_center()


def ship_hit(ai_set, stats, screen, aliens, ship, bullets, alien_img, sb):

	# decrement the ships left
	stats.ship_left -= 1
	stats.score -= 50
	sb.prep_score()
	sb.prep_ship()

	if stats.ship_left > 0:
		# reset the game
		aliens.empty()
		bullets.empty()
		ship.ship_center()

		# create a new fleet
		create_fleet(ai_set, screen, aliens, ship, alien_img)

		# pause
		sleep(0.5)
	else:
		aliens.empty()
		bullets.empty()
		ai_set.reset()
		stats.game_active = False


def fire_bullets(bullets, ai_set, screen, ship, laser_shot):
	if len(bullets) < ai_set.max_bullet:
		# plays the sound effect
		pygame.mixer.Sound.play(laser_shot)

		# fire bullet
		newbullet = Bullet(ai_set, screen, ship)
		bullets.add(newbullet)


def check_bullet_alien_collision(
	ai_set, screen, aliens, ship, bullets,
	alien_exp, alien_img, stats, sb
):
	# check collision between bullets and aliens
	# and eventually delete them
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	# the two "True" arguments make both objects delete themselves
	if collisions:
		pygame.mixer.Sound.play(alien_exp)
		for aliens in collisions.values():
			#check to score all hits
			stats.score += ai_set.alien_points * len(aliens)
			sb.prep_score()
			check_highscore(stats, sb)


	if len(aliens) == 0:  # if there are no aliens left
		# destroy bullets and creates a new fleet
		bullets.empty()
		stats.score += 100
		sb.prep_score()
		check_highscore(stats, sb)
		ai_set.alien_speed += 0.1 # add speed when fleet is destroyed
		create_fleet(ai_set, screen, aliens, ship, alien_img)


def check_fleet_edges(ai_set, aliens, ship):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_dir(ai_set, aliens)
			break


def check_aliens_bottom(
	ai_set, stats, screen, ship, aliens, bullets, alien_img, sb
):

	# checks if any alien has reached the bottom of the screen
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# game over
			ship_hit(
				ai_set, stats, screen,
				aliens, ship, bullets, alien_img, sb
			)
			break
def check_highscore(stats, sb):
	if stats.score > stats.highscore:
		stats.highscore = stats.score
		sb.prep_high()




def get_num_rows(ai_set, ship_height, alien_height):
	# calculate the number of rows
	available_y = ai_set.height - 3 * alien_height - ship_height
	number_rows = int(available_y / (2 * alien_height))
	ai_set.max_bullet = number_rows
	return number_rows


def get_num_aliens_x(ai_set, alien_wid):
	# calculate the number of aliens in a row
	available_x = ai_set.width - 2 * alien_wid
	num_aliens_x = int(available_x / (2 * alien_wid))
	return num_aliens_x


def create_alien(ai_set, screen, aliens, alien_num, row, alien_img):
	alien = Alien(ai_set, screen, alien_img)
	alien_wid = alien.rect.width
	alien.x = alien_wid + 2 * alien_wid * alien_num

	alien.rect.y = 2 * alien.rect.height * row + 60 # so the aliens don't touch the ship
	alien.rect.x = alien.x
	aliens.add(alien)


def create_fleet(ai_set, screen, aliens, ship, alien_img):
	ai_set.fleet_dir = 1

	# create an alien and get his width
	alien = Alien(ai_set, screen, alien_img)

	# gets the number of rows and aliens
	num_aliens_x = get_num_aliens_x(ai_set, alien.rect.width)
	num_rows = get_num_rows(ai_set, ship.rect.height, alien.rect.height)

	# create the first row
	for row in range(num_rows):
		for alien_num in range(num_aliens_x):
			create_alien(ai_set, screen, aliens, alien_num, row, alien_img)


def change_fleet_dir(ai_set, aliens):
	# drops the fleet by 10 units and changes direction
	for alien in aliens.sprites():
		alien.rect.y += ai_set.fleet_drop

	# alien speed limit
	if ai_set.fleet_dir <= 4 and ai_set.fleet_dir >= -4:
		ai_set.fleet_dir *= -1.1
	else:
		ai_set.fleet_dir *= -1


def update_screen(
	ai_set, screen, ship, aliens,
	bullets, play_b, stats, logo, sb
	):

	# redraw the screen
	ship.blitme()
	aliens.draw(screen)


	# draw play button
	if stats.game_active:
		sb.show_score()
		pygame.mouse.set_visible(False)
	else:
		play_b.draw_button()
		logo.draw_logo()
		pygame.mouse.set_visible(True)

	pygame.display.flip()


def update_bullets(
	bullets, aliens, ai_set, screen, ship,
	alien_exp, alien_img, stats, sb
	):

	# updates each bullet
	bullets.update()

	# update bullets and delete them if they go off screen
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		if bullet.rect.y <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collision(
		ai_set, screen, aliens, ship, bullets,
		alien_exp, alien_img, stats, sb
		)


def update_aliens(ai_set, stats, screen, aliens, ship, bullets, alien_img, sb):
	# check if any alien hits the ship

	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_set, stats, screen, aliens, ship, bullets, alien_img, sb)

	# check if the fleet must change direction
	check_fleet_edges(ai_set, aliens, ship)

	# update the fleet
	aliens.update()

	# check if any alien reaches the bottom
	check_aliens_bottom(
		ai_set, stats, screen, ship,
		aliens, bullets, alien_img, sb
	)
