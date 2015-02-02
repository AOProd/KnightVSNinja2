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
    
class Barre_de_vie(pygame.sprite.Sprite):

    def __init__(self,joueur):

        super().__init__()

        self.joueur = joueur
        self.valeur_vie = self.joueur.vie
        self.image = pygame.Surface([self.joueur.vie*80,30])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 35
        self.rect.y = 25

    def update(self):

        self.image = pygame.Surface([self.joueur.vie*80,30])
        self.image.fill(RED)

class Coeur(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("art\keur.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 25
        
        
class Barre_de_bouclier(pygame.sprite.Sprite):

    def __init__(self,joueur):

        super().__init__()

        self.joueur = joueur
        self.image = pygame.Surface([self.joueur.bouclier*40,30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 35
        self.rect.y = 57

    def update(self):

        self.image = pygame.Surface([self.joueur.bouclier*40,30])
        self.image.fill(WHITE)

class Bouclier(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("art\shield.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 57

class Barre_de_boule_de_feu(pygame.sprite.Sprite):

    def __init__(self,joueur):

        super().__init__()

        self.joueur = joueur
        self.image = pygame.Surface([self.joueur.boule_de_feu*40,30])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 550

    def update(self):
        
        self.image = pygame.Surface([self.joueur.boule_de_feu*40,30])
        self.image.fill(BLUE)

class Feu(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("art\ssss.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 550

class Argent(pygame.sprite.Sprite):

    def __init__(self,joueur):

        super().__init__()

        self.font = pygame.font.Font(None, 36)
        self.joueur = joueur
        self.image = self.font.render(str(self.joueur.bourse), True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 730
        self.rect.y = 30

    def update(self):

        self.image = self.font.render(str(self.joueur.bourse), True, WHITE)
        
    
class Bourse(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("art\sbourse.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 690
        self.rect.y = 25
