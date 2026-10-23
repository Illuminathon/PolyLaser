import pygame
from .decoration_object import DecorationObject

class Image(DecorationObject):
    def __init__(self, image_path: str, position, fallback: bool):
        if not fallback:
            self.image = pygame.image.load(image_path)
        self.fallback = fallback
        self.position = position

    def draw(self, window: pygame.Surface):
        if not self.fallback:
            window.blit(self.image, self.position)
        else:
            pygame.draw.rect(window, (255, 0, 0), (*self.position, 50, 50))

    def update_position(self, new_position):
        self.position = new_position