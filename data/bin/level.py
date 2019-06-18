import pygame
from pygame.locals import *
from const import *

class Level:
    def __init__(self):
        path = "../config/"
        self.path = "../resources/level/"
        self.level1 = path + "__level1__.txt"
        self.level2 = path + "__level2__.txt"
        self.struct = 0

        #load img
        self.wall = pygame.image.load(self.path + "wall.png").convert()
        self.floor = pygame.image.load(self.path + "floor.png").convert()

    def generate(self, level):
        if level == LV1:
            file = self.level1
        elif level == LV2:
            file = self.level2

        #open file
        with open(file, "r") as file:
            level_struct = []
            #read line
            for line in file:
                level_line = []
                #read char
                for sprite in line:
                    #forget '\n'
                    if sprite != '\n':
                        #add sprite to list
                        level_line.append(sprite)
                #add line to level list
                level_struct.append(level_line)
            #save this struct
            self.struct = level_struct
            file.close()

    def display(self, window, position):
        window.fill(black)
        #read level list
        line_nb = 0
        for line in self.struct:
            #read line list
            case_nb = 0
            for sprite in line:
                #find real position
                x = (case_nb - position[0]) * tile_format + perso_x
                y = (line_nb - position[1]) * tile_format + perso_y
                if sprite == 'w':                       #wall
                    window.blit(self.wall, (x, y))
                elif sprite == 'f' or sprite == 's':    #floor and start
                    window.blit(self.floor, (x, y))
                case_nb += 1
            line_nb += 1
