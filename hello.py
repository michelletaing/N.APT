import pygame
from pygame.locals import *

pygame.init()

# Set dimensions
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("nick's apartment")

# SET IMAGES
bg = pygame.image.load('assets/BACKGROUND.png').convert_alpha()
air = pygame.image.load('assets/air.png').convert_alpha()
cabinet = pygame.image.load('assets/cabinet.png').convert_alpha()
couch = pygame.image.load('assets/couch.png').convert_alpha()
kitchen = pygame.image.load('assets/kitchen.png').convert_alpha()
lamp = pygame.image.load('assets/lamp.png').convert_alpha()
poster = pygame.image.load('assets/poster.png').convert_alpha()
small_table = pygame.image.load('assets/small_table.png').convert_alpha()
table = pygame.image.load('assets/table.png').convert_alpha()
trash = pygame.image.load('assets/trash.png').convert_alpha()
window_drawing = pygame.image.load('assets/window.png').convert_alpha()
gradient = pygame.image.load('assets/gradient.png').convert_alpha()

# SET RECT BOUNDS
air_rect = air.get_rect();
air_rect.topleft = (10, 517)

def render():
    window.blit(bg, (0,0))
    window.blit(air, (0,0))
    window.blit(cabinet, (0,0))
    window.blit(couch, (0,0))
    window.blit(kitchen, (0,0))
    window.blit(lamp, (0,0))
    window.blit(poster, (0,0))
    window.blit(small_table, (0,0))
    window.blit(table, (0,0))
    window.blit(trash, (0,0))
    window.blit(window_drawing, (0,0))
    window.blit(gradient, (0,0))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if (air_rect.collidepoint(mouse_pos)):
                print("bruh")

        render()
        
    pygame.quit()

if __name__ == "__main__":
    main()