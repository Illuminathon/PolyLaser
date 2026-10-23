import pygame
from .decoration_object import DecorationObject

class Image(DecorationObject):
    def __init__(self, image_path: str, position, width, height, fallback: bool):
        if not fallback:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (width, height))
        self.fallback = fallback
        self.position = position
        self.width = width
        self.height = height

    def draw(self, window: pygame.Surface, height: int, width: int):
        if not self.fallback:
            window.blit(self.image, self.position)
        else:
            pygame.draw.rect(window, (255, 0, 0), (*self.position, self.width, self.height))

    def update_position(self, new_position):
        self.position = new_position