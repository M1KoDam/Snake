import pygame as pg
from sprites import *


class Level_Medium:
    def __init__(self, program):
        self.WIDTH = program.WIDTH
        self.HEIGHT = program.HEIGHT

        self.scene = pg.image.load(Sprites.BACKGROUND)
        self.scene = pg.transform.scale(self.scene, (self.WIDTH, self.HEIGHT))
        self.rect = self.scene.get_rect(topleft=(0, 0))

    def update(self):
        pass
