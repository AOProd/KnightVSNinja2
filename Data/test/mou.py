import pygame
pygame.time.set_timer(5, 1000)
pygame.init()
while 1:
    for event in pygame.event.get():
        if event.type == 5:
            print("moulecon !")
