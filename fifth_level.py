import pygame
import time

from requests import options

HEIGHT = 800
WIDTH = 1300
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def add_positions():
    
    pos = []
    
        # ------------------- Intensity ------------------- #

    # first intensity
    first_int_x = 1000
    first_int_y = 80

    # second intensity
    second_int_x = 1000
    second_int_y = 120

    # third intensity
    third_int_x = 1000
    third_int_y = 160


    # ------------------- Voltages -------------------- #

    # first voltage
    first_volt_x = 1000
    first_volt_y = 280

    # second voltage
    second_volt_x = 1000
    second_volt_y = 360

    # third voltage
    third_volt_x = 1000
    third_volt_y = 440


    # ------------------- Resistors ------------------- #

    # first resistor
    first_res_x = 800
    first_res_y = 610

    # second resistor
    second_res_x = 1100
    second_res_y = 610

    # third resistor
    third_res_x = 950
    third_res_y = 700
    
    pos.append(first_int_x) 
    pos.append(first_int_y)
    pos.append(second_int_x)
    pos.append(second_int_y)
    pos.append(third_int_x)
    pos.append(third_int_y)
    
    pos.append(first_volt_x)
    pos.append(first_volt_y)
    pos.append(second_volt_x)
    pos.append(second_volt_y)
    pos.append(third_volt_x)
    pos.append(third_volt_y)
    
    pos.append(first_res_x)
    pos.append(first_res_y)
    pos.append(second_res_x)
    pos.append(second_res_y)
    pos.append(third_res_x)
    pos.append(third_res_y)
    
    return pos
    

def load_screen(window, pos):
    
    image = pygame.image.load(r'level5_main.png')
    window.fill(WHITE)
    window.blit(image, (170, 10))
    
    # pygame.draw.rect(window, RED, [460, 400, 115, 85], 2) # first resistor
    # pygame.draw.rect(window, RED, [660, 400, 115, 85], 2) # 2nd resistor
    # pygame.draw.rect(window, RED, [580, 190, 60, 70], 2) # voltage
    # pygame.draw.rect(window, RED, [575, 100, 75, 40], 2) # intensity
    
    
    image = pygame.image.load(r'first_intensity.png')
    window.blit(image, (pos[0], pos[1]))
    
    image = pygame.image.load(r'second_intensity.png')
    window.blit(image, (pos[2], pos[3]))
    
    image = pygame.image.load(r'third_intensity.png')
    window.blit(image, (pos[4], pos[5]))
    
    image = pygame.image.load(r'first_voltage.png')
    window.blit(image, (pos[6], pos[7]))
    
    image = pygame.image.load(r'second_voltage.png')
    window.blit(image, (pos[8], pos[9]))
    
    image = pygame.image.load(r'third_voltage.png')
    window.blit(image, (pos[10], pos[11]))
    
    image = pygame.image.load(r'first_resistor.png')
    window.blit(image, (pos[12], pos[13]))

    image = pygame.image.load(r'second_resistor.png')
    window.blit(image, (pos[14], pos[15]))
    
    image = pygame.image.load(r'third_resistor.png')
    window.blit(image, (pos[16], pos[17]))
    
    pygame.display.update()


