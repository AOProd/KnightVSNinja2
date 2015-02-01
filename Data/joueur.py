import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from menu import *
from ninja import *
from shuriken import *
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
        self.image = pygame.image.load(filename)

        # la hitbox
        self.rect = self.image.get_rect()
        
        
        self.attack=False
        self.base=True

        #la variable pour l'animation après

        self.sautage = -20
        self.vie = 5
        self.bouclier = 10
        self.boule_de_feu = 10

        self.boucliercooldown = 0
        
    def update(self):
        """ bouger joueur. """   
        # gravité
        self.gravite()

        # mouvement horizontal
        self.rect.x += self.change_x
        self.normal()
        # test de collision
        block_hit_list = pygame.sprite.spritecollide(self, self.niveau.platform_list, False)
        for block in block_hit_list:
            self.rect.right = block.rect.left
            
        enemy_hit_list = pygame.sprite.spritecollide(self, self.niveau.enemy_list, False)
        for ninja in enemy_hit_list:
            self.change_x = 0
            self.base = False
                    
        shuriken_hit_list = pygame.sprite.spritecollide(self, self.niveau.shuriken_list, False)
        for shuriken in shuriken_hit_list:
            self.bouclier -= 1
            self.boucliercooldown = 0
            shuriken.kill()
            
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

        if self.bouclier < 10:    
            self.boucliercooldown +=1
            if self.boucliercooldown > 200:
                self.bouclier += 1
                self.boucliercooldown = 0
            
        if self.bouclier < 0:
            self.vie = self.vie + self.bouclier
            self.bouclier = 0
            
        if self.vie <= 0:
            self.vie = 5
           
    def gravite(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 1

        # test si on est par terre
        if self.rect.y >= ECRAN_HAUTEUR - self.rect.height - 150 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = ECRAN_HAUTEUR - self.rect.height - 150

    def saut(self):

        # test de plateforme si on peut sauter
        if self.base == True:
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.niveau.platform_list, False)
            self.rect.y -= 2

            # saut si on peut
            if len(platform_hit_list) > 0 or self.rect.bottom >= ECRAN_HAUTEUR - 150:
                self.change_y = self.sautage

    def normal(self):
	#mouvement vers la droite tout le temps
        self.change_x = 3
        self.base = True
	
    def attaque(self):
	#coup d'épée
        self.attack=True
        enemy_hit_list = pygame.sprite.spritecollide(self, self.niveau.enemy_list, False)
        for ninja in enemy_hit_list:
            ninja.vie -= 1
		
class JoueurSprite():
    change_x = 3
    change_y = 0

    niveau = None
    
    def __init__(self,joueur):

        super().__init__() 
        self.joueur = joueur
        self.image = pygame.image.load("art/knight_base.000.png")
        self.rect = self.image.get_rect()
        self.spriteAttack=1
        self.spriteCount = 0
        self.spriteJump = 0
        self.attack = False
        
    def update(self):
    
        self.rect.x = self.joueur.rect.x
        self.rect.y = self.joueur.rect.y-25
     
    def updateAnim(self):
        
        if self.joueur.attack == False :
            if self.joueur.change_y == 0 :                     
                spriteN = "art/knight_base.00%s.png"%(int(self.spriteCount))
                self.image = pygame.image.load(spriteN)
                self.spriteCount += 1
                if self.spriteCount == 7:
                    self.spriteCount = 0
                self.spriteJump = 0
            else :
                if self.spriteJump == 0:
                    spriteN = "art/knight_saut.000.png"
                    self.image = pygame.image.load(spriteN)
                    self.spriteJump += 1
                elif self.spriteJump < 3 :
                    spriteN = "art/knight_saut.00%s.png"%(int(self.spriteJump))
                    self.image = pygame.image.load(spriteN)
                    self.spriteJump += 1
        else:
            spriteN = "art/knight_attaque.00%s.png"%(int(self.spriteAttack))
            self.image = pygame.image.load(spriteN)
            self.spriteAttack += 1
            if self.spriteAttack == 4:

                self.joueur.attack=False
                self.spriteAttack = 1
                
        
