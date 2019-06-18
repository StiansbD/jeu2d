import pygame
from pygame.locals import *
from const import *

class Perso:
    #class gérant un personnage
    def __init__(self, genre, level):
        
        #sprite du personnage
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        self.idle = pygame.image.load(idle).convert_alpha()
        #perso position in cases and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #default direction
        self.direction = self.idle
        #level where is perso
        self.level = level
