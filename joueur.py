import pygame
from knight2 import *
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

        #la variable pour l'animation après
        self.spriteCount = 0
        self.spriteJump = 0
        
    def update(self):
        """ bouger joueur. """

        #ANIMATION
        if self.change_y == 0 :      
            if (pygame.time.get_ticks())%8 == 0:
                spriteN = "jeu/knight_base.00%s.png"%(int(self.spriteCount))
                self.image = pygame.image.load(spriteN)
                self.spriteCount += 1
                if self.spriteCount == 7:
                    self.spriteCount = 0
            self.spriteJump = 0
        else :
            if self.spriteJump ==0:
                spriteN = "jeu/knight_saut.000.png"
                self.image = pygame.image.load(spriteN)
                self.spriteJump += 1
            elif (pygame.time.get_ticks())%8 == 0 and self.spriteJump<3 :
                spriteN = "jeu/knight_saut.00%s.png"%(int(self.spriteJump))
                self.image = pygame.image.load(spriteN)
                self.spriteJump += 1
                
        
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
            


    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # test si on est par terre
        if self.rect.y >= ECRAN_HAUTEUR - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = ECRAN_HAUTEUR - self.rect.height

    def saut(self):

        # test de plateforme si on peut sauter
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.niveau.platform_list, False)
        self.rect.y -= 2

        # saut si on peut
        if len(platform_hit_list) > 0 or self.rect.bottom >= ECRAN_HAUTEUR:
            self.change_y = -10

    def stop(self):
		#quand rien se passe
        self.change_x = 3
