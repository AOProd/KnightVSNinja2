import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from menu import *
from ninja import *
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

class Ninja(pygame.sprite.Sprite,object):

    # vitesse de départ

    change_x = -1
    change_y = 0
    niveau = None

    def __init__(self,joueur):

        super().__init__()

        self.image = pygame.image.load("art/ninja_base.000.png")
        self.rect = self.image.get_rect()
        self.rect.y = ECRAN_HAUTEUR - self.rect.height - 150
        self.rebours = 0
        self.shuriken_active = False
        self.actif = False
        self.joueur = joueur
        self.spriteCount = 0
    def NinjaActif(self,x):
        if x < 800:
            self.actif = True

    def update(self):
        self.NinjaActif(self.rect.x)

        if self.actif == True:
            if pygame.sprite.collide_rect(self.joueur,self):
                self.rect.left = self.joueur.rect.right
                
            if (pygame.time.get_ticks())%8 == 0:
                spriteN = "art/ninja_base.00%s.png"%(int(self.spriteCount))
                self.image = pygame.image.load(spriteN)
                self.spriteCount += 1
                if self.spriteCount == 4:
                    self.spriteCount =0            
            
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
            
        self.rect.x += self.change_x

        

        


