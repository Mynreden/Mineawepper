import pygame
import random
import sys
from const import square_size

# Import files

WIDTH = 10
HEIGHT = 10
spr_emptyGrid = pygame.image.load("static_files/empty.png")
spr_flag = pygame.image.load("static_files/flag.png")
spr_grid = pygame.image.load("static_files/Grid.png")
spr_grid1 = pygame.image.load("static_files/grid1.png")
spr_grid2 = pygame.image.load("static_files/grid2.png")
spr_grid3 = pygame.image.load("static_files/grid3.png")
spr_grid4 = pygame.image.load("static_files/grid4.png")
spr_grid5 = pygame.image.load("static_files/grid5.png")
spr_grid6 = pygame.image.load("static_files/grid6.png")
spr_grid7 = pygame.image.load("static_files/grid7.png")
spr_grid8 = pygame.image.load("static_files/grid8.png")
spr_mine = pygame.image.load("static_files/mine.png")
spr_mineClicked = pygame.image.load("static_files/mineClicked.png")
spr_mineFalse = pygame.image.load("static_files/mineFalse.png")
images = [spr_emptyGrid,
          spr_grid1,
          spr_grid2,
          spr_grid3,
          spr_grid4,
          spr_grid5,
          spr_grid6,
          spr_grid7,
          spr_grid8,
          spr_mine]

screen = pygame.display.set_mode((WIDTH * square_size, HEIGHT * square_size))


class Cube:
    def __init__(self, position: tuple, number: int):
        self.position = position
        self.number = number
        self.is_flagged = False
        self.is_open = False
        self.image = spr_grid
        self.rect = pygame.Rect(position[0] * square_size, position[1] * square_size, square_size, square_size)

    def draw(self, display: pygame.Surface):
        display.blit(self.image, self.rect)


class Board:
    def __init__(self, width: int, height: int, n_bombs: int):
        self.boolean_map = [[False for _ in range(width + 2)] for __ in range(height + 2)]
        self.height = height
        self.width = width
        self.n_bombs = n_bombs
        self.map = []
        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(Cube((i, j), 0))
            self.map.append(line)

    def generate(self, position: tuple):
        n_bombs = self.n_bombs
        first_click = []
        print(position)
        for n in range(max(0, position[0] - 1), min(position[0] + 2, self.width)):
            for m in range(max(0, position[1] - 1), min(position[1] + 2, self.height)):
                first_click.append((n, m))
        print(len(first_click))
        print(first_click)
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
                    line.append(Cube((i, j), -1))
                    continue

                mines = 0
                for n in range(i, i + 3):
                    for m in range(j, j + 3):
                        if self.boolean_map[n][m]:
                            mines += 1

                line.append(Cube((i, j), mines))
            self.map.append(line)

    def open(self, cube: Cube):
        print(cube.position)
        if cube.is_flagged:
            return
        if not cube.is_open:
            self.__open_closed_cube(cube)
        else:
            self.__open_around(cube)

    def __open_closed_cube(self, cube: Cube):
        i, j = cube.position
        self.map[i][j].is_open = True
        self.map[i][j].image = images[self.map[i][j].number]

        if self.map[i][j].number == 0:
            for n in range(max(0, i - 1), min(i + 2, self.width)):
                for m in range(max(0, j - 1), min(j + 2, self.height)):
                    if not self.map[n][m].is_open:
                        self.open(self.map[n][m])

    def __open_around(self, cube: Cube):
        i, j = cube.position
        flags = 0
        for n in range(max(0, i - 1), min(i + 2, self.width)):
            for m in range(max(0, j - 1), min(j + 2, self.height)):
                if self.map[n][m].is_flagged:
                    flags += 1
        if flags == cube.number:
            for n in range(max(0, i - 1), min(i + 2, self.width)):
                for m in range(max(0, j - 1), min(j + 2, self.height)):
                    if not self.map[n][m].is_flagged and not self.map[n][m].is_open:
                        self.open(self.map[n][m])

    def flag(self, cube: Cube):
        if cube.is_open:
            return
        if not cube.is_flagged:
            i, j = cube.position
            self.map[i][j].is_flagged = True
            self.map[i][j].image = spr_flag
        else:
            i, j = cube.position
            self.map[i][j].is_flagged = False
            self.map[i][j].image = spr_grid

    def draw(self, display: pygame.Surface):
        for i in self.map:
            for j in i:
                j.draw(display)


def output_matrix(board: Board):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(int(board.boolean_map[i + 1][j + 1]), end=' ')
        print()


def main():
    pygame.init()
    timer = pygame.time.Clock()
    board = Board(WIDTH, HEIGHT, 10)
    output_matrix(board)

    first_click = True
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in board.map:
                    for j in i:
                        if j.rect.collidepoint(event.pos):
                            if event.button == 1:
                                if first_click:
                                    first_click = False
                                    board.generate(j.position)
                                    output_matrix(board)
                                board.open(j)
                            elif event.button == 3:
                                board.flag(j)

        pygame.display.update()  # Update screen
        board.draw(screen)
        timer.tick(15)  # Tick fps


if __name__ == '__main__':
    main()
