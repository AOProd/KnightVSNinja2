import pygame
import random
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from intro import *
from ninja import *
from shuriken import *
from objet_de_plateforme import *
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

class Niveau(object):
    #classe des niveaux

    #images et tout
    platform_list = None
    enemy_list = None
    shuriken_list = None
    potion_list = None
    texte_list = None

    fond = None

    # taille du niveau
    monde_shift = 0
    niveau_limit = -10000

    def __init__(self, joueur):
        
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.shuriken_list = pygame.sprite.Group()
        self.objet_list = pygame.sprite.Group()
        self.texte_list = pygame.sprite.Group()
        self.joueur = joueur
        self.joueur.vie = 5
        self.joueur.bouclier = self.joueur.boucliermax

    # actualisation
    def update(self):
        for ninja in self.enemy_list:
            if ninja.shuriken_active == True:
                self.shuriken_list.add(ninja.shuriken)
                ninja.shuriken_active = False
        self.platform_list.update()
        self.enemy_list.update()
        self.shuriken_list.update()


    def draw(self, screen):
        #afficher les sprites et graphiques
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.shuriken_list.draw(screen)
        self.objet_list.draw(screen)
        self.texte_list.draw(screen)

    def shift_monde(self, shift_x):
        #scrolling
        self.monde_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for texte in self.texte_list:
            texte.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# créer le premier niveau
class Niveau_Tutorial(Niveau):

    def __init__(self, joueur):

        Niveau.__init__(self, joueur)
        self.background = pygame.image.load("art/imagedefond.png").convert()
        self.niveau_limit = -6000
        self.joueur.boule_de_feu = 1
        self.nom = "Tutorial"
        
        #mesures des platformes
        plateformes_niveau = [[200, 150, 2700, 300]
                 ]

        #création des plateformes
        for platform in plateformes_niveau:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.joueur = self.joueur
            self.platform_list.add(block)

    
        #mesures de ninjas
        ninjas_niveau = [6200,7820,7840,7860]

        #creation ninjas
        for ninja in ninjas_niveau:
            self.nin = Ninja(self.joueur)
            self.nin.rect.x = ninja
            self.enemy_list.add(self.nin)

        texte_niveau = [[1000,150,"Bienvenue dans Knight VS Ninja 2"],
                        [2500,150,"Appuyez sur la touche du haut pour sauter"],
                        [4350,150,"Usez du click gauche pour attaquer"],
                        [5500,150,"Usez du click droit"],
                        [5450,200,"pour envoyer une boule de feu"]
                        ]

        for texte_liste in texte_niveau:
            self.texte = Texte(texte_liste)
            self.texte_list.add(self.texte)
            
# créer le premier niveau
class Niveau_01(Niveau):

    def __init__(self, joueur):

        Niveau.__init__(self, joueur)
        self.background = pygame.image.load("art/imagedefond.png").convert()
        self.niveau_limit = -2000
        self.nom = "Niveau 1"

        #mesures des platformes
        plateformes_niveau = [[100, 20, 800, 300],
                 [150, 20, 1350, 300],
                 [150, 20, 1720, 300],
                 ]


        #création des plateformes
        for platform in plateformes_niveau:
            self.chance_coffre = random.randint(0,9)
            self.chance_potion = random.randint(0,4)
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.joueur = self.joueur
            if self.chance_potion == 4:
                block.potion = Potion(block.rect.width,block.rect.x,block.rect.y)
                self.objet_list.add(block.potion)
                block.potion_active = True
            if self.chance_coffre == 9:
                block.coffre = Coffre(block.rect.width,block.rect.x,block.rect.y)
                self.objet_list.add(block.coffre)
                block.coffre_active = True
            self.platform_list.add(block)

        #mesures de ninjas
        ninjas_niveau = [1000,1500,2000,2500,3000]

        #creation ninjas
        for ninja in ninjas_niveau:
            self.nin = Ninja(self.joueur)
            self.nin.rect.x = ninja
            self.enemy_list.add(self.nin)

class Niveau_02(Niveau):

    def __init__(self, joueur):

        Niveau.__init__(self, joueur)
        self.background = pygame.image.load("art/fondmenu.png").convert()
        self.niveau_limit = -2000
        self.nom = "Niveau 2"

        #mesures des platformes
        plateformes_niveau = [[110, 20, 600, 300],
                 [150, 20, 1000, 255],
                 [150, 20, 1350, 255],
                 [150, 20, 1700, 300],
                 ]


        #création des plateformes
        for platform in plateformes_niveau:
            self.chance_coffre = random.randint(0,9)
            self.chance_potion = random.randint(0,4)
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.joueur = self.joueur
            if self.chance_potion == 4:
                block.potion = Potion(block.rect.width,block.rect.x,block.rect.y)
                self.objet_list.add(block.potion)
                block.potion_active = True
            if self.chance_coffre == 9:
                block.coffre = Coffre(block.rect.width,block.rect.x,block.rect.y)
                self.objet_list.add(block.coffre)
                block.coffre_active = True
            self.platform_list.add(block)

        #mesures de ninjas
        ninjas_niveau = [1100,1100,1500,2000,2500,3000]

        #creation ninjas
        for ninja in ninjas_niveau:
            self.nin = Ninja(self.joueur)
            self.nin.rect.x = ninja
            self.enemy_list.add(self.nin)

class Niveau_03(Niveau):

    def __init__(self, joueur):

        Niveau.__init__(self, joueur)
        self.background = pygame.image.load("art/fondmenu.png").convert()
        self.niveau_limit = -3000
        self.nom = "Niveau 3"

        #mesures des platformes
        plateformes_niveau = [[190, 20, 690, 300],
                 [150, 20, 1200, 255],
                 [150, 20, 1930, 300],
                 [150, 20, 2370, 230],
                 [150, 20, 2720, 300],
                 ]


        #création des plateformes
        for platform in plateformes_niveau:
            self.chance_coffre = random.randint(0,9)
            self.chance_potion = random.randint(0,4)
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.joueur = self.joueur
            if self.chance_potion == 4:
                block.potion = Potion(block.rect.width,block.rect.x,block.rect.y)
                self.objet_list.add(block.potion)
                block.potion_active = True
            if self.chance_coffre == 9:
                block.coffre = Coffre(block.rect.width,block.rect.x,block.rect.y)
                self.objet_list.add(block.coffre)
                block.coffre_active = True
            self.platform_list.add(block)

        #mesures de ninjas
        ninjas_niveau = [700,1300,1500,2200,2500,3300,3900,4500]

        #creation ninjas
        for ninja in ninjas_niveau:
            self.nin = Ninja(self.joueur)
            self.nin.rect.x = ninja
            self.enemy_list.add(self.nin)
