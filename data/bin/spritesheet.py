import pygame

class spritesheet():
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    #load a specific image from a specific rectangle
    def image_at(self, rectangle):
        #loads image from x, y, x + offset, y + offset
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.set_colorkey((0, 0, 0))
        image.blit(self.sheet, (0, 0), rect)
        return image

    #load a whole bunch of images and return them as a list
    def images_at(self, rects):
        #loads multiple images, supply a list of coordinates
        return [self.image_at(rect) for rect in rects]

    #load a whole strip of images
    def load_strip(self, rect, image_count):
        #loads a strip of images and returns them as a list
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
            for x in range(image_count)]
        return self.images_at(tups)

#to animate sprite
class SpriteStripAnim():
    def __init__(self, filename, rect, count, loop=False, frames=1):
        self.filename = filename
        ss = spritesheet(filename)
        self.images = ss.load_strip(rect, count)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames

    def iter(self):
        self.i = 0
        self.f = self.frames
        return self

    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image

    def __add__(self, ss):
        self.images.extend(ss.images)
        return self
