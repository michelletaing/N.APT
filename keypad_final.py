import pygame
import time


iteration_var = 0
code = ""
count = 0  
color = (255,255,255)
smallfont = pygame.font.SysFont('Corbel',35)
display = smallfont.render(f"{code}", True, color)
## under the while loop
while True:  ### remove this and put the rest under actual while loop
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if 430 <= mouse[0] <= 470 and 440 <= mouse[1] <= 480:  # X (or clear) button  ###
                code = ""
                count = 0
            if 480 <= mouse[0] <= 520 and 440 <= mouse[1] <= 480:  # 0 button  ###
                code_inp = "0"
                code += code_inp
                count += 1
            if 530 <= mouse[0] <= 570 and 440 <= mouse[1] <= 480:  # check mark (enter) button ###
                if code != "1234":  # change 1234 to desired code
                    code = "wrong"
                    display = smallfont.render(f"{code}", True, color)
                    window.blit(display, (490, 250))
                    pygame.display.update()
                    time.sleep(1)
                    count = 0
                    code = ""
                elif code == "1234":
                    code = "correct"
                else:
                    code = "wrong"
                    display = smallfont.render(f"{code}", True, color)
                    window.blit(display, (490, 250))
                    pygame.display.update()
                    time.sleep(1)
                    code = ""
                    count = 0
            if 430 <= mouse[0] <= 470 and 390 <= mouse[1] <= 430:  # 1 button  ###
                code_inp = "1"
                code += code_inp
                count += 1
            if 480 <= mouse[0] <= 520 and 390 <= mouse[1] <= 430:  # 2 button  ###
                code_inp = "2"
                code += code_inp
                count += 1
            if 530 <= mouse[0] <= 570 and 390 <= mouse[1] <= 430:  # 3 button  ###
                code_inp = "3"
                code += code_inp
                count += 1
            if 430 <= mouse[0] <= 470 and 340 <= mouse[1] <= 380:  # 4 button  ###
                code_inp = "4"
                code += code_inp
                count += 1
            if 480 <= mouse[0] <= 520 and 340 <= mouse[1] <= 380:  # 5 button  ###
                code_inp = "5"
                code += code_inp
                count += 1
            if 530 <= mouse[0] <= 570 and 340 <= mouse[1] <= 380:  # 6 button  ###
                code_inp = "6"
                code += code_inp
                count += 1
            if 430 <= mouse[0] <= 470 and 290 <= mouse[1] <= 330:  # 7 button  ###
                code_inp = "7"
                code += code_inp
                count += 1
            if 480 <= mouse[0] <= 520 and 290 <= mouse[1] <= 330:  # 8 button  ###
                code_inp = "8"
                code += code_inp
                count += 1
            if 530 <= mouse[0] <= 570 and 290 <= mouse[1] <= 330:  # 9 button  ###
                code_inp = "9"
                code += code_inp
                count += 1
            if count >= 4 and code != "1234" and code != "correct":  # change 1234 to desired code
                code = "wrong"
                display = smallfont.render(f"{code}", True, color)
                window.blit(display, (490, 250))
                pygame.display.update()
                time.sleep(1)
                count = 0
                code = ""
            display = smallfont.render(f"{code}", True, color)  ###
    mouse = pygame.mouse.get_pos()
    window.blit(display, (490, 250))  ### NEED WINDOW VARIABLE
    pygame.display.update()
