import pygame
from .decoration_object import DecorationObject

class Text(DecorationObject):
    def __init__(self, text: str, font_size: int, font_name, color: tuple, position: tuple):
        self.font = pygame.font.SysFont(font_name, font_size)
        self.surface = self.font.render(text, True, color)
        self.position = position
        self.color = color
        self.text = text

    def draw(self, window, height, width):
        window.blit(self.surface, self.position)

    def update_surface(self):
        self.surface = self.font.render(self.text, True, self.color)
        
    def update_text(self, new_text: str):
        self.text = new_text
        self.update_surface()

    def update_position(self, new_position: tuple):
        self.position = new_position

    def update_color(self, new_color: tuple):
        self.color = new_color
        self.update_surface()