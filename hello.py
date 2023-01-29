import pygame
import time
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/amongus.mp3")
pygame.mixer.music.play()

# Set dimensions
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("N.APT")
clock = pygame.time.Clock()

# LOAD IMAGES & SET BOOLS
tv_view = pygame.image.load('assets/tv_view.png').convert_alpha()
tv_status = True

couch_view = pygame.image.load('assets/couch_view.png').convert_alpha()
couch_status = False

window_view = pygame.image.load('assets/window_view.png').convert_alpha()
window_status = False

kitchen_view = pygame.image.load('assets/kitchen_view.png').convert_alpha()
kitchen_status = False

text_menu = pygame.image.load('assets/text_menu.png').convert_alpha()
text_menu_status = False

space = pygame.image.load('assets/SPACE.png').convert_alpha()
space_status = False

hand = pygame.image.load('assets/HAND.png').convert_alpha()

keypad = pygame.image.load('assets/keypad.png').convert_alpha()
keypad_status = False

ending = pygame.image.load('assets/ending.png').convert_alpha()
ending_status = False
ending_text = "You have been in the unknown."

# FONT
Font = pygame.font.Font('assets/ComicSansMS3.ttf', 32)
text_box = Font.render(None, 1, (0, 0, 128))
display_text = ""
smallfont = pygame.font.SysFont('Corbel', 100)
color = (255,255,255)

# KEYPAD CALCULATION
code = ""
count = 0


# COORDINATES
# arrows
left_arrow_left = 80
left_arrow_right = 197
right_arrow_left = 1084
right_arrow_right = 1215
top = 340
bottom = 433

# intro text
display_text = "You wake up to a loud rumbling..."
text_menu_status = True

# air cond
air_coord = [0, 168, 474, 613]
air_text = "The noise must be coming from this..."

# space window
space_coord = [343, 1000, 38, 470]
space_text = "The sky is so clear tonight..."

# remy
remy_coord = [20, 210, 530, 685]
remy_text = "He seems hungry..."

# trash can
trash_coord = [865, 975, 375, 545]
trash_text = "I found a note in the trash that says \"1:7\""

# fridge note
fridge_coord = [995, 1052, 360, 430]
fridge_text = "A note was added to my fridge. It says \"2:4\""

# cat food
cat_coord = [34, 210, 450, 516]
cat_text = "There's a note in Remy's bowl that says \"3:0\""

# cabinet
cabinet_coord = [245, 570, 145, 300]
cabinet_text = "The cabinet has a note that says \"4:9\""

# tyler
tyler_coord = [614, 730, 182, 290]
tyler_text = "This album is pretty good..."

# microwave
microwave_coord = [950, 1080, 257, 330]
microwave_text = "I found a hotpocket in here!"

# tv
tv_coord = [350, 685, 80, 356]
tv_text = "This thing doesn't turn on..."

# nightstand
stand_coord = [286, 376, 407, 540]
stand_text = "I found a note that says \"Don't trust the cat\"..."

# keypad
keypad_coord = [805, 875, 283, 347]
clear_coord = [0, 375, 620, 720]
enter_coord = [800, 1270, 620, 720]
zero_coord = [366, 784, 620, 720]
one_coord = [0, 375, 472, 636]
two_coord = [377, 796, 456, 610]
three_coord = [800, 1270, 456, 610]
four_coord = [0, 375, 286, 460]
five_coord = [377, 796, 286, 460]
six_coord = [800, 1270, 286, 460]
seven_coord = [0, 375, 104, 285]
eight_coord = [377, 796, 104, 285]
nine_coord = [800, 1270, 104, 285]

