# WRITE YOUR SOLUTION HERE:

import pygame
import math
from datetime import datetime

pygame.init()

display = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Drawing shapes")

# def circle(color: int, radius: int):
# 	pygame.draw.circle(display, color, (middle_x, middle_y), radius)

def hand(length: int, thickness: int, proportion: float):
	angle = 2*math.pi*proportion - math.pi/2
	end_x = middle_x + math.cos(angle) * length
	end_y = middle_y + math.sin(angle) * length

	pygame.draw.line(display, (0, 0, 255), (middle_x, middle_y), (end_x, end_y), thickness)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	hours = datetime.now().hour % 12
	minutes = datetime.now().minute
	seconds = datetime.now().second

	pygame.display.set_caption(str(datetime.now().time())[:8])

	display.fill((0, 0, 0))

	middle_x = 320
	middle_y = 240

	pygame.draw.circle(display, (255, 0, 0), (320, 240), 200, 5)
	pygame.draw.circle(display, (255, 0, 0), (320, 240), 10)

	hand(185, 1, seconds/60)
	hand(180, 2, (minutes + seconds / 60) / 60)
	hand(150, 5, (hours + minutes / 60 + seconds / 3600) / 12)

	pygame.display.flip()
