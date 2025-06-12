# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
r_width = robot.get_width()
r_height = robot.get_height()

positions = [[0, 0], [r_width, r_height]]

controls = []

controls.append((pygame.K_LEFT, 0, -2, 0))
controls.append((pygame.K_RIGHT, 0, 2, 0))
controls.append((pygame.K_UP, 0, 0, -2))
controls.append((pygame.K_DOWN, 0, 0, 2))
controls.append((pygame.K_a, 1, -2, 0))
controls.append((pygame.K_d, 1, 2, 0))
controls.append((pygame.K_w, 1, 0, -2))
controls.append((pygame.K_s, 1, 0, 2))

clock = pygame.time.Clock()

key_pressed = {}

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			key_pressed[event.key] = True
		if event.type == pygame.KEYUP:
			del key_pressed[event.key]
		if event.type == pygame.QUIT:
			exit()
	for key in controls:
		if key[0] in key_pressed:
			positions[key[1]][0] += key[2]
			positions[key[1]][1] += key[3]

	screen.fill((0, 0, 0))
	for i in range(2):
		screen.blit(robot, (positions[i][0], positions[i][1]))
	pygame.display.flip()

	clock.tick(60)


# import pygame

# pygame.init()
# window = pygame.display.set_mode((640, 480))

# r = pygame.image.load("robot.png")
# ra = pygame.image.load("robot.png")


# x = 0
# y = 480 - r.get_height()

# x_a = 0
# y_a = 0

# to_right = False
# to_left = False
# to_up = False
# to_down = False

# to_right_a = False
# to_left_a = False
# to_up_a = False
# to_down_a = False

# clock = pygame.time.Clock()

# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			exit()
		
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_LEFT:
# 				to_left = True
# 			if event.key == pygame.K_RIGHT:
# 				to_right = True
# 			if event.key == pygame.K_UP:
# 				to_up = True
# 			if event.key == pygame.K_DOWN:
# 				to_down = True
# 			if event.key == pygame.K_a:
# 				to_left_a = True
# 			if event.key == pygame.K_d:
# 				to_right_a = True
# 			if event.key == pygame.K_w:
# 				to_up_a = True
# 			if event.key == pygame.K_s:
# 				to_down_a = True
# 			if event.key == pygame.K_ESCAPE:
# 				exit()
		
# 		if event.type == pygame.KEYUP:
# 			if event.key == pygame.K_LEFT:
# 				to_left = False
# 			if event.key == pygame.K_RIGHT:
# 				to_right = False
# 			if event.key == pygame.K_UP:
# 				to_up = False
# 			if event.key == pygame.K_DOWN:
# 				to_down = False
# 			if event.key == pygame.K_a:
# 				to_left_a = False
# 			if event.key == pygame.K_d:
# 				to_right_a = False
# 			if event.key == pygame.K_w:
# 				to_up_a = False
# 			if event.key == pygame.K_s:
# 				to_down_a = False
	
# 	if to_right:
# 		x += 2
# 	if to_left:
# 		x -= 2
# 	if to_up:
# 		y -= 2
# 	if to_down:
# 		y += 2
	
# 	if to_right_a:
# 		x_a += 2
# 	if to_left_a:
# 		x_a -= 2
# 	if to_up_a:
# 		y_a -= 2
# 	if to_down_a:
# 		y_a += 2

# 	window.fill((0, 0, 0))
# 	window.blit(r, (x, y))
# 	window.blit(ra, (x_a, y_a))
# 	pygame.display.flip()

# 	clock.tick(60)

