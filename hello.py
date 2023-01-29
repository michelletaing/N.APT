import pygame
import time
from pygame.locals import *

pygame.init()

# Set dimensions
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("nick's apartment")

# LOAD IMAGES & SET BOOLS
tv_view = pygame.image.load('assets/tv_view.png').convert_alpha()
tv_status = True

couch_view = pygame.image.load('assets/couch_view.png').convert_alpha()
couch_status = False

window_view = pygame.image.load('assets/window_view.png').convert_alpha()
window_status = False

kitchen_view = pygame.image.load('assets/kitchen_view.png').convert_alpha()
kitchen_status = False

hand = pygame.image.load('assets/HAND.png').convert_alpha()

# ARROWS
left_arrow_left = 80
left_arrow_right = 197
right_arrow_left = 1084
right_arrow_right = 1215
top = 340
bottom = 433

def toggle_view():
    if tv_status == True:
        window.blit(tv_view, (0,0))
    if couch_status == True:
        window.blit(couch_view, (0,0))
    if window_status == True:
        window.blit(window_view, (0,0))  
    if kitchen_status == True:
        window.blit(kitchen_view, (0,0)) 

def switch_screen(event):
    global tv_status
    global couch_status
    global kitchen_status
    global window_status

    if tv_status == True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if left_arrow_left <= mouse_pos[0] <= left_arrow_right and top <= mouse_pos[1] <= bottom:
                tv_status = False
                kitchen_status = True
            if right_arrow_left <= mouse_pos[0] <= right_arrow_right and top <= mouse_pos[1] <= bottom:
                tv_status = False
                window_status = True
    
    elif window_status == True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if left_arrow_left <= mouse_pos[0] <= left_arrow_right and top <= mouse_pos[1] <= bottom:
                window_status = False
                tv_status = True
            if right_arrow_left <= mouse_pos[0] <= right_arrow_right and top <= mouse_pos[1] <= bottom:
                window_status = False
                couch_status = True

    elif couch_status == True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if left_arrow_left <= mouse_pos[0] <= left_arrow_right and top <= mouse_pos[1] <= bottom:
                couch_status = False
                window_status = True
            if right_arrow_left <= mouse_pos[0] <= right_arrow_right and top <= mouse_pos[1] <= bottom:
                couch_status = False
                kitchen_status = True

    elif kitchen_status == True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if left_arrow_left <= mouse_pos[0] <= left_arrow_right and top <= mouse_pos[1] <= bottom:
                print("poop")
                kitchen_status = False
                couch_status = True
            if right_arrow_left <= mouse_pos[0] <= right_arrow_right and top <= mouse_pos[1] <= bottom:
                kitchen_status = False
                tv_status = True   
    
def render(event):
    switch_screen(event)
    toggle_view()
    window.blit(hand, (0,0))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            
            render(event)

    pygame.quit()

if __name__ == "__main__":
    main()