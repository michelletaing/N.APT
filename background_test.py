import pygame
from pygame.locals import *
pygame.init()
width, height = 1920, 1080
window = pygame.display.set_mode((width, height))
background_img = pygame.image.load('Screenshot 2023-01-27 at 11.57.06 PM.png')
background_img = pygame.transform.scale(background_img, (width,height))
runing = True
while runing:
    window.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()