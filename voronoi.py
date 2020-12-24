import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLOR_MIN_VALUE = 0
COLOR_MAX_VALUE = 255

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
list_of_positions = []
random.seed()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            color = (random.randint(COLOR_MIN_VALUE, COLOR_MAX_VALUE), random.randint(COLOR_MIN_VALUE, COLOR_MAX_VALUE), random.randint(COLOR_MIN_VALUE, COLOR_MAX_VALUE))
            list_of_positions.append((x, y, color))

    pygame.display.update()