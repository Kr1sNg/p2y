# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
window.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()

for j in range(0, 10):
	for i in range (0, 10):
		window.blit(robot, (j * 10 + 50 + i * 40, 100 + j * 20))

pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()