def calculate(event):
    mouse = pygame.mouse.get_pos()
    print(mouse)
    global code
    global count
    global ending_status
    global keypad_status
    #if the mouse is clicked on the
    # button the game is terminated
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if clear_coord[0] <= mouse[0] <= clear_coord[1] and clear_coord[2] <= mouse[1] <= clear_coord[3]:  # X (or clear) button  ###
            code = ""
            count = 0
        if zero_coord[0] <= mouse[0] <= zero_coord[1] and zero_coord[2] <= mouse[1] <= zero_coord[3]:  # 0 button  ###
            code_inp = "0"
            code += code_inp
            count += 1
        if enter_coord[0] <= mouse[0] <= enter_coord[1] and enter_coord[2] <= mouse[1] <= enter_coord[3]:  # check mark (enter) button ###
            if code != "7409":  # change 1234 to desired code
                code = "wrong"
                display = smallfont.render(f"{code}", True, color)
                window.blit(display, (490, 20))
                pygame.display.update()
                time.sleep(1)
                count = 0
                code = ""
            elif code == "7409":
                code = "correct"
                display = smallfont.render(f"{code}", True, color)
                window.blit(display, (490, 20))
                pygame.display.update()
                ending_status = True
                keypad_status = False
            else:
                code = "wrong"
                display = smallfont.render(f"{code}", True, color)
                window.blit(display, (490, 20))
                pygame.display.update()
                time.sleep(1)
                code = ""
                count = 0
        if one_coord[0] <= mouse[0] <= one_coord[1] and one_coord[2] <= mouse[1] <= one_coord[3]:  # 1 button  ###
            print("hello")
            code_inp = "1"
            code += code_inp
            count += 1
        if two_coord[0] <= mouse[0] <= two_coord[1] and two_coord[2] <= mouse[1] <= two_coord[3]:  # 2 button  ###
            code_inp = "2"
            code += code_inp
            count += 1
        if three_coord[0] <= mouse[0] <= three_coord[1] and three_coord[2] <= mouse[1] <= three_coord[3]:  # 3 button  ###
            code_inp = "3"
            code += code_inp
            count += 1
        if four_coord[0] <= mouse[0] <= four_coord[1] and four_coord[2] <= mouse[1] <= four_coord[3]:  # 4 button  ###
            code_inp = "4"
            code += code_inp
            count += 1
        if five_coord[0] <= mouse[0] <= five_coord[1] and five_coord[2] <= mouse[1] <= five_coord[3]:  # 5 button  ###
            code_inp = "5"
            code += code_inp
            count += 1
        if six_coord[0] <= mouse[0] <= six_coord[1] and six_coord[2] <= mouse[1] <= six_coord[3]:  # 6 button  ###
            code_inp = "6"
            code += code_inp
            count += 1
        if seven_coord[0] <= mouse[0] <= seven_coord[1] and seven_coord[2] <= mouse[1] <= seven_coord[3]:  # 7 button  ###
            code_inp = "7"
            code += code_inp
            count += 1
        if eight_coord[0] <= mouse[0] <= eight_coord[1] and eight_coord[2] <= mouse[1] <= eight_coord[3]:  # 8 button  ###
            code_inp = "8"
            code += code_inp
            count += 1
        if nine_coord[0] <= mouse[0] <= nine_coord[1] and nine_coord[2] <= mouse[1] <= nine_coord[3]:  # 9 button  ###
            code_inp = "9"
            code += code_inp
            count += 1
        if count >= 4 and code != "7409" and code != "correct":  # change 1234 to desired code
            code = "wrong"
            display = smallfont.render(f"{code}", True, color)
            window.blit(display, (490, 20))
            pygame.display.update()
            time.sleep(1)
            count = 0
            code = ""
        display = smallfont.render(f"{code}", True, color)  ###
        window.blit(display, (490, 20))
        pygame.display.update()

