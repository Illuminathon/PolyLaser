import pygame

from .interactable_object import InteractableObject
from .decoration_object import DecorationObject
from .image import Image

class DraggableObject(InteractableObject, DecorationObject):
    def __init__(self, image_path, position, width, height, fallback):
        self.image = Image(image_path, position, width, height, fallback)
        self.position = position
        self.dragging = False

    def draw(self, window, height, width):
        self.image.draw(window, height, width)

    def is_mouse_over(self, mouse_position):
        return (self.position[0] <= mouse_position[0] <= self.position[0] + self.image.width) and (self.position[1] <= mouse_position[1] <= self.position[1] + self.image.height)

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if mouse_pressed and self.is_mouse_over(mouse_position):
            self.dragging = True
        elif not mouse_pressed:
            self.dragging = False

        if self.dragging:
            self.position = mouse_position
            self.image.update_position((self.position[0] - self.image.width // 2, self.position[1] - self.image.height // 2))