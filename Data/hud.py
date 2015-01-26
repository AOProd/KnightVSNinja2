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

class Barre_de_vie():

    def __init__(self,joueur):

        super().__init__()

        self.joueur = joueur
        self.valeur = self.joueur.vie
        self.image = pygame.Surface([self.joueur.vie*80,30])
        self.image.fill(RED)
        self.rect = self.image.get_rect

    def update(self):

        self.image = pygame.Surface([self.joueur.vie*80,30])
        self.image.fill(RED)

class Barre_de_bouclier():

    def __init__(self,joueur):

        super().__init__()

        self.joueur = joueur
        self.valeur = self.joueur.bouclier
        self.image = pygame.Surface([self.joueur.vie*80,30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect

    def update(self):

        self.image = pygame.Surface([self.joueur.vie*80,30])
        self.image.fill(RED)
    
