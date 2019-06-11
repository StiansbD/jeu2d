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
from home import *
from level import *

window = Window(title, icon, length_window, height_window)
screen = window.generate()

home = Home()
home.load(screen, home_lv1)
lv = LV1

while window.state():

    for event in pygame.event.get():
        window.exit(event)

    while home.state():
        #limite boucle speed
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            #exit soft
            if not(window.exit(event)):
                home.exit()

            #gestion menu
            if event.type == KEYDOWN:
                #select down
                if event.key == K_s:
                    home.load(screen, home_lv2)
                    lv = LV2
                #select up
                if event.key == K_w:
                    home.load(screen, home_lv1)
                    lv = LV1
                #select level
                if event.key == K_RETURN:
                    home.exit()

    level = Level()
    level.generate(lv)
    level.display(screen)

    pygame.display.flip()
