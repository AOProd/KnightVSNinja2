import pygame
import math
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from intro import *
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
def clic(joueur,z):
    
    monnaie = True
    font = pygame.font.Font("police/freesansbold.ttf", 36)
    global done
    global boursen
    
    if cases[0][4] and joueur.sautup<5:
        if joueur.bourse-prix(joueur.sautup)>=0:
            joueur.sautage-=1
            joueur.bourse-=prix(joueur.sautup) 
            joueur.sautup+=1
        else:
            monnaie=False
    if cases[1][4] and joueur.asup<5:
        if joueur.bourse-prix(joueur.asup)>=0:
            joueur.vitesseattaque-=10
            joueur.bourse-=prix(joueur.asup)
            joueur.asup+=1
        else:
            monnaie=False
    if cases[2][4] and joueur.shieldup<5:
        if joueur.bourse-prix(joueur.shieldup)>=0:       
            joueur.boucliermax+=1
            joueur.bouclier=joueur.boucliermax
            joueur.bourse-=prix(joueur.shieldup)          
            joueur.shieldup+=1   
        else:
            monnaie=False
    if cases[3][4] and joueur.regup<5:
        if joueur.bourse-prix(joueur.regup)>=0:
            joueur.boucliercooldown-=20   
            joueur.bourse-=prix(joueur.regup)  
            joueur.regup+=1   
        else:
            monnaie=False
            
    if cases[4][4]:   
        done = True  
        
    if not monnaie:
        boursen=font.render("%s"%(joueur.bourse), True, RED)
    
    joueur.upstats()

def prix(produit):
    if produit==0:
        return 50
    elif produit==1:
        return 90
    elif produit==2:
        return 160
    elif produit==3:
        return 310
    elif produit==4:
        return 500
    elif produit==5:
        return "MAX"

        
def achatmenu(joueur):
    font = pygame.font.Font("police/freesansbold.ttf", 36)
    backpos = [0, 0]
    backimage = pygame.image.load("art/fondachat.png").convert()
    piece = pygame.image.load("art/piece.png")
    bourse = pygame.image.load("art/bourse.png")
    clock = pygame.time.Clock()
    global cases
    global done
    global boursen
    done = False
    
    while not done:
    
        pos = pygame.mouse.get_pos()
        boursen = font.render("%s"%(joueur.bourse), True, BLACK)
        
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
                    clic(joueur,boursen)
                    
        saut = font.render("%s"%(int(joueur.sautup)), True, BLACK)
        vitesse= font.render("%s"%(int(joueur.asup)), True, BLACK)
        bouclier= font.render("%s"%(int(joueur.shieldup)), True, BLACK)
        regen = font.render("%s"%(int(joueur.regup)), True, BLACK)        
        
        sautp = font.render("%s"%(prix(joueur.sautup)), True, BLACK)
        vitessep= font.render("%s"%(prix(joueur.asup)), True, BLACK)
        bouclierp= font.render("%s"%(prix(joueur.shieldup)), True, BLACK)
        regenp = font.render("%s"%(prix(joueur.regup)), True, BLACK)
        
        screen.blit(backimage, backpos)
        
        for i in range(len(cases)):
            screen.blit(cases[i][7], [cases[i][0],cases[i][2]])
                
        screen.blit(saut,[145,75])
        screen.blit(vitesse,[645,75])
        screen.blit(bouclier,[145,375])
        screen.blit(regen,[645,375])  
        
        screen.blit(sautp,[135,210])
        screen.blit(vitessep,[635,210])
        screen.blit(bouclierp,[135,510])
        screen.blit(regenp,[635,510])
        
        screen.blit(piece,[105,210])
        screen.blit(piece,[105,510])
        screen.blit(piece,[605,210])
        screen.blit(piece,[605,510])
        
        screen.blit(bourse,[350,10])
        screen.blit(boursen,[390,17])
        
        clock.tick(60)        
        pygame.display.flip()
    try:
        sauvegarde = open(joueur.fichier, "w")
        for i in range(len(joueur.stats)):
            for u in range(len(joueur.stats[i])):
                sauvegarde.write(str("%s\n"%(int(joueur.stats[i][u]))))
        sauvegarde.close()
    except IOError:
        print("o_O")


       
