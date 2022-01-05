import uuid
from random import random, randint

import pygame
import sys

pygame.init()

w_info = pygame.display.Info()

W = w_info.current_w - 100
H = w_info.current_h - 100

S = 10
SIZE = WIDTH, HEIGHT = W - (W % S), H - (H % S)
BORDER_WIDTH, CUBE_SIZE = 1, S
x, y, g = (WIDTH / 2) - ((WIDTH / 2) % S) - S, (HEIGHT / 2) - ((HEIGHT / 2) % S) - S, 0.1
print(x, y)

screen = pygame.display.set_mode(SIZE)

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (65, 66, 77)
LIGHT_GRAY = (124, 126, 148)
DARK_BLUE = (33, 37, 87)
COLORS = [GRAY, LIGHT_GRAY, DARK_BLUE]

list_of_cubes = []

font = pygame.font.SysFont(pygame.font.get_fonts()[0], 16)


def x_left_is_valid(_x: int):
    return True if _x > 0 else False


def x_right_is_valid(_x: int):
    return True if _x + 10 < WIDTH else False


def y_top_is_valid(_y: int):
    return True if _y > 0 else False


def y_bottom_is_valid(_y: int):
    return True if _y + 10 < WIDTH else False


def create_new_cube(_x: int, _y: int):
    for _ in range(10):
        _g = (-random() if randint(0, 1) else random())
        _g2 = (-random() if randint(0, 1) else random()) / 1.5
        list_of_cubes.append([_x, _y, COLORS[randint(0, len(COLORS) - 1)], _g, _g2, str(uuid.uuid4())])


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
            elif event.key == pygame.K_d:
                list_of_cubes = []
            elif event.key == 32:
                create_new_cube(x-S, y-S)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0] - (pos[0] % S)
            y = pos[1] - (pos[1] % S)

    # draw cubes
    for cube_config in list_of_cubes:
        cube = pygame.Surface((CUBE_SIZE, CUBE_SIZE))
        cube.fill(cube_config[2])
        cube_config[1] = cube_config[1] + cube_config[4]
        cube_config[0] = cube_config[0] + cube_config[3]
        screen.blit(cube, (cube_config[0], cube_config[1]))

        if cube_config[0] <= 0 or cube_config[0] + CUBE_SIZE >= WIDTH:
            cube_config[3] = -cube_config[3]
            cube_config[0] = cube_config[0] + cube_config[3]
        if cube_config[1] + CUBE_SIZE >= HEIGHT or cube_config[1] <= 0:
            cube_config[4] = -cube_config[4]
            cube_config[1] = cube_config[1] + cube_config[4]

    # draw horizontal line
    for i in range(HEIGHT // S):
        line_horizontal = pygame.Surface((WIDTH, BORDER_WIDTH))
        if y + S == int(S * i):
            line_horizontal.fill(GRAY)
            screen.blit(line_horizontal, (0, int(S * i)))
        elif y == int(S * i):
            line_horizontal.fill(GRAY)
            screen.blit(line_horizontal, (0, int(S * i)))

    # draw vertical line
    for i in range(WIDTH // S):
        line_vertical = pygame.Surface((BORDER_WIDTH, HEIGHT))
        if x + S == int(S * i):
            line_vertical.fill(GRAY)
            screen.blit(line_vertical, (int(S * i), 0))
        elif x == int(S * i):
            line_vertical.fill(GRAY)
            screen.blit(line_vertical, (int(S * i), 0))

    # draw circle
    CIRCLE_RAY = S * 5
    CIRCLE_X = x + (S / 2)
    CIRCLE_Y = y + (S / 2)
    circle = pygame.draw.circle(screen, GRAY, (CIRCLE_X, CIRCLE_Y), CIRCLE_RAY, BORDER_WIDTH)

    # draw rect between lines
    rect = pygame.Surface((S, S))
    rect.fill(GRAY)
    screen.blit(rect, (x, y))

    # draw text
    text = font.render("  " + str(len(list_of_cubes)) + "  ", True, BLACK, LIGHT_GRAY)
    screen.blit(text, (0, 0))

    pygame.display.update()
    screen.fill((0, 0, 0))
