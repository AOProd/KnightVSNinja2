import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from menu import *
from shuriken import *


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

    change_x = -1
    change_y = 0

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("art/knight_base.000.png")
        self.rect = self.image.get_rect()
        self.rect.y = ECRAN_HAUTEUR - self.rect.height - 150
        self.rebours = 0
        self.shuriken_active = False
        self.actif = False

    def NinjaActif(self,x):
        if x < 800:
            self.actif = True

    def update(self):

        self.NinjaActif(self.rect.x)

        if self.actif == True:
        
            self.rect.x += self.change_x
            
            if self.rebours == 100:
                print("CANCER",self.rect.x)
                self.shuriken = Shuriken(self.rect.x,self.rect.y)
                self.shuriken_active = True
                self.rebours = 0
            
            else:
                self.rebours += 1

            if self.rect.x < 0:
                self.actif = False
                self.kill()
            
        

        

        


