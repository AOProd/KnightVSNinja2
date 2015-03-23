import pygame
import os
import pygame.freetype
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from sauvegarde import *
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


fin = False
pygame.freetype.init()
font1 = pygame.freetype.Font("police/shanghai.ttf", 36)
font2 = pygame.freetype.Font("police/OldLondon.ttf", 36)


def intro():

    screen.fill(BLACK)

    logoAOP = pygame.image.load("art/AOP.png")
    logorect=logoAOP.get_rect()
    AOP_position = [400-logorect.width/2, 30]
    screen.blit(logoAOP, AOP_position)
    
    text1 = font1.render("Les productions Anti Otaku", WHITE)
    text2 = font1.render("présentent", WHITE)
    text1pos=[400-text1[1].width/2,460]
    text2pos=[400-text2[1].width/2,500]

    screen.blit(text1[0], text1pos)
    screen.blit(text2[0], text2pos)
    
    pygame.display.flip()
    

    while pygame.time.get_ticks()<1000:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                    pygame.quit()
                    
    antiotaku = pygame.mixer.Sound('art/antiotaku.wav')
    antiotaku.play()
    
    while pygame.time.get_ticks()<6000:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                    pygame.quit()
                    
    logo = pygame.image.load("art/logo1.png")
    logorect = logo.get_rect()
    logo_position = [400-logorect.width/2, 50]
    logo.set_colorkey(BLACK)

    background_position = [0,0]
    background = pygame.image.load("art/fondmenu.png")
   
    global saveid

    global ph
    global cpos
    global flechepos 

    


    fleche = pygame.image.load("art/flecheselec.png")
    flechepos = [200,400]

    cpos = 1
    ph = 0
    
    pygame.mixer.music.load('art/internationale.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    ttitre = font2.render("Knight VS Ninja 2 - Alpha 0.0.1", WHITE)
    tjouer = font2.render("Jouer", WHITE)
    tcredit = font2.render("Crédits", WHITE)   
    tnew = font2.render("Nouvelle partie", WHITE)
    tload = font2.render("Charger une partie", WHITE)
    tkau = font2.render("Kaukau34", WHITE)
    tpiou = font2.render("Pioulamenace", WHITE)
    tecrase = font2.render("Écraser la sauvegarde ?", WHITE)
    toui = font2.render("Oui", WHITE)   
    tnon = font2.render("Non", WHITE)
    tsave1 = font2.render("Sauvegarde 1", WHITE)
    tsave2 = font2.render("Sauvegarde 2", WHITE)
    tretour = font2.render("Retour", WHITE)
    
    titrepos=[400-ttitre[1].width/2,300]
    jouerpos=[400-tjouer[1].width/2,400]
    creditpos=[400-tcredit[1].width/2,500]       
    newpos=[400-tnew[1].width/2,300]       
    loadpos=[400-tload[1].width/2,400]    
    kaupos=[400-tkau[1].width/2,400]    
    pioupos=[400-tpiou[1].width/2,500]        
    ecrasepos=[400-tecrase[1].width/2,300]       
    ouipos=[400-toui[1].width/2,400]              
    nonpos=[400-tnon[1].width/2,500]     
    save1pos=[400-tsave1[1].width/2,300]     
    save2pos=[400-tsave2[1].width/2,400]     
    retourpos=[400-tretour[1].width/2,500]     

    
    while not fin :
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    clic(cpos, ph)
                if event.key == pygame.K_UP:
                    flechepos=selection(cpos, ph, 0)
                if event.key == pygame.K_DOWN:   
                    flechepos=selection(cpos, ph, 1)
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load("art/internationale.mp3")
                pygame.mixer.music.play()
                
        screen.blit(background, background_position)
        screen.blit(logo, logo_position)     
        
        if ph == 0:
            screen.blit(ttitre[0], titrepos)                
            screen.blit(tjouer[0], jouerpos)                
            screen.blit(tcredit[0], creditpos)  
        elif ph == 1:
            screen.blit(tnew[0], newpos)                
            screen.blit(tload[0], loadpos)  
            screen.blit(tretour[0], retourpos)                        
        elif ph == 2:
            screen.blit(ttitre[0], titrepos)                
            screen.blit(tkau[0], kaupos)                
            screen.blit(tpiou[0], pioupos)  
        elif ph == 3:
            screen.blit(tsave1[0], save1pos)                
            screen.blit(tsave2[0], save2pos)   
            screen.blit(tretour[0], retourpos)                
             
        elif ph == 4:
            screen.blit(tecrase[0], ecrasepos)                
            screen.blit(toui[0], ouipos)                
            screen.blit(tnon[0], nonpos)          
        elif ph == 5:
            screen.blit(tretour[0], retourpos)                
            screen.blit(tsave1[0], save1pos)                
            screen.blit(tsave2[0], save2pos)           

              
        screen.blit(fleche, flechepos)                
        pygame.display.flip()
    return saveid

def selection(pos, phase, direction):

    global cpos
    
    if phase in [0, 2, 4]:
        if pos == 1:
            pos=2
        else:
            pos=1

    elif phase in [1, 3, 5]:
        if direction == 0:
            pos-=1
        else:
            pos+=1
        if pos < 0:
            pos=2
        elif pos > 2:
            pos= 0  
    cpos = pos
    x = 200
    y = pos*100+300        
    return [x,y]
    
def clic(pos, phase): #bas en haut, phase : 0 = premier choix, 1 = selection sauvegarde, 2 = crédits, 3 = confirmade
    
    global fin
    global cpos
    global ph
    global saveid
    global flechepos
    
    if phase == 0 :
        if pos == 1:
            ph = 1            
        elif pos == 2:
            ph = 2
            print("zz")
    
    elif phase == 1:
        if pos == 0:
            if savecheck()<=1:
                saveid = savecheck()
                fin = True
            else :
                ph = 4
                cpos = 1 
                flechepos = [200,400]
        elif pos == 1:
            ph = 3
        else:
            ph = 0
            
    elif phase == 2:
        ph = 0
        
    elif phase == 3:
        if pos == 0:
            saveid = 0
            fin = True        
        elif pos == 1:
            saveid = 1
            fin = True
        else:
            ph = 0
            
    elif phase == 4:
        if pos == 1:
            ph=5
        elif pos == 2:
            ph=1
            
    elif phase == 5:

        if pos == 0:
            try:
                os.remove("sauvegardes/save0.txt")
                saveid = 0
                fin = True 
            except FileNotFoundError:
                saveid = 0
                fin = True     
        elif pos == 1:
            try:
                os.remove("sauvegardes/save1.txt")
                saveid = 1
                fin = True 
            except FileNotFoundError:
                saveid = 1
                fin = True                 
        elif pos == 2:
            ph = 0   
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    