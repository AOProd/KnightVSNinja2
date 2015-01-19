import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from menu import *
from ninja import *


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

class Shuriken(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()
        
        self.image = pygame.image.load("art/shuriken.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 10

    def update(self):

        self.rect.x = self.rect.x - 20
        print(self.rect.x)

        if self.rect.x < 0:
            self.kill()
        
        
    
