import pygame
from .draggable_object import DraggableObject

class Mirror(DraggableObject):
    def __init__(self, image_path, position, width, height, fallback):
        super().__init__(image_path, position, width, height, fallback)
        self.angle = 0
        self.type = "mirror"
        self._last_mouse_position = None
        self._base_image = (
            self.image.image.copy() if not self.image.fallback else None
        )

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        left_button = pygame.mouse.get_pressed()[0]
        rotating = left_button and pygame.key.get_pressed()[pygame.K_r]

        if left_button and (self.dragging or self.is_mouse_over(mouse_position)):
            self.dragging = True
            if rotating:
                if self._last_mouse_position is not None:
                    mouse_delta = mouse_position[0] - self._last_mouse_position[0]
                    self.rotate(mouse_delta * 0.5)
            else:
                self.position = mouse_position
                self.image.update_position(
                    (
                        self.position[0] - self.image.width // 2,
                        self.position[1] - self.image.height // 2,
                    )
                )
        else:
            self.dragging = False

        self._last_mouse_position = mouse_position if rotating else None

    # To nie będzie widoczne w fallback modzie
    def rotate(self, angle):
        self.angle = (self.angle + angle) % 360
        if self._base_image is None:
            return

        center = (
            self.image.position[0] + self.image.width / 2,
            self.image.position[1] + self.image.height / 2,
        )
        self.image.image = pygame.transform.rotate(self._base_image, self.angle)
        self.image.width, self.image.height = self.image.image.get_size()
        self.image.update_position(
            (
                round(center[0] - self.image.width / 2),
                round(center[1] - self.image.height / 2),
            )
        )

    def check_collision(self, ray_line):
        rect = pygame.Rect(
            self.image.position[0],
            self.image.position[1],
            self.image.width,
            self.image.height,
        )
        clipped = rect.clipline(ray_line[0], ray_line[1])
        if not clipped:
            return None

        start = pygame.Vector2(ray_line[0])
        return min(
            (pygame.Vector2(point) for point in clipped),
            key=lambda point: point.distance_squared_to(start),
        )

    def calculate_reflection(self, direction):
        normal = pygame.Vector2(0, -1).rotate(-self.angle)
        return direction.reflect(normal).normalize()