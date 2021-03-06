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

class Platform(pygame.sprite.Sprite):


    def __init__(self, LARGEUR, HAUTEUR):
        #constructeur des platformes
        super().__init__()

        self.image = pygame.Surface([LARGEUR, HAUTEUR])
        self.image.fill(GREEN)
        self.potion_active = False
        self.coffre_active = False
        self.rect = self.image.get_rect()

    def update(self):

        if self.potion_active == True:
            self.potion.update(self.rect.x)

        if self.coffre_active == True:
            self.coffre.update(self.rect.x)
        
