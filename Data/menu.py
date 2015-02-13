import pygame
import pygame.freetype
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

def menu():
    pygame.freetype.init()
    font1 = pygame.freetype.Font("police/shanghai.ttf", 36)
    font2 = pygame.freetype.Font("police/OldLondon.ttf", 36)
    
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

    text3 = font2.render("ENTREE pour commencer", RED)
    text3pos=[400-text3[1].width/2,500]

    screen.blit(background, background_position)
    screen.blit(logo, logo_position)
    screen.blit(text3[0], text3pos)

    pygame.display.flip()

    clic = False

    pygame.mixer.music.load('art/internationale.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

    while not clic :
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    clic = True
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load("art/internationale.mp3")
                pygame.mixer.music.play()
	
