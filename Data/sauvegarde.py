import pygame
from knight2 import *
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from intro import *
from ninja import *
from shuriken import *
from hud import *
from entredeux import *
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
ECRAN_LARGEUR  = 800
ECRAN_HAUTEUR = 600
size = [ECRAN_LARGEUR, ECRAN_HAUTEUR]
screen = pygame.display.set_mode(size)

###########################################################
            
def savecheck():
    done = False
    nombre = 0
    while not done :
        try:
            sauvegarde=open("sauvegardes/save%s.txt"%(int(nombre)), "r")
            sauvegarde.close()
            nombre+=1        
        except IOError:
            done = True
    return nombre
 