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

        self.joueur = joueur
        self.image = pygame.image.load("art/ninja_base.000.png")
        self.rect = self.image.get_rect()
        self.rect.y = ECRAN_HAUTEUR - self.rect.height - 150
        self.rebours = 0
        self.shuriken_active = False
        self.actif = False
        self.attaque = False
        self.joueur = joueur
        self.spriteCount = 0
        self.spriteCount2 = 0
        self.vie = 3
        
        
    def NinjaActif(self,x):
        if x < 800:
            self.actif = True

    def tuer(self):
        #faut faire lanim de la mor ici ^^
        self.kill()
        self.joueur.bourse += 10

    def Attaque(self):
        self.attaque = True

    def update(self):
        self.NinjaActif(self.rect.x)
        if self.rect.x < 0:
            self.actif = False
            self.kill()

        if self.vie <= 0:
            self.joueur.boule_de_feu += 0.25
            self.tuer()
            
        if self.actif == True:
            #corps a corps
            if pygame.sprite.collide_rect(self.joueur,self): 
                self.rect.left = self.joueur.rect.right-30
                if self.rebours == 100:
                    self.Attaque()
                else :
                    self.rebours += 1
                if (pygame.time.get_ticks())%8 == 0: #animation attaquer (cancer)
                    if self.attaque == True:
                        spriteA = "art/ninjaattaque%s.png"%(int(self.spriteCount2))
                        self.image = pygame.image.load(spriteA)
                        self.spriteCount2 += 1
                        if self.spriteCount2 == 3:
                            self.joueur.bouclier -= 1
                            self.joueur.boucliercount = 0
                        if self.spriteCount2 == 4:
                            self.spriteCount2 = 0
                            self.attaque = False
                            self.rebours = 0
    
            #a distance
            else:
                
                if self.rebours == 100:
                        self.shuriken = Shuriken(self.rect.x,self.rect.y)
                        self.shuriken_active = True
                        self.rebours = 0

                else:
                    self.rebours += 1
                         
                if (pygame.time.get_ticks())%8 == 0: #animation marcher
                    spriteN = "art/ninja_base.00%s.png"%(int(self.spriteCount))
                    self.image = pygame.image.load(spriteN)
                    self.spriteCount += 1
                    if self.spriteCount == 4:
                        self.spriteCount =0            
            
                


                
        self.rect.x += self.change_x

        

        


