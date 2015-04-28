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
class boule_de_feu(pygame.sprite.Sprite):

    def __init__(self,bouliste,explosiste,boum):

        super().__init__()
        self.bouliste = bouliste
        self.explosiste = explosiste
        self.boum = boum
        self.image = self.bouliste[0]
        self.rect = self.image.get_rect()
        self.rect.y = -200
        self.niveau = None
        self.spriteCount = 0
        self.impact = False
        self.pos = pygame.mouse.get_pos()
        self.son = False

        
    def update(self):
        if self.rect.y > 220 and not self.son:
            self.boum.play()
            self.son = True
        #detection collision sol                
        if self.rect.y > 370 and not self.impact:

            self.spriteCounti = 0
            self.impact = True
            self.image = self.explosiste[0]
            self.rect = pygame.Rect(self.pos[0]-125,320,190,230)

            for ninja in self.niveau.enemy_list:
                if pygame.sprite.collide_rect(self,ninja) == True:
                    ninja.tuer()


        if self.impact:

            self.image = self.explosiste[int(self.spriteCounti/4)]
            self.spriteCounti += 1                                
            if self.spriteCounti == 24:
                self.kill()

                        
        else:
            # deplacement position/boule
            self.rect.y = self.rect.y + 15
            self.rect.x = self.pos[0]-50
            
            #animation
            if (pygame.time.get_ticks())%4 == 0:
                self.image = self.bouliste[(self.spriteCount)]
                self.spriteCount += 1
                if self.spriteCount == 7:
                    self.spriteCount =0