def popups(event):
    global text_menu_status
    global display_text
    global space_status
    global keypad_status
    global text_box

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        # User clicks on the air conditioning in the couch view
        if (air_coord[0] <= mouse_pos[0] <= air_coord[1] and air_coord[2] <= mouse_pos[1] <= air_coord[3]) and couch_status:
            text_menu_status = True
            display_text = air_text
        # User clicks on the window
        if (space_coord[0] <= mouse_pos[0] <= space_coord[1] and space_coord[2] <= mouse_pos[1] <= space_coord[3]) and window_status:
            text_menu_status = True
            space_status = True
            display_text = space_text
        # Clicks on keypad
        if (keypad_coord[0] <= mouse_pos[0] <= keypad_coord[1] and keypad_coord[2] <= mouse_pos[1] <= keypad_coord[3]) and tv_status:
            keypad_status = True
            
        # Remy
        if (remy_coord[0] <= mouse_pos[0] <= remy_coord[1] and remy_coord[2] <= mouse_pos[1] <= remy_coord[3]) and tv_status:
            text_menu_status = True
            display_text = remy_text

        # Trash
        if (trash_coord[0] <= mouse_pos[0] <= trash_coord[1] and trash_coord[2] <= mouse_pos[1] <= trash_coord[3]) and couch_status:
            text_menu_status = True
            display_text = trash_text
        
        # Fridge
        if (fridge_coord[0] <= mouse_pos[0] <= fridge_coord[1] and fridge_coord[2] <= mouse_pos[1] <= fridge_coord[3]) and kitchen_status:
            text_menu_status = True
            display_text = fridge_text

        # Cat food
        if (cat_coord[0] <= mouse_pos[0] <= cat_coord[1] and cat_coord[2] <= mouse_pos[1] <= cat_coord[3]) and tv_status:
            text_menu_status = True
            display_text = cat_text

        # Cabinet
        if (cabinet_coord[0] <= mouse_pos[0] <= cabinet_coord[1] and cabinet_coord[2] <= mouse_pos[1] <= cabinet_coord[3]) and kitchen_status:
            text_menu_status = True
            display_text = cabinet_text
            
        # Tyler
        if (tyler_coord[0] <= mouse_pos[0] <= tyler_coord[1] and tyler_coord[2] <= mouse_pos[1] <= tyler_coord[3]) and couch_status:
            text_menu_status = True
            display_text = tyler_text

        # Microwave
        if (microwave_coord[0] <= mouse_pos[0] <= microwave_coord[1] and microwave_coord[2] <= mouse_pos[1] <= microwave_coord[3]) and kitchen_status:
            text_menu_status = True
            display_text = microwave_text

        # TV
        if (tv_coord[0] <= mouse_pos[0] <= tv_coord[1] and tv_coord[2] <= mouse_pos[1] <= tv_coord[3]) and tv_status:
            text_menu_status = True
            display_text = tv_text
        
        # Nightstand
        if (stand_coord[0] <= mouse_pos[0] <= stand_coord[1] and stand_coord[2] <= mouse_pos[1] <= stand_coord[3]) and couch_status:
            text_menu_status = True
            display_text = stand_text

        # Ending
        if ending_status == True:
            display_text = ending_text
            text_menu_status = True;

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            text_menu_status = False
            display_text = ""
            text_box = None
            space_status = False
            keypad_status = False

def toggle_view(event):
    global text_box
    global text_menu_status

    # Draw main rooms
    if tv_status == True:
        window.blit(tv_view, (0,0))
    if couch_status == True:
        window.blit(couch_view, (0,0))
    if window_status == True:
        window.blit(window_view, (0,0))  
    if kitchen_status == True:
        window.blit(kitchen_view, (0,0))
    
    # Popups
    if space_status == True:
        window.blit(space, (0,0))
    if ending_status == True:
        window.blit(ending, (0,0))
        
    # Hand needs to be drawn before the text box
    window.blit(hand, (0,0))

    # Text box
    if text_menu_status == True:
        window.blit(text_menu,(0,0))
        if text_box is not None:
            window.blit(text_box, (width / 4 - 30, height * 6 / 8))
        text_box = Font.render(display_text, 1, (0, 0, 128))
    if keypad_status == True:
        window.blit(keypad, (0,0))
        calculate(event) 
    

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
                kitchen_status = False
                couch_status = True
            if right_arrow_left <= mouse_pos[0] <= right_arrow_right and top <= mouse_pos[1] <= bottom:
                kitchen_status = False
                tv_status = True   
    
def render(event):
    switch_screen(event)
    toggle_view(event)
    popups(event)
    
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            
            render(event)

    clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()