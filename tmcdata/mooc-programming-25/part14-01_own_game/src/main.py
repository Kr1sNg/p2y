# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((640, 480))

pygame.display.set_caption("A rain of coins")

robot = pygame.image.load("robot.png")
x = 0
y = 480 - robot.get_height()

coin = pygame.image.load("coin.png")
monster = pygame.image.load("monster.png")

number = 5
positions = []
positions_m = []
for i in range(number):
	positions.append([randint(0, 640 - coin.get_width()), -randint(100, 1000)])
	positions_m.append([randint(0, 640 - monster.get_width()), -randint(100, 1000)])

to_right = False
to_left = False

point = 0
font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				to_left = True
			if event.key == pygame.K_RIGHT:
				to_right = True
			if event.key == pygame.K_ESCAPE:
				exit()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				to_left = False
			if event.key == pygame.K_RIGHT:
				to_right = False
	
	if to_right:
		x += 2
	if to_left:
		x -= 2

	for i in range(number):
		positions[i][1] += 1
		positions_m[i][1] += 1
		robot_middle = x + robot.get_width() / 2
		if positions[i][1] >= y:
			coin_middle = positions[i][0] + coin.get_width() / 2
			if abs(robot_middle - coin_middle) <= (robot.get_width() + coin.get_width()) / 2:
				positions[i][0] = randint(0, 640 - coin.get_width())
				positions[i][1] = -randint(100, 1000)
				point += 1
		if positions_m[i][1] >= y:
			monster_middle = positions[i][0] + monster.get_width() / 2
			if abs(robot_middle - monster_middle) <= (robot.get_width() + monster.get_width()) / 2:
				exit()


	window.fill((255, 255, 255))
	window.blit(robot, (x, y))
	for i in range(number):
		window.blit(coin, (positions[i][0], positions[i][1]))
		window.blit(monster, (positions_m[i][0], positions_m[i][1]))
	
	text = font.render("Points: " + str(point), True, (255, 0, 0))
	window.blit(text, (500, 10))

	pygame.display.flip()

	clock.tick(60)
