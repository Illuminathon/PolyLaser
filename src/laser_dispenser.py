import pygame
from .decoration_object import DecorationObject
from .image import Image

class LaserDispenser(DecorationObject):
    def __init__(self, image_path: str, position: tuple, width: int, height: int, fallback: bool = False):
        self.sprite = Image(image_path, position, width, height, fallback)
        self.position = position
        self.width = width
        self.height = height
        self.laser_on = True
        self.angle = -90
        self.type = "laser_dispenser"

    def draw(self, window, height, width):
        self.sprite.draw(window, height, width)

    def get_laser_origin(self):
        return pygame.Vector2(
            self.position[0] + self.width / 2,
            self.position[1] + self.height / 2,
        )
