# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
width = robot.get_width()
height = robot.get_height()

x = 0
a = 0

velocity = 1
motorcity = 2
clock = pygame.time.Clock()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	
	window.fill((0, 0, 0))
	window.blit(robot, (x, 50))
	window.blit(robot, (a, 240 - height))
	pygame.display.flip()

	x += velocity
	if velocity > 0 and (x + width >= 640):
		velocity = - velocity
	if velocity < 0 and x <= 0:
		velocity = - velocity

	a += motorcity
	if motorcity > 0 and (a + width >= 640):
		motorcity = - motorcity
	if motorcity < 0 and a <= 0:
		motorcity = - motorcity
	
	clock.tick(60)
