import pygame
import time

HEIGHT = 800
WIDTH = 1300
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
start_message = "Your intensity acceptance in this area is "

def run(window):

    image = pygame.image.load(r'first_level_start.png')

    window.fill(WHITE)
    window.blit(image, (160, 150))
    pygame.display.update()
    
    time.sleep(15)

    x_pos = 820
    y_pos = 450
    player_radius = 10

    finish_x_pos = 440
    finish_y_pos = 270
    finish_radius = 10

    # first represents the selection / the part of exercice / image
    x_range_of_movement = [(0, 450)]
    y_range_of_movement = [(1, 500)]
    x_bounds = [(0, 820)]
    y_bounds = [(1, 1000)]

    image = pygame.image.load(r'first.png')

    window.fill(WHITE)
    window.blit(image, (360, 150))
    pygame.display.update()

    clock = pygame.time.Clock()

    font_style = pygame.font.SysFont(None, 50)
    def message(message, color, resistance, print_x, print_y):
        new_msg = message + str(resistance)
        msg = font_style.render(new_msg, True, color)
        window.blit(msg, [print_x, print_y])

    acceptances = ["2A","3A"]
    index = 0

    def return_option():
        
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        ev = pygame.event.get()
        has_been_clicked = False
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                has_been_clicked = True
        if has_been_clicked:
            if mouse_pos_x < WIDTH // 2:
                return 1
            else:
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
                    x_update = -20
                    y_update = 0
                elif event.key == pygame.K_RIGHT:
                    x_update = 20
                    y_update = 0
                elif event.key == pygame.K_UP:
                    x_update = 0
                    y_update = -20
                elif event.key == pygame.K_DOWN:
                    x_update = 0
                    y_update = 20

        x_pos += x_update
        y_pos += y_update
        
        out_of_bonds = 0
        if x_update and (selected, y_pos) not in x_range_of_movement or (selected == x_bounds[0][0] and x_pos > x_bounds[0][1]):
            out_of_bonds = 1
        if y_update and (selected, x_pos) not in y_range_of_movement or (selected == y_bounds[0][0] and y_pos > y_bounds[0][1]):
            out_of_bonds = 1
        
        if out_of_bonds:
            window.fill(WHITE)
            message("You Lose!", BLACK, "", 600, 400)
            pygame.display.update()
            time.sleep(3)
            return

        window.fill(WHITE)
        window.blit(image, (360, 150))
        pygame.draw.circle(window, RED, [x_pos, y_pos], player_radius)
        pygame.draw.circle(window, GREEN, [finish_x_pos, finish_y_pos], finish_radius)
        message(start_message, BLACK, acceptances[index], 280, 100)
        pygame.display.update()
        
        if x_pos <= 450 and x_pos >= 430 and y_pos <= 460 and y_pos >= 440 and selected == 0:
            image = pygame.image.load(r'choose_1.png')
            window.fill(WHITE)
            window.blit(image, (50, 200))
            message("Choose the good option to escape the circuit!", BLACK, "", 300, 100)
            message("Where the circuit's main intensity (I) is bigger than the other's!", BLACK, "", 150, 150)
            pygame.draw.circle(window, RED, [x_pos - 310, y_pos + 55], player_radius)
            pygame.draw.circle(window, GREEN, [finish_x_pos - 310, finish_y_pos + 55], finish_radius)
            pygame.draw.circle(window, RED, [x_pos + 355, y_pos + 88], player_radius)
            pygame.draw.circle(window, GREEN, [finish_x_pos + 355, finish_y_pos + 110], finish_radius)
            pygame.display.update()
            option = 0
            while option == 0:
                
                option = return_option()
                time.sleep(0.01)
                
            if option == 1:
                window.fill(WHITE)
                message("You Lose!", BLACK, "", 600, 400)
                pygame.display.update()
                time.sleep(3)
                return
            else:
                image = pygame.image.load(r'3rd_option.png')
                window.fill(WHITE)
                window.blit(image, (50, 200))
                message(start_message, BLACK, acceptances[1], 280, 100)
                index = 1
                x_pos += 60
                y_pos += 40
                finish_y_pos = y_pos - 160
                finish_x_pos = x_pos
                print(x_pos)
            pygame.display.update()
            selected = 1
        
        if selected == 1 and x_pos <= finish_x_pos + 10 and x_pos >= finish_x_pos - 10 and y_pos <= finish_y_pos + 10 and y_pos >= finish_y_pos - 10:
            window.fill(WHITE)
            message("You escaped the circuit, good job!", BLACK, "", 400, 400)
            pygame.display.update()
            time.sleep(3)
            return
        
        clock.tick(20)