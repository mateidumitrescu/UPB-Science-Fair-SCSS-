import pygame
import time

HEIGHT = 800
WIDTH = 1300
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def return_option(case):
        
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        ev = pygame.event.get()
        has_been_clicked = False
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                has_been_clicked = True
        if has_been_clicked:
            if case == 1:
                if mouse_pos_x <= 400 and mouse_pos_x >= 300 and mouse_pos_y >= 240 and  mouse_pos_y <= 300:
                    return 1
                elif mouse_pos_x <= 920 and mouse_pos_x >= 840 and mouse_pos_y >= 240 and  mouse_pos_y <= 300:
                    return 2
            if case == 2:
                if mouse_pos_x <= 500 and mouse_pos_x >= 390 and mouse_pos_y >= 220 and  mouse_pos_y <= 310:
                    return 2
                elif mouse_pos_x <= 990 and mouse_pos_x >= 770 and mouse_pos_y >= 240 and  mouse_pos_y <= 310:
                    return 1
            if case == 3:
                if mouse_pos_x <= 824 and mouse_pos_x >= 460 and mouse_pos_y >= 270 and  mouse_pos_y <= 320:
                    return 2
                elif mouse_pos_x <= 824 and mouse_pos_x >= 460 and mouse_pos_y >= 340 and  mouse_pos_y <= 395:
                    return 1
        return 0

def run(window):
    
    font_style = pygame.font.SysFont(None, 50)
    def message(message, color, resistance, print_x, print_y):
        new_msg = message + str(resistance)
        msg = font_style.render(new_msg, True, color)
        window.blit(msg, [print_x, print_y])
    
    x_pos = 350
    y_pos = 520
    player_radius = 10

    finish_x_pos = 930
    finish_y_pos = 520
    finish_radius = 10
    
    image = pygame.image.load(r'level3_first_traverse.png')
    window.fill(WHITE)
    window.blit(image, (250, 100))
    pygame.draw.circle(window, RED, [x_pos, y_pos], player_radius)
    pygame.draw.circle(window, GREEN, [finish_x_pos, finish_y_pos], finish_radius)
    pygame.display.update()

    time.sleep(5)
    
    # INSERT FIRST QUESTION
    
    image = pygame.image.load(r'level3_first_question.png')
    window.fill(WHITE)
    window.blit(image, (180, 100))
    pygame.display.update()
    
    option = 0
    while not option:
        
        option = return_option(1)
        time.sleep(0.1)
    
    if option == 1:
        window.fill(WHITE)
        message("Good choice!", BLACK, "", 550, 400)
        pygame.display.update()
        window.fill(WHITE)
        window.blit(image, (180, 100))
    elif option == 2:
        window.fill(WHITE)
        message("You lost!", BLACK, "", 550, 400)
        pygame.display.update()
        time.sleep(2)
        return
    
    time.sleep(2)
    
    # End first question
    
    image = pygame.image.load(r'level3_first_second_traverse.png')
    while x_pos < 610:
        x_pos += 10
        window.fill(WHITE)
        window.blit(image, (250, 240))
        pygame.draw.circle(window, RED, [x_pos, y_pos], player_radius)
        pygame.draw.circle(window, GREEN, [finish_x_pos, finish_y_pos], finish_radius)
        pygame.display.update()
        time.sleep(0.05)
        
    time.sleep(2)
    
    # INSERT Second QUESTION
    
    image = pygame.image.load(r'level3_second_question.png')
    window.fill(WHITE)
    window.blit(image, (350, 100))
    pygame.display.update()
    
    option = 0
    while not option:
        
        option = return_option(2)
        time.sleep(0.1)
    
    if option == 1:
        window.fill(WHITE)
        message("Good choice!", BLACK, "", 550, 400)
        pygame.display.update()
        window.fill(WHITE)
        window.blit(image, (180, 100))
    elif option == 2:
        window.fill(WHITE)
        message("You lost!", BLACK, "", 550, 400)
        pygame.display.update()
        time.sleep(2)
        return
    
    time.sleep(2)
    
    # End second question
    
    image = pygame.image.load(r'level3_second_traverse.png')
    while x_pos < 790:
        x_pos += 10
        window.fill(WHITE)
        window.blit(image, (250, 240))
        pygame.draw.circle(window, RED, [x_pos, y_pos], player_radius)
        pygame.draw.circle(window, GREEN, [finish_x_pos, finish_y_pos], finish_radius)
        pygame.display.update()
        time.sleep(0.05)
        
    time.sleep(2)
    
    # INSERT THIRD QUESTION
    
    image = pygame.image.load(r'level3_third_question.png')
    window.fill(WHITE)
    window.blit(image, (250, 100))
    pygame.display.update()
    
    option = 0
    while not option:
        
        option = return_option(3)
        time.sleep(0.1)
    
    if option == 1:
        window.fill(WHITE)
        message("Good choice!", BLACK, "", 550, 400)
        pygame.display.update()
        window.fill(WHITE)
        window.blit(image, (180, 100))
    elif option == 2:
        window.fill(WHITE)
        message("You lost!", BLACK, "", 550, 400)
        pygame.display.update()
        time.sleep(2)
        return
    
    time.sleep(2)
    
    # End third question
    
    image = pygame.image.load(r'final_traverse.png')
    while x_pos < 930:
        x_pos += 10
        window.fill(WHITE)
        window.blit(image, (250, 240))
        pygame.draw.circle(window, RED, [x_pos, y_pos], player_radius)
        pygame.draw.circle(window, GREEN, [finish_x_pos, finish_y_pos], finish_radius)
        pygame.display.update()
        time.sleep(0.05)
        
    window.fill(WHITE)
    message("You escaped the circuit, good job!", BLACK, "", 350, 400)
    pygame.display.update()
    time.sleep(3)
    
    return
        
    