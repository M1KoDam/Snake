import pygame as pg


class SnakePart:
    def __init__(self, sprite, size, coord):
        self.surf = pg.image.load(sprite)
        self.surf = pg.transform.scale(self.surf, (size, size))
        self.rect = self.surf.get_rect(topleft=coord)

    def rotate(self, angle):
        self.surf = pg.transform.rotate(self.surf, angle)

