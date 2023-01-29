import pygame
import sys
  
  
# initializing the constructor
pygame.init() 
  
while True:
    

    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
                  
    # stores the (x,y) coordinates into
    # the variable as a tuple (needed to define the button)
    mouse = pygame.mouse.get_pos()
      

      
    # updates the frames of the game
    pygame.display.update()