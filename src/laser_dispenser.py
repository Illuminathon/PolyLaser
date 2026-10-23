from .decoration_object import DecorationObject

class LazerDispenser(DecorationObject):
    def __init__(self, position: tuple, width: int, height: int):
        self.position = position
        self.width = width
        self.height = height
        self.laser_on = False