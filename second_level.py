import pygame
import time

HEIGHT = 800
WIDTH = 1300
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
start_message = """Try to get to the green node (Vf), traversing through one of the two
                blue nodes, taking in consideration the fact that Vblue (V1 or V2) should
                respect Vblue = min {V1, V2}."""

def run(window):

    x_pos = 480
    y_pos = 580
    player_radius = 10

    finish_x_pos = 750
    finish_y_pos = 310
    finish_radius = 10

    image = pygame.image.load(r'level2.png')

    window.fill(WHITE)
    window.blit(image, (360, 150))
    pygame.display.update()
    
    font_style = pygame.font.SysFont(None, 30)
    def message(message, color, resistance, print_x, print_y):
        new_msg = message + str(resistance)
        msg = font_style.render(new_msg, True, color)
        window.blit(msg, [print_x, print_y])

    clock = pygame.time.Clock()

    def return_option():
        
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        ev = pygame.event.get()
        has_been_clicked = False

        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                has_been_clicked = True
        if has_been_clicked:
            if mouse_pos_x < 485 and mouse_pos_x > 325 and mouse_pos_y < 390 and  mouse_pos_y > 330:
                return 1
            elif mouse_pos_x < 955 and mouse_pos_x > 800 and mouse_pos_y < 390 and  mouse_pos_y > 330:
                return 2
        
        return 0

    game_on_progress = True
    selected = 0
    while game_on_progress:
    
        x_update = 0
        y_update = 0
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_on_progress = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_update = -10
                    y_update = 0
                elif event.key == pygame.K_RIGHT:
                    x_update = 10
                    y_update = 0
                elif event.key == pygame.K_UP:
                    x_update = 0
                    y_update = -10
                elif event.key == pygame.K_DOWN:
                    x_update = 0
                    y_update = 10

        x_pos += x_update
        y_pos += y_update
        
        out_of_bounds = 0
        if selected == 0 and ((x_pos < 480 or x_pos > finish_x_pos) or (y_pos != 580)):
            out_of_bounds = 1
            
        if selected == 0 and x_pos == finish_x_pos:
            selected = 1
            
        if selected == 1 and ((x_pos != finish_x_pos) or (y_pos > 580 or y_pos < 310)):
            out_of_bounds = 1
            
        if selected == 1 and y_pos == finish_y_pos:
            selected = 2
            
        if selected == 2:
            window.fill(WHITE)
            message("You have to answer the next question in order to escape the circuit", BLACK, "", 350, 400)
            pygame.display.update()
            time.sleep(5)
            
            
            image = pygame.image.load(r'level2_intrebare.png')
            window.fill(WHITE)
            window.blit(image, (280, 0))
            pygame.display.update()
            
            option = 0
            while not option:
                
                option = return_option()
                time.sleep(0.01)
                
            if option == 1:
                window.fill(WHITE)
                message("You Lose!", BLACK, "", 600, 400)
                pygame.display.update()
                time.sleep(3)
                return
            else:
                window.fill(WHITE)
                message("You escaped the circuit, good job!", BLACK, "", 480, 400)
                pygame.display.update()
                time.sleep(3)
                return
        
        
        if out_of_bounds:
            window.fill(WHITE)
            message("You Lose!", BLACK, "", 600, 400)
            pygame.display.update()
            time.sleep(3)
            return

        if selected != 2:
            window.fill(WHITE)
            window.blit(image, (280, 90))
            pygame.draw.circle(window, RED, [x_pos, y_pos], player_radius)
            pygame.draw.circle(window, GREEN, [finish_x_pos, finish_y_pos], finish_radius)
            message("= -4V", BLACK, "", 760, 280)
            pygame.display.update()
        
        clock.tick(20)

