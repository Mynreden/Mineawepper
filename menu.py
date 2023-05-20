import pygame
from const import background, scale
from pygame.transform import flip, chop
import sys

class TextField:
    def __init__(self, text: str, position: tuple, font: str = 'Calibri', size: int = 30):
        self.text = text
        self.font = pygame.font.SysFont(font, size)
        self.image = self.font.render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

class Button(TextField):
    def __init__(self, text: str, position: tuple, font: str = 'Calibri', size: int = 30):
        super().__init__(text, position)
        self.border = pygame.rect.Rect(position[0], position[1], self.rect.width + 20, self.rect.height + 20)
        self.border_color = (0, 0, 200)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.border_color, self.rect, border_radius=15)
        super().draw(surface)

class Menu:
    def __init__(self, size: tuple):
        self.buttons = [Button("  easy  ", (50, 190)),
                        Button("  medium  ", (50, 230)),
                        Button("  hard  ", (50, 270)), ]
        self.text = [TextField('Game "Minesweeper"', (50, 50), 'TimesNewRoman', 40),
                     TextField('made by mynreden', (50, 500), 'TimesNewRoman', 20),
                     TextField('Select difficulty level:', (50, 150))]
        self.is_running = True
        self.game_settings = 0
        self.size = size

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                for i in range(len(self.buttons)):
                    if self.buttons[i].rect.collidepoint(event.pos):
                        self.buttons[i].border_color = (51, 153, 255)
                    else:
                        self.buttons[i].border_color = (0, 0, 200)

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


