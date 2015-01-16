import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *


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
def main():
    pygame.init()

    #l'écran s'affiche
    size = [ECRAN_LARGEUR, ECRAN_HAUTEUR]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Knight VS Ninja 2")

    joueur = Joueur("art/knight.png")
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
