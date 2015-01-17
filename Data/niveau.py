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

class Niveau(object):
    #classe des niveaux

    #images et tout
    platform_list = None
    enemy_list = None

    fond = None

    # taille du niveau
    monde_shift = 0
    niveau_limit = -10000

    def __init__(self, joueur):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.joueur = joueur

    # actualisation
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        #afficher les sprites et graphiques
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_monde(self, shift_x):
        #scrolling
        self.monde_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# créer le premier niveau
class Niveau_01(Niveau):

    def __init__(self, joueur):

        Niveau.__init__(self, joueur)

        self.niveau_limit = -1300

        # mesures des platformes
        niveau = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]


        # création des plateformes
        for platform in niveau:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.joueur = self.joueur
            self.platform_list.add(block)

