import pygame as pg
from snake_part import *
from sprites import *
from movement import *


class Snake:
    def __init__(self):
        self.SIZE = 64
        self.SPEED = 4
        self.START_COORDS = (100, 100)
        self.direction_delay = 0
        self.movement = Movement(self.SPEED, 0, 0)

        self.snake_parts = []

        self.snake_parts.append(SnakePart(Sprites.SNAKE_HEAD, self, 0, [self.movement], self.movement))
        self.snake_parts.append(SnakePart(Sprites.SNAKE_TAIL, self, 1, [], self.movement))

    def update(self):
        for snake_part in self.snake_parts:
            snake_part.move()

        if self.direction_delay >= self.SIZE:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.change_direction(self.movement.direction[1], -self.movement.direction[0], 90)
            elif keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.change_direction(-self.movement.direction[1], self.movement.direction[0], -90)
        else:
            self.movement.rotation = 0

        for snake_part in self.snake_parts:
            snake_part.movements.insert(0, self.movement.copy())

        self.direction_delay += self.SPEED

    def change_direction(self, x, y, angle):
        self.movement = Movement(x, y, angle)
        self.direction_delay = 0

    def add_part(self):
        angle = self.snake_parts[-1].DIRECTION
        self.snake_parts[-1].surf = pg.transform.rotate(pg.image.load(Sprites.SNAKE_BODY), angle)

        new_snake_part = SnakePart(Sprites.SNAKE_TAIL, self, 1,
                                   self.snake_parts[-1].movements.copy(),
                                   self.snake_parts[-1].movements[0])
        new_snake_part.rotate(angle)
        self.snake_parts.append(new_snake_part)
