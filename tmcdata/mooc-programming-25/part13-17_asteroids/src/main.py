# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Asterodit")

robot = pygame.image.load("robot.png")
x = 0
y = 480 - robot.get_height()

rock = pygame.image.load("rock.png")

number = 5
positions = []
for i in range(number):
	positions.append([randint(0, 640 - rock.get_width()), -randint(100, 1000)])

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
		if positions[i][1] + rock.get_height() > 480:
			exit()
		if positions[i][1] >= y:
			robot_middle = x + robot.get_width() / 2
			rock_middle = positions[i][0] + rock.get_width() / 2
			if abs(robot_middle - rock_middle) <= (robot.get_width() + rock.get_width()) / 2:
				positions[i][0] = randint(0, 640 - rock.get_width())
				positions[i][1] = -randint(100, 1000)
				point += 1

	window.fill((0, 0, 0))
	window.blit(robot, (x, y))
	for i in range(number):
		window.blit(rock, (positions[i][0], positions[i][1]))
	
	text = font.render("Points: " + str(point), True, (255, 0, 0))
	window.blit(text, (500, 10))

	pygame.display.flip()

	clock.tick(60)
