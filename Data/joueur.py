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

class Joueur(pygame.sprite.Sprite):
    #classe du joueur

    # vitesse de départ

    change_x = 3
    change_y = 0

    # sprites ou on peut rentrer dedans
    niveau = None
    
    def __init__(self, filename):

        super().__init__() 

        # sprite
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)

        # la hitbox
        self.rect = self.image.get_rect()
		
        self.attack=False


        #la variable pour l'animation après
        self.spriteAttack=0
        self.spriteCount = 0
        self.spriteJump = 0
        
    def update(self):
        """ bouger joueur. """
              
        # gravité
        self.calc_grav()

        # mouvement horizontal
        self.rect.x += self.change_x

        # test de collision
        block_hit_list = pygame.sprite.spritecollide(self, self.niveau.platform_list, False)
        for block in block_hit_list:
            self.rect.right = block.rect.left

        # mouvement vertical
        self.rect.y += self.change_y

        # test de collision
        block_hit_list = pygame.sprite.spritecollide(self, self.niveau.platform_list, False)
        for block in block_hit_list:

            # change la position si c'est en bas ou en haut qu'on touche
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # arrête le mouvement
            self.change_y = 0
    
    def updateAnim(self):
        
        if self.attack == False :
            if self.change_y == 0 :                     
                spriteN = "art/knight_base.00%s.png"%(int(self.spriteCount))
                self.image = pygame.image.load(spriteN)
                self.spriteCount += 1
                if self.spriteCount == 7:
                    self.spriteCount = 0
                self.spriteJump = 0
            else :
                if self.spriteJump ==0:
                    spriteN = "art/knight_saut.000.png"
                    self.image = pygame.image.load(spriteN)
                    self.spriteJump += 1
                elif self.spriteJump<3 :
                    spriteN = "art/knight_saut.00%s.png"%(int(self.spriteJump))
                    self.image = pygame.image.load(spriteN)
                    self.spriteJump += 1
        else:
            spriteN = "art/knight_attaque.00%s.png"%(int(self.spriteAttack))
            self.image = pygame.image.load(spriteN)
            self.spriteAttack += 1
            if self.spriteAttack == 5:
                self.attack=False
                self.spriteAttack = 0
            


    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # test si on est par terre
        if self.rect.y >= ECRAN_HAUTEUR - self.rect.height - 150 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = ECRAN_HAUTEUR - self.rect.height - 150

    def saut(self):

        # test de plateforme si on peut sauter
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.niveau.platform_list, False)
        self.rect.y -= 2

        # saut si on peut
        if len(platform_hit_list) > 0 or self.rect.bottom >= ECRAN_HAUTEUR - 150:
            self.change_y = -10

    def stop(self):
	#mouvement vers la droite tout le temps
        self.change_x = 3
	
    def attaque(self):
	#coup d'épée
        self.attack=True
		