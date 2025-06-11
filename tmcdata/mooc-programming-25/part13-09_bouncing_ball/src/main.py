# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")
width = ball.get_width()
height = ball.get_height()

x = randint(0, 640 - width)
y = 0
velocity = 1
helocity = 1
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	
	window.fill((0, 0, 0))
	window.blit(ball, (x, y))

	pygame.display.flip()

	x += velocity
	y += helocity
	if velocity > 0 and (x + width >= 640):
		velocity = -velocity
	if velocity < 0 and (x <= 0):
		velocity = -velocity
	if helocity > 0 and (y + height >= 480):
		helocity = -helocity
	if helocity < 0 and (y <= 0):
		helocity = -helocity
	
	clock.tick(200)
