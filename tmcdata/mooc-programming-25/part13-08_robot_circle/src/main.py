# WRITE YOUR SOLUTION HERE:

import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

angle = 0
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	
	window.fill((0, 0, 0))
	
	for i in range (0, 10):
		# x = 320 + math.cos(angle + 0.63 * i) * 140 - (width / 2)
		# y = 240 + math.sin(angle + 0.63 * i) * 140 - (height / 2)
		x = 320 + math.cos(angle + 2 * math.pi * i/10) * 150 - width/2
		y = 240 + math.sin(angle + 2 * math.pi * i/10) * 150 - height/2
		window.blit(robot, (x, y))
	
	pygame.display.flip()

	angle += 0.01
	clock.tick(60)
