# # WRITE YOUR SOLUTION HERE:

# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
width = robot.get_width()
height = robot.get_height()

x = 0
y = 0
clock = pygame.time.Clock()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	
	window.fill((0, 0, 0))
	window.blit(robot, (x, y))
	pygame.display.flip()

	if (y == 0):
		if (x + width < 640):
			x += 1
	if (x + width == 640):
		if (y + height < 480):
			y += 1
	if (y + height == 480):
		if x > 0:
			x -= 1
	if (x == 0):
		if (y > 0):
			y -= 1
	
	clock.tick(60)
