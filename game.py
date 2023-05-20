import pygame
from board import Board
import sys
from menu import Button
from const import screen_height
import time


class Game:
    def __init__(self, WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE):
        self.restart = Button('  restart  ', (0, 0),size=30)
        self.restart.rect.topleft = (370, 20)
        self.restart.border_color = (170, 170, 170)
        self.mines_left = BOMBS_NUMBER
        self.time = 0
        self.font = pygame.font.SysFont('Calibri', 30)
        self.timer = pygame.time.Clock()
        self.upper_border = screen_height - HEIGHT * SQUARE_SIZE
        self.board = Board(WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE)
        self.first_click = True
        self.square_size = SQUARE_SIZE
        self.is_running = True
        self.is_defeated = False

        self.click_sound = pygame.mixer.Sound('static_files/sound/click.wav')
        self.bomb_sound = pygame.mixer.Sound('static_files/sound/bomb.wav')
        self.win_sound = pygame.mixer.Sound('static_files/sound/win.wav')

    def get_events(self):
        if not self.is_defeated:
            self.get_events_alive()
        else:
            self.get_events_defeat()

    def get_events_alive(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart.rect.collidepoint(event.pos):
                    self.is_running = False
                    continue
                for i in self.board.map:
                    for j in i:
                        if j.rect.collidepoint(event.pos):
                            if event.button == 1:
                                if self.first_click:
                                    self.first_click = False
                                    self.board.generate(j.position)
                                self.board.open(j)
                                if j.number == -1:
                                    self.bomb_sound.play()
                                    self.is_defeated = True
                                else:
                                    self.click_sound.play()
                                if self.board.squares_left == 0 and not self.is_defeated:
                                    self.win_sound.play()
                            elif event.button == 3:
                                self.click_sound.play()
                                if self.board.flag(j):
                                    self.mines_left -= 1
                                else:
                                    self.mines_left += 1
            elif event.type == pygame.MOUSEMOTION:
                if self.restart.rect.collidepoint(event.pos):
                    self.restart.border_color = (200, 200, 200)
                else:
                    self.restart.border_color = (170, 170, 170)

    def get_events_defeat(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart.rect.collidepoint(event.pos):
                    self.is_running = False

            elif event.type == pygame.MOUSEMOTION:
                if self.restart.rect.collidepoint(event.pos):
                    self.restart.border_color = (200, 200, 200)
                else:
                    self.restart.border_color = (170, 170, 170)

    def draw(self, surface: pygame.Surface):
        if not self.first_click:
            self.time += 1
        if self.is_defeated or self.board.squares_left == 0:
            self.time -= 1

        pygame.display.update()  # Update screen

        if self.board.squares_left == 0 and not self.is_defeated:
            self.draw_won(surface)
            return
        pygame.draw.rect(surface, (150, 150, 150), pygame.rect.Rect((0, 0),(600, screen_height)))
        inf = self.font.render(f'time: {self.time // 60} | mines left: {self.mines_left} |', True, (0,0,0))
        self.restart.draw(surface)

        surface.blit(inf,(30, 20))
        self.board.draw(surface)

        self.timer.tick(60)  # Tick fps

    def draw_won(self, surface: pygame.Surface):

        pygame.draw.rect(surface, (150, 150, 150), pygame.rect.Rect((0, 0),(600, screen_height)))
        self.board.draw(surface)

        pygame.draw.rect(surface, (255, 255, 255), (95, 130, 300, 300), border_radius=10)

        won_mess = self.font.render('You won!!!', True, (0,0,0),)
        additional_mess = self.font.render(f'Your time: {self.time // 60}s',True, (0,0,0))
        self.restart.rect.topleft = (193, 350)
        self.restart.draw(surface)

        surface.blit(additional_mess, (150, 250))
        surface.blit(won_mess,(180, 180))

        self.timer.tick(60)  # Tick fps

