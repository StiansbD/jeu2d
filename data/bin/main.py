#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
jeu2d
jeu dans lequel on doit deplacer un personnage d'un point à l'autre

script python
fichiers: main.py const.py window.py home.py perso.py
"""

import pygame
from pygame.locals import *

from const import *
from window import *

window = Window(title, icon, length_window, height_window)
window = window.generate()

purchase = 1
purchase_home = 1

home = pygame.image.load("../resources/menu/home.png").convert_alpha()
window.blit(home, (0,0))

cursor = pygame.image.load("../resources/menu/cursor.png").convert()
cursor.set_colorkey((0, 0, 0))
window.blit(cursor, home_lv1)
pygame.display.flip()

while purchase:

    while purchase_home:
        #limite boucle speed
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            #exit soft
            if event.type == QUIT:
                purchase = 0
                purchase_home = 0

            if event.type == KEYDOWN:
                window.blit(home, (0,0))
                #select down
                if event.key == K_s:
                    window.blit(cursor, home_lv2)
                #select up
                if event.key == K_w:
                    window.blit(cursor, home_lv1)

        pygame.display.flip()
