import pygame
import time
from pygame.locals import *

pygame.init()

# Set dimensions
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("nick's apartment")

# SET IMAGES
# arrows
arrow_left = pygame.image.load(f'assets/arrow_left.png').convert_alpha()
left_rect = arrow_left.get_rect()
left_rect.topleft = (83,87)

arrow_right = pygame.image.load(f'assets/arrow_right.png').convert_alpha()
right_rect = arrow_right.get_rect()
right_rect.topleft = (1089, 343)

# initialize views lists and load tv_view images
tv_view = []
for i in range(1,11):
    tv_view.append(pygame.image.load(f'assets/tv_view/{i}.png').convert_alpha())

couch_view = []
#or i in range(1,13):
    #couch_view.append(pygame.image.load(f'assets/couch_view/{i}.png').convert_alpha()) 

window_view = []
#for i in range(1,6):
    #window_view.append(pygame.image.load(f'assets/window_view/{i}.png').convert_alpha()) 

kitchen_view = []
#for i in range(1,10):
    #couch_view.append(pygame.image.load(f'assets/kitchen_view/{i}.png').convert_alpha()) 

def toggle_view(images, turnOn):
    window.fill((0,0,0))
    if turnOn:
        for i in range(len(images)):
            if images[i] is not None:
                window.blit(images[i], (0,0))
    if not turnOn:
        for i in range(len(images)):
            images[i] = None       

def switch_views(event):
    if window_view is not None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if left_rect.collidepoint(mouse_pos):
                toggle_view(window_view, False)
                # Reload the images
                for i in range(1,11):
                    tv_view.append(pygame.image.load(f'assets/tv_view/{i}.png').convert_alpha()) 
                toggle_view(tv_view, True)
            if right_rect.collidepoint(mouse_pos):
                toggle_view(window_view, False)
                for i in range(1,13):
                    couch_view.append(pygame.image.load(f'assets/couch_view/{i}.png').convert_alpha()) 
                toggle_view(couch_view, True)
    
    if tv_view is not None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if left_rect.collidepoint(mouse_pos):
                toggle_view(tv_view, False)
                for i in range(1,10):
                    couch_view.append(pygame.image.load(f'assets/kitchen_view/{i}.png').convert_alpha()) 
                toggle_view(kitchen_view, True)
            if right_rect.collidepoint(mouse_pos):
                toggle_view(tv_view, False)
                for i in range(1,6):
                    window_view.append(pygame.image.load(f'assets/window_view/{i}.png').convert_alpha()) 
                toggle_view(window_view, True)
    
    if couch_view is not None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if left_rect.collidepoint(mouse_pos):
                toggle_view(couch_view, False)
                for i in range(1,6):
                    window_view.append(pygame.image.load(f'assets/window_view/{i}.png').convert_alpha()) 
                toggle_view(window_view, True)
            if right_rect.collidepoint(mouse_pos):
                toggle_view(couch_view, False)
                for i in range(1,10):
                    couch_view.append(pygame.image.load(f'assets/kitchen_view/{i}.png').convert_alpha()) 
                toggle_view(kitchen_view, True)


    if kitchen_view is not None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if left_rect.collidepoint(mouse_pos):
                toggle_view(kitchen_view, False)
                for i in range(1,13):
                    couch_view.append(pygame.image.load(f'assets/couch_view/{i}.png').convert_alpha()) 
                toggle_view(couch_view, True)
            elif right_rect.collidepoint(mouse_pos):
                toggle_view(kitchen_view, False)
                for i in range(1,11):
                    tv_view.append(pygame.image.load(f'assets/tv_view/{i}.png').convert_alpha()) 
                toggle_view(tv_view, True)
    
    pygame.display.flip()


def render():
    for image in tv_view:
        if image is not None:
            window.blit(image, (0,0))
    
    window.blit(arrow_left, (0,0))
    window.blit(arrow_right, (0,0))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            
            switch_views(event)

        render()

    pygame.quit()

if __name__ == "__main__":
    main()