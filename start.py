import pygame
import time
import first_level
import second_level
import third_level
import fourth_level
import fifth_level

pygame.init()

HEIGHT = 800
WIDTH = 1300
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
pygame.display.set_caption("ELTH Project")

image = pygame.image.load(r'select_photo.png')
window.fill(WHITE)
window.blit(image, (250, 100))

level = 0

pygame.draw.rect(window, BLACK, pygame.Rect(410, 400, 90, 90), 2)
pygame.draw.rect(window, BLACK, pygame.Rect(590, 400, 90, 90), 2)
pygame.draw.rect(window, BLACK, pygame.Rect(773, 400, 90, 90), 2)
pygame.draw.rect(window, BLACK, pygame.Rect(490, 540, 90, 90), 2)
pygame.draw.rect(window, BLACK, pygame.Rect(675, 540, 90, 90), 2)
pygame.display.update()

def choose_option():
    
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    ev = pygame.event.get()
    has_been_clicked = False
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            has_been_clicked = True
    if has_been_clicked:
        if mouse_pos_x >= 410 and mouse_pos_x <= 500 and mouse_pos_y >= 400 and mouse_pos_y <= 490:
            return 1
        elif mouse_pos_x >= 590 and mouse_pos_x <= 680 and mouse_pos_y >= 400 and mouse_pos_y <= 490:
            return 2
        elif mouse_pos_x >= 773 and mouse_pos_x <= 863 and mouse_pos_y >= 400 and mouse_pos_y <= 490:
            return 3
        elif mouse_pos_x >= 490 and mouse_pos_x <= 580 and mouse_pos_y >= 540 and mouse_pos_y <= 630:
            return 4
        elif mouse_pos_x >= 675 and mouse_pos_x <= 765 and mouse_pos_y >= 540 and mouse_pos_y <= 630:
            return 5
    return 0

while 1:
    level = choose_option()
    
    if level == 1:
        first_level.run(window)
    elif level == 2:
        second_level.run(window)
    elif level == 3:
        third_level.run(window)
    elif level == 4:
        fourth_level.run(window)
    elif level == 5:
        fifth_level.run(window)
    
    window.fill(WHITE)
    window.blit(image, (250, 100))
    pygame.display.update()

pygame.quit()
