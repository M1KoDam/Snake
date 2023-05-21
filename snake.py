import pygame as pg
from snake_part import *
from sprites import *


class Snake:
    def __init__(self):
        self.SIZE = 64

        self.snake_parts = [SnakePart(Sprites.SNAKE_HEAD, self.SIZE, (self.SIZE, 0)),
                            SnakePart(Sprites.SNAKE_TAIL, self.SIZE, (0, 0))]

        self.speed = 4
        self.direction = (self.speed, 0)
        self.direction_delay = 0

    def update(self):
        for snake_part in self.snake_parts:
            snake_part.rect.move_ip(self.direction)

        if self.direction_delay >= self.SIZE:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.move((self.direction[1], -self.direction[0]))
                self.rotate(90)
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.move((-self.direction[1], self.direction[0]))
                self.rotate(-90)

        self.direction_delay += self.speed

    def move(self, direction):
        self.direction = direction
        self.direction_delay = 0

    def rotate(self, angle):
        for snake_part in self.snake_parts:
            snake_part.rotate(angle)
