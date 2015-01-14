import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        
        self.i = 0
        self.image = pygame.image.load('0.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 584 - self.rect.height
        clock = pygame.time.Clock()

    def update(self):
        
        self.i = self.i + 1
        if self.i == 1:    
            self.image = pygame.image.load('1.png')
        elif self.i == 2:
            self.image = pygame.image.load('2.png')
        elif self.i == 3:
            self.image = pygame.image.load('3.png')
            self.i = 0
        clock.tick(20)

        
    

class Sol1(pygame.sprite.Sprite):

    def __init__(self):


        self.image = pygame.image.load('sol.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 590
        
    def update(self):

        self.rect.x =  self.rect.x - 2

class Sol2(pygame.sprite.Sprite):

    def __init__(self):


        self.image = pygame.image.load('sol.png')
        self.rect = self.image.get_rect()
        self.rect.x = 796
        self.rect.y = 590
        
    def update(self):

        self.rect.x =  self.rect.x - 2
        
        


background = pygame.image.load('background.png')

sol1 = Sol1()
sol2 = Sol2()

player = Player()

screen = pygame.display.set_mode((1200,800))

screen_rect = screen.get_rect()

clock = pygame.time.Clock()

while 1 :

    
    screen.blit(background,screen_rect)
    screen.blit(sol1.image,(sol1.rect.x,sol1.rect.y))
    screen.blit(sol2.image,(sol2.rect.x,sol2.rect.y))
    screen.blit(player.image,(player.rect.x,player.rect.y))
    player.update()
    sol1.update()
    sol2.update()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()


    
