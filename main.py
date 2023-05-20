import pygame
import random
import sys
from pygame.transform import scale
from menu import Menu
from board import Board
from const import game_settings, WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE, screen_height
from game import Game
# Import files

def main():
    pygame.init()
    back_music = pygame.mixer.Sound('static_files/sound/background.mp3')
    print(back_music.get_volume())
    back_music.set_volume(0.1)
    back_music.play(10)
    while True:
        menu_screen_size = (490, screen_height)
        screen = pygame.display.set_mode(menu_screen_size, pygame.RESIZABLE)

        menu = Menu(menu_screen_size)
        while menu.is_running:
            menu.get_events()
            menu.draw(screen)

        WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE = game_settings[menu.game_settings]
        screen = pygame.display.set_mode((WIDTH * SQUARE_SIZE, screen_height))

        game = Game(WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE)
        while game.is_running:
            game.get_events()
            game.draw(screen)


if __name__ == '__main__':
    main()
