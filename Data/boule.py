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

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("art/0.png").convert()
        self.rect = self.image.get_rect()
        self.rect.y = -200

        self.spriteCount = 0
        self.impact = 0
        self.pause = 0
        
        self.pos = pygame.mouse.get_pos()

        
    def update(self):

        #detection collision sol
        if self.rect.y > 350 and self.impact == 0:
            self.impact = 1
            self.image = pygame.image.load("art/impact.png").convert()
            self.rect.x = self.rect.x - 80
            self.rect.y = self.rect.y - 40
            


        if self.impact == 1:
            self.image.set_alpha(255-self.pause*2.55)
            self.image.set_colorkey(BLACK)
            self.pause += 1            
            if self.pause == 100:
                self.kill()

                        
        else:
            # deplacement position/boule
            self.rect.y = self.rect.y + 25
            self.rect.x = self.pos[0]-50
            
            #animation
            if (pygame.time.get_ticks())%8 == 0:
                spriteN = "art/%s.png"%(int(self.spriteCount))
                self.image = pygame.image.load(spriteN)
                self.spriteCount += 1
                if self.spriteCount == 5:
                    self.spriteCount =0


