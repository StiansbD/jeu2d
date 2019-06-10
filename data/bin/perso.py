import pygame
from pygame.locals import *
from const import *

class Perso:
    #class gérant un personnage
    def __init__(self, droite, gauche, haut, bas, niveau):
        #sprite du personnage
        self.droite = pygame.image.load().convert_alpha()
