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

        self.pos = pygame.mouse.get_pos()

        
    def update(self):

        # deplacement position/boule
        self.rect.y = self.rect.y + 15
        self.rect.x = self.pos[0]-50

        #animation
        if (pygame.time.get_ticks())%8 == 0:
            spriteN = "art/%s.png"%(int(self.spriteCount))
            self.image = pygame.image.load(spriteN)
            self.spriteCount += 1
            if self.spriteCount == 5:
                self.spriteCount =0

        #detection collision sol
        if self.rect.y > 350:
            self.kill()


            # arrête le mouvement
            self.change_y = 0
        
