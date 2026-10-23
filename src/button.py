import pygame
from .interactable_object import InteractableObject
from .decoration_object import DecorationObject
from .text import Text
from .image import Image

class Button(InteractableObject, DecorationObject):
    def __init__(self, image_path: str, text: str, font_size: int, font_name: str, color: tuple, position: tuple, width, height, on_click, fallback: bool = False):
        self.background_image = Image(image_path, position, fallback)
        self.text = Text(text, font_size, font_name, color, position)
        self.position = position
        self.on_click = on_click
        self.font_size = font_size
        self.width = width
        self.height = height
        self.clicked = False

    def update_title(self, new_text: str):
        self.text.update_text(new_text)

    def update_position(self, new_position: tuple):
        self.position = new_position
        self.text.update_position(new_position)
        self.background_image.update_position(new_position)

    def draw(self, surface: pygame.Surface, width: int, height: int):
        self.background_image.draw(surface, height, width)
        self.text.draw(surface, height, width)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.is_hovered(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.on_click()
            else:
                self.clicked = False

    def is_hovered(self, mouse_pos: tuple):
        return (self.position[0] <= mouse_pos[0] <= self.position[0] + self.width) and (self.position[1] <= mouse_pos[1] <= self.position[1] + self.height)