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
            if case == 0 and mouse_pos_x <= 690 and mouse_pos_x >= 580 and mouse_pos_y >= 695 and  mouse_pos_y <= 745:
                return 1
            if case == 1:
                # pygame.draw.rect(window, RED, [430, 135, 90, 55], 2)
                # pygame.draw.rect(window, RED, [755, 135, 90, 55], 2)
                if mouse_pos_x <= 520 and mouse_pos_x >= 430 and mouse_pos_y >= 135 and  mouse_pos_y <= 190:
                    return 1
                elif mouse_pos_x <= 845 and mouse_pos_x >= 755 and mouse_pos_y >= 135 and  mouse_pos_y <= 190:
                    return 2
            if case == 2:
                # pygame.draw.rect(window, RED, [410, 135, 125, 70], 2)
                # pygame.draw.rect(window, RED, [735, 135, 125, 70], 2)
                if mouse_pos_x <= 545 and mouse_pos_x >= 410 and mouse_pos_y >= 135 and  mouse_pos_y <= 205:
                    return 1
                elif mouse_pos_x <= 860 and mouse_pos_x >= 735 and mouse_pos_y >= 135 and  mouse_pos_y <= 205:
                    return 2
            if case == 3:
            # pygame.draw.rect(window, RED, [410, 145, 180, 80], 2)
            # pygame.draw.rect(window, RED, [680, 145, 180, 80], 2)
                if mouse_pos_x <= 590 and mouse_pos_x >= 410 and mouse_pos_y >= 145 and  mouse_pos_y <= 225:
                    return 2
                elif mouse_pos_x <= 860 and mouse_pos_x >= 680 and mouse_pos_y >= 145 and  mouse_pos_y <= 225:
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

    finish_x_pos = 380
    finish_y_pos = 480
    finish_radius = 10
    
    # Description
    
    image = pygame.image.load(r'level4_start.png')
    window.fill(WHITE)
    window.blit(image, (170, 50))
    pygame.display.update()
    
    time.sleep(10)
    
    # End of Description
    
    # Presentation
    
    image = pygame.image.load(r'level4_present.png')
    window.fill(WHITE)
    window.blit(image, (140, 0))
    pygame.display.update()
    
    option = 0
    while not option:
        
        option = return_option(0)
        time.sleep(0.1)
    
    # Presentation
    
    # First Question
    
    image = pygame.image.load(r'level4_first_question.png')
    window.fill(WHITE)
    window.blit(image, (180, -50))
    pygame.draw.circle(window, RED, [880, 480], player_radius)
    pygame.draw.circle(window, GREEN, [finish_x_pos, finish_y_pos], finish_radius)
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
    
    # Second Question
    
    image = pygame.image.load(r'level4_second_question.png')
    window.fill(WHITE)
    window.blit(image, (180, -50))
    pygame.draw.circle(window, RED, [700, 330], player_radius)
    pygame.draw.circle(window, GREEN, [finish_x_pos, finish_y_pos], finish_radius)
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
    
    # End Second Question
    
    # Third Question
    
    image = pygame.image.load(r'level4_third_question.png')
    window.fill(WHITE)
    window.blit(image, (180, -50))
    pygame.draw.circle(window, RED, [400, 330], player_radius)
    pygame.draw.circle(window, GREEN, [finish_x_pos, finish_y_pos], finish_radius)
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
    
    # End of third question
    
    window.fill(WHITE)
    message("You escaped the circuit, good job!", BLACK, "", 350, 400)
    pygame.display.update()
    time.sleep(3)
    
    return