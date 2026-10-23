class Scene:
    def __init__(self, decoration: list, interactables: list, x: int, y: int, laser_angle: float):
        self.decoration = decoration
        self.interactables = interactables
        
        self.laser_startpos = [x, y]
        self.laser_angle = laser_angle

    def update(self):
        for interactable in self.interactables:
            interactable.update()

    def draw(self, window, height, width):
        bundled = self.decoration
        bundled.extend(self.interactables)
        for object in bundled:
            object.draw(window, height, width)
