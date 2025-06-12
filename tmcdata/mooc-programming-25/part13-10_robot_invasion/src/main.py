# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

number = 20

robots = []
for i in range(number):
	robots.append([-1000, 480])

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	
	window.fill((0, 0, 0))
	
	for i in range(number):
		if robots[i][1] + height < 480:
			robots[i][1] += 1
		else:
			if robots[i][0] < -width or robots[i][0] > 640:
				robots[i][0] = randint(0, 640 - width)
				robots[i][1] = randint(-1000, -100)
			elif robots[i][0] + width/2 < 320:
				robots[i][0] -= 1
			else:
				robots[i][0] += 1

	for i in range(number):
		window.blit(robot, (robots[i][0], robots[i][1]))

	pygame.display.flip()

	clock.tick(60)
