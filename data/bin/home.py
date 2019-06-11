import pygame
from pygame.locals import *

class Home:
    #gérer le menu principal
    def __init__(self):
        self.purchase = 1

    def exit(self):
        self.purchase = 0
        return self.purchase

    def state(self):
        return self.purchase

    def load(self, window, level):
        #load home
        home = pygame.image.load("../resources/menu/home.png").convert_alpha()
        window.blit(home, (0,0))
        #load cursor
        cursor = pygame.image.load("../resources/menu/cursor.png").convert()
        cursor.set_colorkey((0, 0, 0))
        window.blit(cursor, level)
        pygame.display.flip()
