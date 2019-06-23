from pygame.locals import *

#format img
tile_format = 64

#level format
length_level = 12
height_level = 8

#paramètres de la fenêtre
length_window = tile_format * length_level
height_window = tile_format * height_level
center = (length_window/2, height_window/2)

title = "jeu2d"
icon = ""

#position cursor
home_lv1 = (260, 228)
home_lv2 = (260, 330)

#const level
LV1 = 1
LV2 = 2

#perso genre
MAN = "man"
WOMEN = "women"

#perso direction
up = 0
down = 2
right = 3
left = 1

#black screen for refresh
black = Color('black')

#position perso
perso_x = length_window/2
perso_y = height_window/2

start = (2, 2)

#items
apple = (0, 8)
key = (4, 8)
parchment = (6, 4)
necklace = (0, 4)
candle = (6, 8)
hat = (5, 6)
potion = (3, 5)
