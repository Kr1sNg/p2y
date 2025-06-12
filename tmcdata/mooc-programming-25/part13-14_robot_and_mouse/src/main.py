# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

ms_x = 320 - robot.get_width()/2
ms_y = 240 - robot.get_height()/2

while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEMOTION:
			ms_x = event.pos[0] - robot.get_width()/2
			ms_y = event.pos[1] - robot.get_height()/2
			
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()


	
	window.fill((0, 0, 0))
	window.blit(robot, (ms_x, ms_y))
	pygame.display.flip()


