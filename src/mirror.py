import pygame

class Mirror:
    def __init__(self, x: int, y: int, angle: float):
        self.x = x
        self.y = y
        self.angle = angle

        pass

    def update_pos_abs(self, x: int, y: int):
        self.x = x
        self.y = y

    # TODO: wywalic niepotrzebne
    def update_pos_rel(self, dx: int, dy: int):
        self.x+=dx
        self.y+=dy

    def draw(self, window: pygame.Surface):
        pass # TODO: draw image

    def rotate_abs(self, angle: float):
        self.angle = angle
    
    def rotate_rel(self, angle: float):
        self.angle += angle
        if self.angle > 360:
            self.angle-=360 # TODO: wezcie ogarnicjei jak to lepiej zrobic xddd nie ma szans