import pygame
pygame.init()

screen_info = pygame.display.Info()  
width = screen_info.current_w # Contains information about the width of screen
height = screen_info.current_h # Contains information about the height of screen

window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("PolyLaser")

run = True




