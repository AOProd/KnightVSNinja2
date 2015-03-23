import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from intro import *
from ninja import *
from shuriken import *
from entredeux import *
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

    niveau = None
    
    def __init__(self, filename, id):

        super().__init__() 
        
        ##################                         SAUVEGARDE
        self.stats0 = [[0,-20],#saut
        [0,60],#attaque
        [0,1],#bouclier
        [0,200],#regen
        [0],#monnaie
        [1]]#son
        self.stats = [[0,-20],#saut
        [0,60],#attaque
        [0,1],#bouclier
        [0,200],#regen
        [0],#monnaie
        [1]]#son

        ######################################################################
        
        
        self.id = id
        self.readsave(self.id)
        
        
        # sprite
        self.image = pygame.image.load(filename)

        # la hitbox
        self.rect = self.image.get_rect()
        
        self.attack=False
        self.base=True

        #la variable pour l'animation après

        self.sautage = self.stats[0][1]
        
        self.vitesseattaque = self.stats[1][1]
        
        self.attackcount = 0
        
        self.boucliermax = self.stats[2][1]
        self.boucliercount= 0
        self.boucliercooldown = self.stats[3][1]
        
        self.sautup = self.stats[0][0]
        self.asup = self.stats[1][0]
        self.shieldup = self.stats[2][0]
        self.regup = self.stats[3][0]

        self.boule_de_feu = 0

        self.bourse = self.stats[4][0]
        
        self.combat = False
        
        self.shwing = pygame.mixer.Sound("art/epee.wav")
        self.sounds = self.stats[5][0]

        self.godmode = False
                
    def update(self):

        self.upstats()

        # gravité
        self.gravite()
        self.combat = False
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
            self.combat = True
            
        shuriken_hit_list = pygame.sprite.spritecollide(self, self.niveau.shuriken_list, False)
        for shuriken in shuriken_hit_list:
            self.bouclier -= 1
            self.boucliercount = 0
            shuriken.kill()

        potion_hit_list = pygame.sprite.spritecollide(self, self.niveau.objet_list, False)
        for objet in potion_hit_list:
            objet.mort(self)
            
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


        if self.bouclier < self.boucliermax:    
            self.boucliercount +=1
            if self.boucliercount > self.boucliercooldown:
                self.bouclier += 1
                self.boucliercount = 0
            
        if self.bouclier < 0:
            self.vie = self.vie + self.bouclier
            self.bouclier = 0

        if self.boule_de_feu < 0:
            self.boule_de_feu = 0
        
        self.attackcount+=1
        
        if self.godmode:
            if self.vie <= 2:
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
        if self.attackcount > self.vitesseattaque:
            if self.sounds:
                self.shwing.play()
            self.attack=True
            enemy_hit_list = pygame.sprite.spritecollide(self, self.niveau.enemy_list, False)
            for ninja in enemy_hit_list:
                ninja.vie -= 1
            self.attackcount = 0
    
    def upstats(self):
        self.stats = [[self.sautup,self.sautage],#saut
        [self.asup,self.vitesseattaque],#attaque
        [self.shieldup,self.boucliermax],#bouclier
        [self.regup,self.boucliercooldown],#regen
        [self.bourse],#monnaie
        [self.sounds]]#son
	
    def readsave(self, id):
        self.fichier = "sauvegardes/save%s.txt"%(int(id))
        try:
            self.sauvegarde = open(self.fichier, "r")
            for i in range(len(self.stats)):
                for u in range(len(self.stats[i])):
                    self.stats[i][u] = int(self.sauvegarde.readline())
            self.sauvegarde.close()
        except IOError: #Si il existe pas
            try:
                self.sauvegarde = open(self.fichier, "w")
                for i in range(len(self.stats0)):
                    for u in range(len(self.stats0[i])):
                        self.sauvegarde.write(str("%s\n"%(int(self.stats0[i][u]))))
                self.sauvegarde.close()
                self.stats = self.stats0
            except IOError:
                print("Sauvegarde créée")
        except ValueError: #Si c'est pas normal
            print("Sauvegarde corrompue o_O")
            try:
                self.sauvegarde = open(self.fichier, "w")
                for i in range(len(self.stats0)):
                    for u in range(len(self.stats0[i])):
                        self.sauvegarde.write(str("%s\n"%(int(self.stats0[i][u]))))
                self.sauvegarde.close()
                print(self.stats0)
                self.stats = self.stats0
            except IOError:
                print("wtf nunu")
        
#####################################
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
            if self.joueur.combat:
                self.image = pygame.image.load("art/knight_combat.png")
            else:
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
                    
            
