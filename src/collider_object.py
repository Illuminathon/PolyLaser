import pygame

from .decoration_object import DecorationObject
from .image import Image

class ColliderObject(DecorationObject):
    def __init__(self, image_path, position: tuple, width: int, height: int, fallback: bool):
        self.sprite = Image(image_path, position, width, height, fallback)
        self.position = position
        self.width = width
        self.height = height
        self.type = "collider"

    def draw(self, window, height, width):
        self.sprite.draw(window, height, width)

    def check_collision(self, ray_line):
        rect = pygame.Rect(
            self.sprite.position[0],
            self.sprite.position[1],
            self.width,
            self.height,
        )
        clipped = rect.clipline(ray_line[0], ray_line[1])
        if not clipped:
            return None

        start = pygame.Vector2(ray_line[0])
        return min(
            (pygame.Vector2(point) for point in clipped),
            key=lambda point: point.distance_squared_to(start),
        )