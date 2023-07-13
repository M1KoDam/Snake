import pygame as pg
from movement import *


class SnakeRotatePart(pg.sprite.Sprite):
    def __init__(self, sprite, snake, coordinate, angle):
        super().__init__()
        self.surf = pg.image.load(sprite)
        self.surf = pg.transform.scale(self.surf, (snake.SIZE, snake.SIZE))
        self.surf = pg.transform.rotate(self.surf, angle)
        self.rect = self.surf.get_rect(topleft=coordinate)
        self.tail_intersection = False
        self.timer = 0

    def update(self, tail, speed):
        if self.rect.colliderect(tail.rect):
            self.tail_intersection = True
            self.timer += 1
        if self.tail_intersection and self.timer > 60 // speed:
            return True
        return False
