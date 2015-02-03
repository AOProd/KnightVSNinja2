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

def menu():
    global done
    font = pygame.font.Font(None, 36)
    screen.fill(BLACK)
    AOP_position = [190, 30]
    logoAOP = pygame.image.load("art/AOP.png").convert()
    screen.blit(logoAOP, AOP_position)
    text1 = font.render("Les productions Anti Otaku", True, WHITE)
    text1_x = 240
    text1_y = 460

    text2 = font.render("présentent", True, WHITE)
    text2_x = 330
    text2_y = 500

    screen.blit(text1, [text1_x, text1_y])
    screen.blit(text2, [text2_x, text2_y])
    pygame.display.flip()

    while pygame.time.get_ticks()<6000 and not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
        
    logo_position = [270, 50]
    logo = pygame.image.load("art/logo1.png")
    logo.set_colorkey(BLACK)

    background_position = [0,0]
    background = pygame.image.load("art/fondmenu.png").convert()

    text3 = font.render("ENTREE pour commencer", True, RED)
    text3_x = 200
    text3_y = 500

    screen.blit(background, background_position)
    screen.blit(logo, logo_position)
    screen.blit(text3, [text3_x, text3_y])

    pygame.display.flip()

    clic = False

    pygame.mixer.music.load('art/internationale.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

    while not clic and not done :
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    clic = True
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('art/musicmenu.ogg')
                pygame.mixer.music.play()
    menu.done = done
	
