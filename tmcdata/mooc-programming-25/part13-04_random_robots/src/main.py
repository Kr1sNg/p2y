# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))

for i in range(0, 1000):
	window.blit(robot, (randint(5, 640 - 5 - width), randint(5, 480 - 5 - height)))

pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
