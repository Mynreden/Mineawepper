import pygame
from const import *
import random

class Cube:
    def __init__(self, position: tuple, number: int, square_size: int, upper_border: int = 0):
        self.position = position # (y, x)
        self.number = number
        self.is_flagged = False
        self.is_open = False
        self.image = scale(spr_grid, (square_size, square_size))
        self.rect = pygame.Rect(position[1] * square_size, position[0] * square_size - upper_border, square_size, square_size)

    def draw(self, display: pygame.Surface):
        display.blit(self.image, self.rect)


class Board:
    def __init__(self, width: int, height: int, n_bombs: int, square_size: int):
        self.boolean_map = [[False for _ in range(width + 2)] for __ in range(height + 2)]
        self.height = height
        self.width = width
        self.n_bombs = n_bombs
        self.square_size = square_size
        self.upper_border = height * square_size - screen_height
        self.squares_left = width *height - n_bombs
        self.map = []
        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(Cube((i, j), 0, square_size, self.upper_border))
            self.map.append(line)

    def generate(self, position: tuple):
        n_bombs = self.n_bombs
        first_click = []
        for n in range(max(0, position[0] - 1), min(position[0] + 2, self.height)):
            for m in range(max(0, position[1] - 1), min(position[1] + 2, self.width)):
                first_click.append((n, m))
        while n_bombs:
            mine = (random.randint(1, self.height - 1), random.randint(1, self.width - 1))
            if not self.boolean_map[mine[0]][mine[1]] and (mine[0] - 1, mine[1] - 1) not in first_click:
                self.boolean_map[mine[0]][mine[1]] = True
                n_bombs -= 1
        self.map = []
        for i in range(self.height):
            line = []
            for j in range(self.width):

                if self.boolean_map[i + 1][j + 1]:
                    line.append(Cube((i, j), -1, self.square_size, self.upper_border))
                    continue
                mines = 0
                for n in range(i, i + 3):
                    for m in range(j, j + 3):
                        if self.boolean_map[n][m]:
                            mines += 1
                line.append(Cube((i, j), mines, self.square_size, self.upper_border))
            self.map.append(line)

    def open(self, cube: Cube):
        if cube.is_flagged:
            return
        if not cube.is_open:
            self.squares_left -= 1
            self.__open_closed_cube(cube)
        else:
            self.__open_around(cube)

    def __open_closed_cube(self, cube: Cube):
        i, j = cube.position
        self.map[i][j].is_open = True
        self.map[i][j].image = scale(images[self.map[i][j].number], (self.square_size,) * 2)
        if self.map[i][j].number == 0:
            for n in range(max(0, i - 1), min(i + 2, self.height)):
                for m in range(max(0, j - 1), min(j + 2, self.width)):
                    if not self.map[n][m].is_open:
                        self.open(self.map[n][m])

    def __open_around(self, cube: Cube):
        i, j = cube.position
        flags = 0
        for n in range(max(0, i - 1), min(i + 2, self.height)):
            for m in range(max(0, j - 1), min(j + 2, self.width)):
                if self.map[n][m].is_flagged:
                    flags += 1
        if flags == cube.number:
            for n in range(max(0, i - 1), min(i + 2, self.height)):
                for m in range(max(0, j - 1), min(j + 2, self.width)):
                    if not self.map[n][m].is_flagged and not self.map[n][m].is_open:
                        self.open(self.map[n][m])

    def flag(self, cube: Cube) -> bool:
        if cube.is_open:
            return
        i, j = cube.position
        if not cube.is_flagged:

            self.map[i][j].is_flagged = True
            self.map[i][j].image = scale(spr_flag, (self.square_size,) * 2)
            return True
        else:
            i, j = cube.position
            self.map[i][j].is_flagged = False
            self.map[i][j].image = scale(spr_grid, (self.square_size,) * 2)
            return False

    def draw(self, display: pygame.Surface):
        for i in self.map:
            for j in i:
                j.draw(display)
