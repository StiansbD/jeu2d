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
from sprite_anim import *

perso = WOMEN
window = Window(title, icon, length_window, height_window)
screen = window.generate()

home = Home()
lv = LV1
level = Level()

anim = SpriteAnim(120, perso)
game = 0
pygame.key.set_repeat(10, 150)

while window.state():
    for event in pygame.event.get():
        window.exit(event)

    position = start
    screen.fill(black)
    lv = home.load(screen, home_lv1)
    while home.state():
        for event in pygame.event.get():
            #exit soft
            if not(window.exit(event)):
                home.exit()

            #gestion menu
            if event.type == KEYDOWN:
                #select down
                if event.key == K_s:
                    lv = home.load(screen, home_lv2)
                #select up
                if event.key == K_w:
                    lv = home.load(screen, home_lv1)
                #select level
                if event.key == K_RETURN:
                    screen.fill(black)
                    level.generate(lv)
                    level.display(screen, position)
                    pygame.display.flip()
                    game = 1
                    home.exit()

    while game:
        for event in pygame.event.get():
            if not(window.exit(event)):
                game = 0
            if event.type == KEYDOWN:
                if event.key == K_w:
                    new_position = (position[0], position[1] - 1)
                    if level.get(new_position):
                        position = new_position
                    if anim.get() != up:
                        anim.set(up)
                if event.key == K_s:
                    new_position = (position[0], position[1] + 1)
                    if level.get(new_position):
                        position = new_position
                    if anim.get() != down:
                        anim.set(down)
                if event.key == K_a:
                    new_position = (position[0] - 1, position[1])
                    if level.get(new_position):
                        position = new_position
                    if anim.get() != left:
                        anim.set(left)
                if event.key == K_d:
                    new_position = (position[0] + 1, position[1])
                    if level.get(new_position):
                        position = new_position
                    if anim.get() != right:
                        anim.set(right)
                if event.key == K_ESCAPE:
                    game = 0
                    home.set(1)

        #anim.play(screen)
        level.display(screen, position)
        anim.play(screen)

    pygame.display.flip()
