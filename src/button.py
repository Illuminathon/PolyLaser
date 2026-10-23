import pygame
from .interactable_object import InteractableObject
from .decoration_object import DecorationObject
from .text import Text
from .image import Image

class Button(InteractableObject, DecorationObject):
    def __init__(self, image_path: str, text: str, font_size: int, font_name: str, color: tuple, position: tuple, on_click):
        self.background_image = Image(image_path)
        self.text = Text(text, font_size, font_name, color, position / 2)
        self.position = position
        self.on_click = on_click

    def update_title(self, new_text: str):
        self.text.update_text(new_text)

    def update_position(self, new_position: tuple):
        self.position = new_position
        self.text.update_position(new_position / 2)
        self.background_image.update_position(new_position)

    def draw(self, surface: pygame.Surface):
        self.text.draw(surface)
        self.background_image.draw(surface)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.is_hovered(self, mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.on_click()

    def is_hovered(self, mouse_pos: tuple):
        return (self.position[0] <= mouse_pos[0] <= self.position[0] + self.width) and (self.position[1] <= mouse_pos[1] <= self.position[1] + self.height)