import pygame
import random
import sys
from pygame.transform import scale
from menu import Menu
from board import Board
from const import game_settings, WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE
from game import Game
# Import files

def main():
    pygame.init()
    menu_screen_size = (600, 600)
    screen = pygame.display.set_mode(menu_screen_size, pygame.RESIZABLE)
    menu = Menu(menu_screen_size)
    while menu.is_running:
        menu.get_events()
        menu.draw(screen)

    WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE = game_settings[menu.game_settings]
    screen = pygame.display.set_mode((WIDTH * SQUARE_SIZE, HEIGHT * SQUARE_SIZE))

    game = Game(WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE)
    while True:
        game.get_events()
        game.draw(screen)


if __name__ == '__main__':
    main()
