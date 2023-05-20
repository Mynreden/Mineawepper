import pygame
from pygame.transform import scale

spr_emptyGrid = pygame.image.load("static_files/images/empty.png")
spr_flag = pygame.image.load("static_files/images/flag.png")
spr_grid = pygame.image.load("static_files/images/Grid.png")
spr_grid1 = pygame.image.load("static_files/images/grid1.png")
spr_grid2 = pygame.image.load("static_files/images/grid2.png")
spr_grid3 = pygame.image.load("static_files/images/grid3.png")
spr_grid4 = pygame.image.load("static_files/images/grid4.png")
spr_grid5 = pygame.image.load("static_files/images/grid5.png")
spr_grid6 = pygame.image.load("static_files/images/grid6.png")
spr_grid7 = pygame.image.load("static_files/images/grid7.png")
spr_grid8 = pygame.image.load("static_files/images/grid8.png")
spr_mine = pygame.image.load("static_files/images/mine.png")
spr_mineClicked = pygame.image.load("static_files/images/mineClicked.png")
spr_mineFalse = pygame.image.load("static_files/images/mineFalse.png")

background = pygame.image.load("static_files/images/menu_background.png")

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
game_settings = [(8, 8 , 10, 61), (14, 14, 40, 35), (20, 20, 99, 24)]
WIDTH, HEIGHT, BOMBS_NUMBER, SQUARE_SIZE = game_settings[0]
