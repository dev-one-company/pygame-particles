import uuid
from random import random, randint

import pygame
import sys

pygame.init()

SIZE = WIDTH, HEIGHT = 500, 500
S = 10
BORDER_WIDTH, CUBE_WIDTH = 1, S
x, y, g = 0, 0, 0.1

screen = pygame.display.set_mode(SIZE)

YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
LIGHT_BLUE = (57, 122, 227)
PURPLE = (228, 45, 235)
COLORS = [GREEN, RED, YELLOW, LIGHT_BLUE, PURPLE]


list_of_cubes = []


def x_left_is_valid(_x: int):
    return True if _x > 0 else False


def x_right_is_valid(_x: int):
    return True if _x + 10 < WIDTH else False


def y_top_is_valid(_y: int):
    return True if _y > 0 else False


def y_bottom_is_valid(_y: int):
    return True if _y + 10 < WIDTH else False


def create_new_cube(_x: int, _y: int):
    for _ in range(5):
        _g = (-random() if randint(0, 1) else random()) / 4
        list_of_cubes.append([_x, _y, COLORS[randint(0, len(COLORS) - 1)], _g, str(uuid.uuid4())])


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if x_right_is_valid(x):
                    x += S
            elif event.key == pygame.K_LEFT:
                if x_left_is_valid(x):
                    x -= S
            elif event.key == pygame.K_DOWN:
                if y_bottom_is_valid(y):
                    y += S
            elif event.key == pygame.K_UP:
                if y_top_is_valid(y):
                    y -= S
            elif event.key == 32:
                create_new_cube(x-S, y-S)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0] - (pos[0] % S)
            y = pos[1] - (pos[1] % S)

    for cube_config in list_of_cubes:
        cube = pygame.Surface((CUBE_WIDTH, CUBE_WIDTH))
        cube.fill(cube_config[2])
        cube_config[1] = cube_config[1] + g
        cube_config[0] = cube_config[0] + cube_config[3]
        screen.blit(cube, (cube_config[0], cube_config[1]))

        if cube_config[0] <= 0:
            cube_config[3] = -cube_config[3]
            cube_config[0] = cube_config[0] + cube_config[3]
        if cube_config[0] >= WIDTH:
            cube_config[3] = -cube_config[3]
            cube_config[0] = cube_config[0] + cube_config[3]
        if cube_config[1] > HEIGHT:
            list_of_cubes.remove(cube_config)

    for i in range(HEIGHT // S):
        line_horizontal = pygame.Surface((WIDTH, BORDER_WIDTH))
        if y + S == int(S * i):
            line_horizontal.fill(GREEN)
            screen.blit(line_horizontal, (0, int(S * i)))
        elif y == int(S * i):
            line_horizontal.fill(GREEN)
            screen.blit(line_horizontal, (0, int(S * i)))

    for i in range(WIDTH // S):
        line_vertical = pygame.Surface((BORDER_WIDTH, HEIGHT))
        if x + S == int(S * i):
            line_vertical.fill(GREEN)
            screen.blit(line_vertical, (int(S * i), 0))
        elif x == int(S * i):
            line_vertical.fill(GREEN)
            screen.blit(line_vertical, (int(S * i), 0))

    CIRCLE_RAY = S * 5
    CIRCLE_X = x + (S / 2)
    CIRCLE_Y = y + (S / 2)
    circle = pygame.draw.circle(screen, GREEN, (CIRCLE_X, CIRCLE_Y), CIRCLE_RAY, BORDER_WIDTH)

    rect = pygame.Surface((S, S))
    rect.fill(GREEN)
    screen.blit(rect, (x, y))
    pygame.display.update()

    screen.fill((0, 0, 0))
