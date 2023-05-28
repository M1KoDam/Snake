import pygame as pg
import random
from sprites import *


class Food:
    def __init__(self, x, y):
        self.SIZE = 64
        self.X = x
        self.Y = y

        self.surf = pg.image.load(Sprites.BOX)
        self.surf = pg.transform.scale(self.surf, (self.SIZE, self.SIZE))
        self.rect = self.surf.get_rect(topleft=(self.X, self.Y))

    def update(self):
        self.surf = pg.image.load(Sprites.BOX)
        self.surf = pg.transform.scale(self.surf, (self.SIZE, self.SIZE))
        self.rect = self.surf.get_rect(topleft=(self.X, self.Y))


