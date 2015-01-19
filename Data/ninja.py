import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
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

# KnightVSNinja2
import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from menu import *


# définit les couleurs
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)

# taille de l'écran
ECRAN_LARGEUR  = 800
ECRAN_HAUTEUR = 600

size = [ECRAN_LARGEUR, ECRAN_HAUTEUR]
screen = pygame.display.set_mode(size)

class Ninja(pygame.sprite.Sprite):

    # vitesse de départ

    change_x = -6
    change_y = 0

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("art/knight.png")
        self.rect = self.image.get_rect()
        self.rect.y = ECRAN_HAUTEUR - self.rect.height - 150
        self.rect.x = 1500
        

    def update(self):

        self.rect.x += self.change_x

