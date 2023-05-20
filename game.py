import pygame
from board import Board
import sys

class Game:
    def __init__(self, WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE):
        self.timer = pygame.time.Clock()
        self.board = Board(WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE)
        self.first_click = True
        self.square_size = SQUARE_SIZE

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in self.board.map:
                    for j in i:
                        if j.rect.collidepoint(event.pos):
                            if event.button == 1:
                                if self.first_click:
                                    self.first_click = False
                                    self.board.generate(j.position)
                                self.board.open(j)
                            elif event.button == 3:
                                self.board.flag(j)

    def draw(self, surface: pygame.Surface):
        pygame.display.update()  # Update screen
        self.board.draw(surface)
        self.timer.tick(15)  # Tick fps

