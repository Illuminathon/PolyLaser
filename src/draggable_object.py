from .interactable_object import InteractableObject
from .decoration_object import DecorationObject
from .image import Image

class DraggableObject(InteractableObject, DecorationObject):
    def __init__(self, image_path, position):
        self.image = Image(image_path, position)
        self.position = position
        self.dragging = False

    def draw(self, window):
        self.image.draw(window, self.position)

    def update(self, mouse_position, mouse_pressed):
        if mouse_pressed and self.is_mouse_over(mouse_position):
            self.dragging = True
        elif not mouse_pressed:
            self.dragging = False

        if self.dragging:
            self.position = mouse_position