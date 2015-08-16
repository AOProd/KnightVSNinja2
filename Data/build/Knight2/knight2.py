import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from intro import *
from ninja import *
from shuriken import *
from hud import *
from sauvegarde import *
from entredeux import *
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

def main(ider):
    
    #boucle jusqu'a ce que fin = true


    #l'écran s'affiche
    pygame.init()   
    pygame.display.set_caption("Knight VS Ninja 2")
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    logo = pygame.image.load("art/favicon.ico")
    pygame.display.set_icon(logo)
    
    pygame.freetype.init()
    font1 = pygame.freetype.Font("police/shanghai.ttf", 36)
    font2 = pygame.freetype.Font("police/OldLondon.ttf", 36)    

        #charger la partie par l'intro ou l'id
    if ider == None:
        saveid = intro()
    else : 
        saveid = ider
    #création du joueur
    joueur = Joueur("art/knight.png", saveid)
    joueurAnim = JoueurSprite(joueur)
    #création des niveaux
    niveau_list = []
    niveau_list.append(Niveau_Tutorial(joueur)) 
    niveau_list.append(Niveau_01(joueur))
    niveau_list.append(Niveau_02(joueur))
    niveau_list.append(Niveau_03(joueur))
    current_niveau_no = joueur.niveau_no
    current_niveau = niveau_list[current_niveau_no]
        
    background_position = [0, 0]
    background_image = current_niveau.background

    active_sprite_list = pygame.sprite.Group()
    hud_list = pygame.sprite.Group()

    joueur.niveau = current_niveau
    joueurAnim.niveau = current_niveau

    joueur.rect.x = 0
    joueur.rect.y = ECRAN_HAUTEUR - joueur.rect.height

    #Fondu imagé
    
    nomniveau = font1.render(current_niveau.nom, WHITE)
    nomniveaupos = [400-nomniveau[1].width/2,300]
    
    ecrannoir = pygame.Surface((ECRAN_LARGEUR,ECRAN_HAUTEUR))
    ecrannoir.fill(BLACK)
    ecrannoir.blit(nomniveau[0],nomniveaupos)
    ecrannoiralpha = 255
    
    active_sprite_list.add(joueur)
    
    clock = pygame.time.Clock()
    pygame.time.set_timer(1, 100)
    fin = False
    over = False
#la grande boucle
    while not fin:
	#si cliquer sur fermer
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    joueur.saut()
                if event.key == pygame.K_s:
                    if joueur.sounds: #son
                        joueur.sounds=0
                    else:
                        joueur.sounds=1
                        
                if event.key == pygame.K_x: #CHEAT BOUTON !!!!
                    joueur.bourse+=100
                if event.key == pygame.K_u: #CHEAT BOUTON !!!!
                    joueur.boule_de_feu+=100
                if event.key == pygame.K_o: #CHEAT BOUTON !!!
                    if joueur.godmode :
                        joueur.godmode = False
                    else:
                        joueur.godmode = True
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    joueur.attaque()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    boule = boule_de_feu(joueur)
                    boule.niveau = current_niveau
                    if boule.actif == True:
                        active_sprite_list.add(boule)
            
            if event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load("art/internationale.mp3")
                pygame.mixer.music.play()
            if event.type == 1:
                joueurAnim.updateAnim()
                

        if ecrannoiralpha > 0 : #fondu imagé encore
            ecrannoiralpha -= 1
            ecrannoir.set_alpha(ecrannoiralpha)
                
        # actualiser
        
        joueurAnim.update()            
        current_niveau.update()
        active_sprite_list.update()
        hud_list.update()
            

        # scrolling
        scrolette = 100
        if joueur.rect.right >= scrolette:
            diff = joueur.rect.right - scrolette
            joueur.rect.right = scrolette
            current_niveau.shift_monde(-diff)
            
        # changement de niveau et tout
        
        current_position = joueur.rect.x + current_niveau.monde_shift
        if current_position < current_niveau.niveau_limit:
            if current_niveau_no < len(niveau_list)-1:

                joueur.niveau_no +=1
                if current_niveau_no == 0:
                    joueur.boule_de_feu = 0
                    joueur.bourse = 0
                else:
                     achatmenu(joueur)
                current_niveau_no += 1
                joueur.rect.x = 120
                joueur.vie = 5
                joueur.bouclier = joueur.boucliermax
                current_niveau = niveau_list[current_niveau_no]
                joueur.niveau = current_niveau
                background_image = current_niveau.background
            else:
                achatmenu(joueur)
                joueur.rect.x = 100
                current_niveau = Niveau_01(joueur)
                joueur.niveau = current_niveau
                
            ecrannoiralpha = 255
            ecrannoir.fill(BLACK)
            nomniveau = font1.render(current_niveau.nom, WHITE)
            nomniveaupos = [400-nomniveau[1].width/2,300]
            ecrannoir.blit(nomniveau[0],nomniveaupos)
            

        # les dessins en dessous :

        
        screen.blit(background_image, background_position)
        current_niveau.draw(screen)     
        active_sprite_list.draw(screen)
        screen.blit(joueurAnim.image, [joueurAnim.rect.x,joueurAnim.rect.y])
        hud(joueur)
        
        #fondu imagé encore encore
        if ecrannoiralpha > 0:
            screen.blit(ecrannoir,[0,0])

        #
        
        clock.tick(60)

        # update de l'écran
        pygame.display.flip()
        if joueur.vie <= 0 : #rip
            fin = gameover(joueur)
            over = True
    if over:
        main(joueur.id)
    else:
        pygame.quit()

def gameover(joueur): #on revient au début du niveau
    done = False
    screen.fill(BLACK)
    text1 = font1.render("Les ninjas ont réussi...", WHITE)    
    text1pos=[400-text1[1].width/2,300]
    screen.blit(text1[0], text1pos)

    while not done :
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN: 
                done = True
                return True
        pygame.display.flip()
        

if __name__ == "__main__":
    main(None)
