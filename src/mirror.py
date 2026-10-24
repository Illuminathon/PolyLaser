import pygame
from .draggable_object import DraggableObject

class Mirror(DraggableObject):
    def __init__(self, image_path, position, width, height, fallback):
        super().__init__(image_path, position, width, height, fallback)
        self.angle = 0
        self.type = "mirror"
        self._last_mouse_position = None
        self._base_size = pygame.Vector2(width, height)
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
        start = pygame.Vector2(ray_line[0])
        ray = pygame.Vector2(ray_line[1]) - start
        corners = self._get_corners()
        intersections = []

        for first, second in zip(corners, corners[1:] + corners[:1]):
            edge = second - first
            denominator = ray.cross(edge)
            if abs(denominator) < 1e-8:
                continue

            offset = first - start
            ray_distance = offset.cross(edge) / denominator
            edge_distance = offset.cross(ray) / denominator
            if 0 <= ray_distance <= 1 and 0 <= edge_distance <= 1:
                intersections.append(start + ray * ray_distance)

        if not intersections:
            return None

        return min(
            intersections,
            key=lambda point: point.distance_squared_to(start),
        )

    def _get_corners(self):
        center = pygame.Vector2(
            self.image.position[0] + self.image.width / 2,
            self.image.position[1] + self.image.height / 2,
        )
        half_size = self._base_size / 2
        return [
            center + pygame.Vector2(-half_size.x, -half_size.y).rotate(-self.angle),
            center + pygame.Vector2(half_size.x, -half_size.y).rotate(-self.angle),
            center + pygame.Vector2(half_size.x, half_size.y).rotate(-self.angle),
            center + pygame.Vector2(-half_size.x, half_size.y).rotate(-self.angle),
        ]

    def calculate_reflection(self, direction, hit_point):
        corners = self._get_corners()

        def distance_to_edge(point, edge):
            start, end = edge
            segment = end - start
            length_squared = segment.length_squared()
            if length_squared == 0:
                return point.distance_squared_to(start)
            projection = max(
                0,
                min(1, (point - start).dot(segment) / length_squared),
            )
            closest = start + segment * projection
            return point.distance_squared_to(closest)

        first_edge = min(
            zip(corners, corners[1:] + corners[:1]),
            key=lambda edge: distance_to_edge(hit_point, edge),
        )
        edge = first_edge[1] - first_edge[0]
        normal = pygame.Vector2(-edge.y, edge.x).normalize()
        return direction.reflect(normal).normalize()