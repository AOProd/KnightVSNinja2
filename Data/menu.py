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
	font = pygame.font.Font(None, 36)
	screen.fill(BLACK)
	AOP_position = [190, 30]
	logoAOP = pygame.image.load("art/AOP.png").convert()
	screen.blit(logoAOP, AOP_position)
	text1 = font.render("Les productions Anti Otaku", True, WHITE)
	text2 = font.render("présentent", True, WHITE)
	text1_x = 240
	text1_y = 460
	text2_x = 330
	text2_y = 500

	screen.blit(text1, [text1_x, text1_y])
	screen.blit(text2, [text2_x, text2_y])
	pygame.display.flip()
	while pygame.time.get_ticks()<6000 :
		None

	
