# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

rb_x = 320 - robot.get_width()/2
rb_y = 240 - robot.get_height()/2
ms_x = 0
ms_y = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			ms_x = event.pos[0]
			ms_y = event.pos[1]
			
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()

	if rb_x <= ms_x <= rb_x + robot.get_width():
		if rb_y <= ms_y <= rb_y + robot.get_height():
			rb_x = randint(0, 640 - robot.get_width())
			rb_y = randint(0, 240 - robot.get_height())

	
	window.fill((0, 0, 0))
	window.blit(robot, (rb_x, rb_y))
	pygame.display.flip()


