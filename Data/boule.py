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

    def __init__(self,joueur):

        super().__init__()
        self.boum = pygame.mixer.Sound("art/explosion.wav")
        self.pouet = pygame.mixer.Sound("art/pouet.wav")

        self.actif = False
        self.joueur = joueur
        
        if self.joueur.boule_de_feu >= 1:
            self.image = pygame.image.load("art/boule1.png")
            self.rect = self.image.get_rect()
            self.rect.y = -200
            self.niveau = None
            self.spriteCount = 0
            self.impact = False
            self.pos = pygame.mouse.get_pos()
            self.joueur.boule_de_feu -= 1
            self.actif = True
            self.son = False
            
        elif joueur.sounds:
            self.pouet.play()

        
    def update(self):
        if self.actif == True :

            if self.rect.y > 220 and self.joueur.sounds and not self.son:
                self.boum.play()
                self.son = True
            #detection collision sol                
            if self.rect.y > 370 and not self.impact:

                self.spriteCounti = 0
                self.impact = True
                self.image = pygame.image.load("art/explosion1.png").convert()
                self.rect = pygame.Rect(self.pos[0]-125,320,190,230)

                for ninja in self.niveau.enemy_list:
                    if pygame.sprite.collide_rect(self,ninja) == True:
                        ninja.tuer()


            if self.impact:
                
                spriteN = "art/explosion%s.png"%(int(self.spriteCounti/4+1))
                self.image = pygame.image.load(spriteN)
                self.spriteCounti += 1                                
                if self.spriteCounti == 24:
                    self.kill()

                            
            else:
                # deplacement position/boule
                self.rect.y = self.rect.y + 15
                self.rect.x = self.pos[0]-50
                
                #animation
                if (pygame.time.get_ticks())%4 == 0:
                    spriteN = "art/boule%s.png"%(int(self.spriteCount+1))
                    self.image = pygame.image.load(spriteN)
                    self.spriteCount += 1
                    if self.spriteCount == 6:
                        self.spriteCount =0


