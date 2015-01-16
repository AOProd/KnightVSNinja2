import pygame
from joueur import *

# définit les couleurs
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)

# taille de l'écran
ECRAN_LARGEUR  = 800
ECRAN_HAUTEUR = 600

size = [ECRAN_LARGEUR, ECRAN_HAUTEUR]
screen = pygame.display.set_mode(size)


    

class Platform(pygame.sprite.Sprite):


    def __init__(self, LARGEUR, HAUTEUR):
        #constructeur des platform
        super().__init__()

        self.image = pygame.Surface([LARGEUR, HAUTEUR])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

class boule_de_feu(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("jeu/0.png").convert()
        self.rect = self.image.get_rect()
        self.rect.y = 0

        self.spriteCount = 0
        

        
    def update(self):

        self.pos = pygame.mouse.get_pos()
        self.rect.y = self.rect.y + 1
        self.rect.x = self.pos[0]-50
        print(self.rect.y)
        print(self.rect.x)
        if (pygame.time.get_ticks())%8 == 0:
            spriteN = "jeu/%s.png"%(int(self.spriteCount))
            self.image = pygame.image.load(spriteN)
            self.spriteCount += 1
            if self.spriteCount == 8:
                self.spriteCount =0
            

class Niveau(object):
    #classe des niveaux

    #images et tout
    platform_list = None
    enemy_list = None

    fond = None

    # taille du niveau
    monde_shift = 0
    niveau_limit = -1000

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

        screen.fill(BLUE)
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


def main():
    pygame.init()

    #l'écran s'affiche
    size = [ECRAN_LARGEUR, ECRAN_HAUTEUR]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Knight VS Ninja 2")

    joueur = Joueur("jeu/knight.png")
    #boule = boule_de_feu()

    niveau_list = []
    niveau_list.append(Niveau_01(joueur))

    current_niveau_no = 0
    current_niveau = niveau_list[current_niveau_no]

    active_sprite_list = pygame.sprite.Group()
    joueur.niveau = current_niveau

    joueur.rect.x = 0
    joueur.rect.y = ECRAN_HAUTEUR - joueur.rect.height
    
    active_sprite_list.add(joueur)
    #active_sprite_list.add(boule)

    #boucle jusqu'a ce que done = true
    done = False

    clock = pygame.time.Clock()

#la grande boucle
    while not done:
		#si cliquer sur fermer
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    joueur.saut()

        # actualiser
        active_sprite_list.update()
        current_niveau.update()

        # scrolling
        if joueur.rect.right >= 100:
            diff = joueur.rect.right - 100
            joueur.rect.right = 100
            current_niveau.shift_monde(-diff)
            
        # changement de niveau et tout
        current_position = joueur.rect.x + current_niveau.monde_shift
        if current_position < current_niveau.niveau_limit:
            if current_niveau_no < len(niveau_list)-1:
                joueur.rect.x = 120
                current_niveau_no += 1
                current_niveau = niveau_list[current_niveau_no]
                joueur.niveau = current_niveau
            else:
                joueur.rect.x = 100
                current_niveau = Niveau_01(joueur)
                joueur.niveau = current_niveau

        # les dessins en dessous :
       
        current_niveau.draw(screen)
        active_sprite_list.draw(screen)

        # et au dessus 


        clock.tick(60)

        # update de l'écran
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
