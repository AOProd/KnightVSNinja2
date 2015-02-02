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

cases=[[100,200,100,200,False,pygame.image.load("art/saut.png"),pygame.image.load("art/sauth.png"),""],#saut
       [600,700,100,200,False,pygame.image.load("art/epee.png"),pygame.image.load("art/epeeh.png"),""],#vitesse d'attaque
       [100,200,400,500,False,pygame.image.load("art/bouclier.png"),pygame.image.load("art/bouclierh.png"),""],#bouclier max
       [600,700,400,500,False,pygame.image.load("art/rbouclier.png"),pygame.image.load("art/rbouclierh.png"),""],#regen bouclier
       [350,450,250,350,False,pygame.image.load("art/nsuivant.png"),pygame.image.load("art/nsuivanth.png"),""],#next
       ]
done = False

def clic(pos,joueur):
    font = pygame.font.Font(None, 36)
    global done
    if cases[0][4] and joueur.sautage > -25:
        joueur.sautage-=1
    if cases[1][4] and joueur.vitesseattaque > 10:
        joueur.vitesseattaque-=10  
    if cases[2][4] and joueur.boucliermax < 6:
        joueur.boucliermax+=1
        joueur.bouclier=joueur.boucliermax
        print("mou")
    if cases[3][4] and joueur.boucliercooldown > 100:
        joueur.boucliercooldown-=20          
    if cases[4][4]:
        done = True
def achatmenu(joueur):
    font = pygame.font.Font(None, 36)
    backpos = [0, 0]
    backimage = pygame.image.load("art/fondachat.png").convert()
    clock = pygame.time.Clock()
    global cases
    global done
    done = False
    saut="%s"%(int(-(joueur.sautage+20)/2))
    text1 = font.render(saut, True, WHITE)
    
    while not done:
        pos = pygame.mouse.get_pos()
    
        for i in range(len(cases)):
            cases[i][4]=False
            cases[i][7]=cases[i][5]
            if pos[0] >= cases[i][0] and pos[0] <= cases[i][1] and pos[1] >= cases[i][2] and pos[1] <= cases[i][3]:
                cases[i][4]=True
                cases[i][7]=cases[i][6]
                
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clic(pos,joueur)
                    
        saut="%s"%(int(-(joueur.sautage+20)))
        sauterie = font.render(saut, True, WHITE)
        atspeed="%s"%(int(-(joueur.vitesseattaque-60)/10))
        vitesse= font.render(atspeed, True, BLACK)
        boucl="%s"%(int(joueur.boucliermax-1))
        bouclier= font.render(boucl, True, BLACK)
        bregen="%s"%(int((-joueur.boucliercooldown+200)/20))
        regen = font.render(bregen, True, BLACK)
        
        screen.blit(backimage, backpos)
        
        for i in range(len(cases)):
            screen.blit(cases[i][7], [cases[i][0],cases[i][2]])
            
        screen.blit(font.render("Niveau suivant", True, BLACK),[310,350])     
        screen.blit(sauterie,[145,75])
        screen.blit(vitesse,[645,75])
        screen.blit(bouclier,[145,375])
        screen.blit(regen,[645,375])
        
        clock.tick(60)        
        pygame.display.flip()
        


       
