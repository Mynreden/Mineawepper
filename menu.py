import pygame
from const import background, scale
from pygame.transform import flip, chop
import sys

class TextField:
    def __init__(self, text: str, position: tuple, font: str = 'Calibri', size: int = 35):
        self.text = text
        self.font = pygame.font.SysFont(font, size)
        self.image = self.font.render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

class Button(TextField):
    def __init__(self, text: str, position: tuple):
        super().__init__(text, position)
        self.border = pygame.rect.Rect(position[0], position[1], self.rect.width + 20, self.rect.height + 20)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (0,0,0), self.rect)
        super().draw(surface)

class Menu:
    def __init__(self, size: tuple):
        self.buttons = [Button(" easy ", (50, 200)),Button(" medium ", (50, 250)),Button(" hard ", (50, 300)), ]
        self.text = [TextField('Game "Minesweeper"', (50, 50), 'TimesNewRoman', 50),
                     TextField('made by mynreden', (50, 500), 'TimesNewRoman', 20),
                     TextField('Select difficulty level:', (50, 150))]
        self.is_running = True
        self.game_settings = 0
        self.size = size

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.buttons)):
                    if self.buttons[i].rect.collidepoint(event.pos):
                        self.is_running = False
                        self.game_settings = i

    def draw(self, surface: pygame.Surface):
        pygame.display.update()  # Update screen

        surface.blit(scale(background, pygame.display.get_window_size()), (0, 0))
        for i in self.buttons:
            i.draw(surface)
        for i in self.text:
            i.draw(surface)


