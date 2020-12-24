import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLOR_MIN_VALUE = 0
COLOR_MAX_VALUE = 255
MASSIVE_VALUE = 9999999999999999999999999999999999999999999999999
LEFT = 1
RIGHT = 3

gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
list_of_positions = []
random.seed()


def recolor():
    pixelarray = pygame.PixelArray(gameDisplay)

    if len(list_of_positions) > 0:
        for i in range(0, SCREEN_WIDTH):
            for j in range(0, SCREEN_HEIGHT):
                min_distance = MASSIVE_VALUE
                index = 0
                for k in range (0,len(list_of_positions)):
                    temp_x, temp_y, temp_color = list_of_positions[k]
                    if min_distance > ((temp_x - i) * (temp_x - i) + (temp_y - j) * (temp_y - j)):
                        min_distance = ((temp_x - i) * (temp_x - i) + (temp_y - j) * (temp_y - j))
                        index = k

                temp_x, temp_y, temp_color = list_of_positions[index]
                pixelarray[i][j] = temp_color



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x, y = event.pos
            color = (random.randint(COLOR_MIN_VALUE, COLOR_MAX_VALUE), random.randint(COLOR_MIN_VALUE, COLOR_MAX_VALUE), random.randint(COLOR_MIN_VALUE, COLOR_MAX_VALUE))
            list_of_positions.append((x, y, color))
            recolor()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            if len(list_of_positions) > 0:
                list_of_positions.pop()
                recolor()

    pygame.display.update()