import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from knight2 import *

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
ECRAN_LARGEUR  = 800
ECRAN_HAUTEUR = 600
size = [ECRAN_LARGEUR, ECRAN_HAUTEUR]
screen = pygame.display.set_mode(size)

###################################################
def hud(joueur):
    ##joueur
    vie = pygame.image.load("art\keur.png")
    for i in range(joueur.vie):
        screen.blit(vie, [35*(i+1),25])
    ##bouclier
    bouclier = pygame.image.load("art\shield.png")
    for i in range(joueur.bouclier):
        screen.blit(bouclier, [35*(i+1),60])
    ##boule de feu
    icofeu = pygame.image.load("art/bouleico.png")
    screen.blit(icofeu, [5,546])
    feu = pygame.Surface([joueur.boule_de_feu*40,30])
    feu.fill(RED)
    screen.blit(feu, [40,550])
    ##argent
    bourse = pygame.image.load("art/bourse.png")
    screen.blit(bourse, [680,28])
    font = pygame.freetype.Font("police/freesansbold.ttf", 36)
    monnaie = font.render("%s"%(joueur.bourse), WHITE)
    textpos=[730-monnaie[1].width/2,30]
    screen.blit(monnaie[0],textpos)
