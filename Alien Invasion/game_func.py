import sys
import pygame

from time import sleep
from alien import Alien
from bullet import Bullet



def check_events(ai_set, screen, ship, bullets):
	#watch for keyboard and mouse event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
					
		elif event.type == pygame.KEYDOWN:	
			check_keydown_events(event, ai_set, screen, ship, bullets)
			
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		
			
			
			
def check_keydown_events(event, ai_set, screen, ship, bullets):
	""" move to the right or left"""
	if event.key == pygame.K_RIGHT:
		ship.move_right = True
		
	elif event.key == pygame.K_LEFT:
		ship.move_left = True
		
	elif event.key == pygame.K_SPACE:
		fire_bullets(bullets, ai_set, screen, ship)
		
	elif event.key == pygame.K_ESCAPE:
		sys.exit()
			
				
				
def check_keyup_events(event, ship):		
	if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
		#stops
		ship.move_right = False
		ship.move_left = False
		
		
def ship_hit(ai_set, stats, screen, aliens, ship, bullets):
	
	#decrement the ships left
	stats.ship_left -= 1
	
	if stats.ship_left > 0:
		#reset the game
		aliens.empty()
		bullets.empty()
		ship.ship_center()
		
		#create a new fleet
		create_fleet(ai_set, screen, aliens, ship)
		
		#pause
		sleep(0.5)
	else:
		stats.game_active = False
	

	
def fire_bullets(bullets, ai_set, screen, ship):
	# if there are less than 3 bullets
	if len(bullets) < ai_set.max_bullet:
		newbullet = Bullet(ai_set, screen, ship)
		bullets.add(newbullet)	


	
	
	
def check_bullet_alien_collision(ai_set, screen, aliens, ship, bullets):
	#check collision between bullets and aliens
	#and eventually delete them
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	#the two "True" arguments make both objects delete themselves


	if len(aliens) == 0: #if there are no aliens left
		#destroy bullets and creates a new fleet 
		bullets.empty()
		create_fleet(ai_set, screen, aliens, ship)
		
	
	
	


def get_num_rows(ai_set, ship_height, alien_height):
	#calculate the number of rows
	available_y = ai_set.height - 3*alien_height - ship_height
	number_rows = int(available_y / (2*alien_height))
	return number_rows



def get_num_aliens_x(ai_set, alien_wid):
	#calculate the number of aliens in a row
	available_x = ai_set.width - 2 * alien_wid
	num_aliens_x = int(available_x / (2*alien_wid))
	return num_aliens_x
	
	
def create_alien(ai_set, screen, aliens, alien_num, row):
	alien = Alien(ai_set, screen)
	alien_wid = alien.rect.width
	alien.x = alien_wid + 2 * alien_wid * alien_num
	
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
	alien.rect.x = alien.x
	aliens.add(alien)




def create_fleet(ai_set, screen, aliens, ship):
	ai_set.fleet_dir = 1
	
	#create an alien and get his width
	alien = Alien(ai_set, screen)
	
	#gets the number of rows and aliens
	num_aliens_x = get_num_aliens_x(ai_set, alien.rect.width)
	num_rows = get_num_rows(ai_set, ship.rect.height, alien.rect.height)
	
	
	# create the first row
	for row in range(num_rows):
		for alien_num in range(num_aliens_x):
			create_alien(ai_set, screen, aliens, alien_num, row)


def check_fleet_edges(ai_set, aliens, ship):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_dir(ai_set, aliens)
			break
			
			
def change_fleet_dir(ai_set, aliens):
	#drops the fleet by 10 units and changes direction
	for alien in aliens.sprites():
		alien.rect.y += ai_set.fleet_drop
	ai_set.fleet_dir *= -1.1

	
	
	
def update_screen(ai_set, screen, ship, aliens, bullets, background):
	#redraw the screen
	pygame.display.flip()
	screen.fill(ai_set.bg)
	screen.blit(background, (0,0))
	ship.blitme()
	aliens.draw(screen)
	
	
def update_bullets(bullets, aliens, ai_set, screen, ship):
	#updates each bullet
	bullets.update()
	
	# update bullets and delete them if they go off screen
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		if bullet.rect.y <=0:
			bullets.remove(bullet)
			
	check_bullet_alien_collision(ai_set, screen, aliens, ship, bullets)
	
	
def update_aliens(ai_set, stats, screen, aliens, ship, bullets):
	#check if the fleet must change direction
	check_fleet_edges(ai_set, aliens, ship)
	

	#update the fleet
	aliens.update()
	
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_set, stats, screen, aliens, ship, bullets)
