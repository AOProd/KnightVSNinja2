import pygame

ECRAN_LARGEUR  = 800
ECRAN_HAUTEUR = 600
size = [ECRAN_LARGEUR, ECRAN_HAUTEUR]
screen = pygame.display.set_mode(size)
pygame.init()

cases=[[250,300,50,100],[500,560,20,75]]

def clic(pos):
    print(pos)
    for i in range(len(cases)):
        if pos[0] >= cases[i][0] and pos[0] <= cases[i][1] and pos[1] >= cases[i][2] and pos[1] <= cases[i][3]:
            print("moulger!!")
def achatmenu():

    background_position = [0, 0]
    background_image = pygame.image.load("art/fondachat.png").convert()
    done = False
    clock = pygame.time.Clock()
    while not done:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clic(pos)
        screen.blit(background_image, background_position)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    achatmenu()
