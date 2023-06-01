import pygame as pg
from movement import *


def calculate_coordinates(snake):
    if len(snake.snake_parts) == 0:
        return snake.START_COORDS

    coords = (snake.snake_parts[-1].rect.x, snake.snake_parts[-1].rect.y)
    if snake.movement.direction[0] > 0:
        coords = (coords[0] - snake.SIZE, coords[1])
    elif snake.movement.direction[0] < 0:
        coords = (coords[0] + snake.SIZE, coords[1])
    elif snake.movement.direction[1] > 0:
        coords = (coords[0], coords[1] - snake.SIZE)
    else:
        coords = (coords[0], coords[1] + snake.SIZE)

    return coords


class SnakePart(pg.sprite.Sprite):
    def __init__(self, sprite, snake, parts, prev_movements, movement):
        super().__init__()
        self.DIRECTION = 0
        self.surf = pg.image.load(sprite)
        self.surf = pg.transform.scale(self.surf, (snake.SIZE, snake.SIZE))
        self.rect = self.surf.get_rect(topleft=calculate_coordinates(snake))

        self.movements = prev_movements
        for i in range(int(snake.SIZE / snake.SPEED) * parts):
            self.movements.append(movement)

    def move(self):
        current_movement = self.movements.pop()
        self.rect.move_ip(current_movement.direction)
        self.surf = pg.transform.rotate(self.surf, current_movement.rotation)
        self.DIRECTION += current_movement.rotation

    def rotate(self, angle):
        self.surf = pg.transform.rotate(self.surf, angle)
        self.DIRECTION += angle

    def update_sprite(self, sprite, snake):
        self.surf = pg.image.load(sprite)
        self.surf = pg.transform.scale(self.surf, (snake.SIZE, snake.SIZE))
        self.surf = pg.transform.rotate(self.surf, self.DIRECTION)
