import pygame
from pygame.locals import *

pygame.init()

# Set dimensions
width, height = 1280, 720
window = pygame.display.set_mode((width, height))

# Set images
thumbnail_nick = pygame.image.load('assets/thumbnail_nick.png').convert()
thumbnail_nick = pygame.transform.scale(thumbnail_nick, (width,height))

test_obj = pygame.image.load('assets/drawer.png').convert()
test_obj = pygame.transform.scale(test_obj, (163,150))
test_rect = test_obj.get_rect()

def draw_window():
    window.blit(thumbnail_nick, (0, 0))
    window.blit(test_obj, (293, 405))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        mouse_pos = pygame.mouse.get_pos()
        
        if pygame.mouse.get_pressed()[0]:
            print(mouse_pos)
            if (test_rect.collidepoint(mouse_pos)):
                print("bruh")

        draw_window()
        
    pygame.quit()

if __name__ == "__main__":
    main()