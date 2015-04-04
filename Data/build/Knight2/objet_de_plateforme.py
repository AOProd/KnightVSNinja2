import pygame
import random
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from intro import *
from ninja import *
from shuriken import *
from hud import *
from sauvegarde import *
from entredeux import *
# définit les couleurs
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)

class Potion(pygame.sprite.Sprite):

    def __init__(self,width,x,y):

        super().__init__()

        self.image = pygame.image.load("art/potion.png")
        self.rect = self.image.get_rect()
        self.randpos = random.randint(self.rect.width,width)
        self.rect.y = y - self.rect.height
        self.rect.x = x + self.randpos - self.rect.width

    def update(self,x):

        self.rect.x = x + self.randpos - self.rect.width

    def mort(self,joueur):

        self.kill()
        
        joueur.vie += 2

class Coffre(pygame.sprite.Sprite):

    def __init__(self,width,x,y):

        super().__init__()

        self.image = pygame.image.load("art/coffre.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.randpos = random.randint(self.rect.width,width)
        self.rect.y = y - self.rect.height
        self.rect.x = x + self.randpos - self.rect.width

    def update(self,x):

        self.rect.x = x + self.randpos - self.rect.width

    def mort(self,joueur):

        self.kill()
        joueur.bourse += random.randint(50,200)

class Texte(pygame.sprite.Sprite):

    def __init__(self,texte_liste):

        super().__init__()

        self.font = pygame.freetype.Font("police/OldLondon.ttf", 48)
        self.texte = self.font.render(texte_liste[2],BLACK)
        self.rect = self.texte[1]
        self.rect.x = texte_liste[0]
        self.rect.y = texte_liste[1]
        self.image = self.texte[0]
        


        

        



   
        
        
        
