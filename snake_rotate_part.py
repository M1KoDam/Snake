import pygame as pg
from movement import *


class SnakeRotatePart(pg.sprite.Sprite):
    def __init__(self, sprite, snake, coordinate):
        super().__init__()
        self.surf = pg.image.load(sprite)
        self.surf = pg.transform.scale(self.surf, (snake.SIZE, snake.SIZE))
        self.rect = self.surf.get_rect(topleft=coordinate)

    def update(self, tail):
        if self.rect.colliderect(tail.rect):
            print("KILL")
            self.kill()
