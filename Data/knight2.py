import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from menu import *
from ninja import *
from shuriken import *
from hud import *

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
    
    #boucle jusqu'a ce que done = true
    pygame.init()

    #l'écran s'affiche
    
    size = [ECRAN_LARGEUR, ECRAN_HAUTEUR]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Knight VS Ninja 2")
    
        #Menu
    #menu()
    #done = menu.done
    
    joueur = Joueur("art/knight.png")
    joueurAnim = JoueurSprite()
    
    background_position = [0, 0]
    background_image = pygame.image.load("art/imagedefond.png").convert()
    
    niveau_list = []
    niveau_list.append(Niveau_01(joueur))
    current_niveau_no = 0
    current_niveau = niveau_list[current_niveau_no]

    active_sprite_list = pygame.sprite.Group()
    hud_sprite_list = pygame.sprite.Group()
    
    joueur.niveau = current_niveau

    joueur.rect.x = 0
    joueur.rect.y = ECRAN_HAUTEUR - joueur.rect.height

    vie = Barre_de_vie(joueur)

    active_sprite_list.add(joueur)


    

    done = False

    clock = pygame.time.Clock()
    pygame.time.set_timer(1, 100)
    
#la grande boucle
    while not done:
	#si cliquer sur fermer
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    joueur.saut()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    joueur.attaque()
                    joueurAnim.attaque()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    boule = boule_de_feu()
                    active_sprite_list.add(boule)
            if event.type == pygame.constants.USEREVENT:
                    pygame.mixer.music.load('art/musicmenu.ogg')
                    pygame.mixer.music.play()
            if event.type == 1:
                    joueurAnim.updateAnim()
            
        # actualiser
        joueurAnim.update(joueur.change_x,joueur.change_y,joueur.rect.x,joueur.rect.y)            
        active_sprite_list.update()
        current_niveau.update()
        vie.update()


       
            

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
        screen.blit(background_image, background_position)
        current_niveau.draw(screen)
    
        active_sprite_list.draw(screen)
        screen.blit(vie.image, [30,30])
        screen.blit(joueurAnim.image, [joueurAnim.rect.x,joueurAnim.rect.y])

        # et au dessus 


        clock.tick(60)

        # update de l'écran
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
