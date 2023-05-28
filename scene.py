import pygame as pg
from sprites import *


class Scene:
    def __init__(self, program):
        self.WIDTH = program.WIDTH
        self.HEIGHT = program.HEIGHT

        self.surf = pg.image.load(Sprites.BACKGROUND)
        self.surf = pg.transform.scale(self.surf, (self.WIDTH, self.HEIGHT))
        self.rect = self.surf.get_rect(topleft=(0, 0))

    def update(self):
        pass
