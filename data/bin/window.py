import pygame
from pygame.locals import *

class Window:
    #generation d'une fenêtre via pygame
    def __init__(self, title, icon, length, height):
        self.title = title
        self.icon = icon
        self.length = length
        self.height = height
        self.purchase = 1

    def state(self):
        return self.purchase

    def generate(self):
        pygame.init()
        #open window
        window = pygame.display.set_mode((self.length, self.height))
        #titre
        pygame.display.set_caption(self.title)
        return(window)

    def exit(self, event):
        #exit soft
        if event.type == QUIT:
            self.purchase = 0

        return self.purchase