def check_move(window, pos):

    has_been_clicked = False
    exit = 0
    drag = 0
    while True:
        ev = pygame.event.get()
        for event in ev:
           
            if event.type == pygame.MOUSEBUTTONUP and has_been_clicked:
                exit = 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                has_been_clicked = True
    
        if exit:
            break
    
        if has_been_clicked:
    
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

            # first intensity
            if (mouse_pos_x >= pos[0] and mouse_pos_x <= pos[0] + 75 \
            and mouse_pos_y >= pos[1] and  mouse_pos_y <= pos[1] + 35) or drag == 1:
                pos[0] = mouse_pos_x
                pos[1] = mouse_pos_y
                load_screen(window, pos)    
                drag = 1
                continue
            
            # second intensity
            if (mouse_pos_x >= pos[2] and mouse_pos_x <= pos[2] + 75 \
            and mouse_pos_y >= pos[3] and  mouse_pos_y <= pos[3] + 35 and drag == 0) or drag == 2:
                pos[2] = mouse_pos_x
                pos[3] = mouse_pos_y
                load_screen(window, pos)    
                drag = 2
                continue
            
            # third intensity
            if (mouse_pos_x >= pos[4] and mouse_pos_x <= pos[4] + 75 \
            and mouse_pos_y >= pos[5] and  mouse_pos_y <= pos[5] + 35 and drag == 0) or drag == 3:
                pos[4] = mouse_pos_x
                pos[5] = mouse_pos_y
                load_screen(window, pos)    
                drag = 3
                continue
            
            # first volt
            if (mouse_pos_x >= pos[6] and mouse_pos_x <= pos[6] + 70 \
            and mouse_pos_y >= pos[7] and  mouse_pos_y <= pos[7] + 60 and drag == 0) or drag == 4:
                pos[6] = mouse_pos_x
                pos[7] = mouse_pos_y
                load_screen(window, pos)    
                drag = 4
                continue
            
            # second volt
            if (mouse_pos_x >= pos[8] and mouse_pos_x <= pos[8] + 70 \
            and mouse_pos_y >= pos[9] and  mouse_pos_y <= pos[9] + 60 and drag == 0) or drag == 5:
                pos[8] = mouse_pos_x
                pos[9] = mouse_pos_y
                load_screen(window, pos)    
                drag = 5
                continue
            
            # third volt
            if (mouse_pos_x >= pos[10] and mouse_pos_x <= pos[10] + 70 \
            and mouse_pos_y >= pos[11] and  mouse_pos_y <= pos[11] + 60 and drag == 0) or drag == 6:
                pos[10] = mouse_pos_x
                pos[11] = mouse_pos_y
                load_screen(window, pos)    
                drag = 6
                continue
            
            # first res
            if (mouse_pos_x >= pos[12] and mouse_pos_x <= pos[12] + 115 \
            and mouse_pos_y >= pos[13] and  mouse_pos_y <= pos[13] + 85 and drag == 0) or drag == 7:
                pos[12] = mouse_pos_x
                pos[13] = mouse_pos_y
                load_screen(window, pos)    
                drag = 7
                continue

            # second res
            if (mouse_pos_x >= pos[14] and mouse_pos_x <= pos[14] + 115 \
            and mouse_pos_y >= pos[15] and  mouse_pos_y <= pos[15] + 85 and drag == 0) or drag == 8:
                pos[14] = mouse_pos_x
                pos[15] = mouse_pos_y
                load_screen(window, pos)    
                drag = 8
                continue
            
            # third res
            if (mouse_pos_x >= pos[16] and mouse_pos_x <= pos[16] + 115 \
            and mouse_pos_y >= pos[17] and  mouse_pos_y <= pos[17] + 85 and drag == 0) or drag == 9:
                pos[16] = mouse_pos_x
                pos[17] = mouse_pos_y
                load_screen(window, pos)    
                drag = 9
                
        if exit or has_been_clicked == False:
            break

    return 0

def run(window):
    
    font_style = pygame.font.SysFont(None, 50)
    def message(message, color, resistance, print_x, print_y):
        new_msg = message + str(resistance)
        msg = font_style.render(new_msg, True, color)
        window.blit(msg, [print_x, print_y])
    
    image = pygame.image.load(r'level5_start.png')
    window.fill(WHITE)
    window.blit(image, (170, 10))
    pygame.display.update()
    time.sleep(20)
    
    pos = add_positions()
    load_screen(window, pos)
    
    while True:
        check_move(window, pos)
        
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        ev = pygame.event.get()
        has_been_clicked = False
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                has_been_clicked = True
                break
        if has_been_clicked:
            if mouse_pos_x <= 720 and mouse_pos_x >= 530 and mouse_pos_y >= 735 and  mouse_pos_y <= 795:
                is_ok = 1
                if not (pos[6] >= 560 and pos[6] <= 660 and pos[7] >= 170 and pos[7] <= 280): #voltage
                   is_ok = 0
                   print("volt " + str(is_ok))
                if not (pos[0] >= 550 and pos[0] <= 670 and pos[1] >= 70 and pos[1] <= 170): #intensity
                    is_ok = 0
                    print("int " + str(is_ok))
                if not ((pos[14] >= 430 and pos[14] <= 590 and pos[15] >= 370 and pos[15] <= 520) or \
                    (pos[14] >= 630 and pos[14] <= 700 and pos[15] >= 370 and pos[15] <= 520)):
                    is_ok = 0
                    print("res1 " + str(is_ok))
                if not ((pos[16] >= 430 and pos[16] <= 590 and pos[17] >= 370 and pos[17] <= 520) or \
                    (pos[16] >= 630 and pos[16] <= 700 and pos[17] >= 370 and pos[17] <= 520)):
                    is_ok = 0
                    print("res2 " + str(is_ok))
                
                if is_ok:
                    window.fill(WHITE)
                    message("You solved the problem!", BLACK, "", 450, 400)
                    pygame.display.update()
                    time.sleep(2)
                    return
                else:
                    window.fill(WHITE)
                    message("You lost!", BLACK, "", 550, 400)
                    pygame.display.update()
                    time.sleep(2)
                    return
                