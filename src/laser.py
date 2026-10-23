import pygame 

def draw_laser(surface):
    start_position = (100, 360)
    end_position = (1180, 360)

    pygame.draw.line(surface, (255, 0, 0), start_position, end_position, width=5)
