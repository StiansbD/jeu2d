import pygame
from pygame.locals import *
import spritesheet

LARG_MENU = 50

#fenêtre
pygame.init()
fenetre = pygame.display.set_mode((640, 480))

#fond
fond = pygame.image.load("level/tileset.png").convert()
fenetre.blit(fond, (0,LARG_MENU))

#perso
perso = pygame.image.load("sprite/perso.png").convert_alpha()
pos_perso = perso.get_rect()
pos_perso = pos_perso.move(0, LARG_MENU)
fenetre.blit(perso, pos_perso)

#refresh screen
pygame.display.flip()

#infiny
pygame.key.set_repeat(400, 30)
continuer = 1
while continuer:
    #parcours evenement
    for event in pygame.event.get():
        #stop execution
        if event.type == QUIT:
            continuer = 0
        #event souris
        if event.type == MOUSEBUTTONUP:
            if event.button == 3 and event.pos[1] < 100:
                print("Zone dangereuse")
        #event clavier
        if event.type == KEYDOWN:
            #touche Z
            if event.key == K_w:
                print("Avancer")
                pos_perso = pos_perso.move(0, -5)
            #touche ESPACE
            if event.key == K_SPACE:
                print("Sauter")
            #touche S
            if event.key == K_s:
                print("Reculer")
                pos_perso = pos_perso.move(0, 5)
            #touche Q
            if event.key == K_a:
                print("Gauche")
                pos_perso = pos_perso.move(-5, 0)
            #touche D
            if event.key == K_d:
                print("Droite")
                pos_perso = pos_perso.move(5, 0)
            #touche I
            if event.key == K_i:
                print("Inventaire")
            #touche E
            if event.key == K_e:
                print("Sort")

        fenetre.blit(fond, (0,LARG_MENU))
        fenetre.blit(perso, pos_perso)
        pygame.display.flip()
