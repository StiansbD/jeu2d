import pygame
from pygame.locals import *

from const import *
from spritesheet import *

class SpriteAnim():
    def __init__(self, FPS, genre):
        filename = "../resources/sprite/" + genre + ".png"
        self.FPS = FPS
        self.frames = self.FPS / 12
        self.n = 0
        self.strips = [
            SpriteStripAnim(filename, (0, tile_format * 8, tile_format, tile_format), 9, True, self.frames),
            SpriteStripAnim(filename, (0, tile_format * 9, tile_format, tile_format), 9, True, self.frames),
            SpriteStripAnim(filename, (0, tile_format * 10, tile_format, tile_format), 9, True, self.frames),
            SpriteStripAnim(filename, (0, tile_format * 11, tile_format, tile_format), 9, True, self.frames),
            SpriteStripAnim(filename, (0, tile_format * 12, tile_format, tile_format), 6, True, self.frames),
            SpriteStripAnim(filename, (0, tile_format * 13, tile_format, tile_format), 6, True, self.frames),
            SpriteStripAnim(filename, (0, tile_format * 14, tile_format, tile_format), 6, True, self.frames),
            SpriteStripAnim(filename, (0, tile_format * 15, tile_format, tile_format), 6, True, self.frames),
            SpriteStripAnim(filename, (0, tile_format * 20, tile_format, tile_format), 6, True, self.frames),
        ]
        self.clock = pygame.time.Clock()
        self.strips[self.n].iter()
        self.image = self.strips[self.n].next()

    def set(self, direction):
        self.n = direction
        self.strips[self.n].iter()

    def get(self):
        return self.n

    def play(self, surface):
        surface.blit(self.image, center)
        pygame.display.flip()
        self.image = self.strips[self.n].next()
        self.clock.tick(self.FPS)
