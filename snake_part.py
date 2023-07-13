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


def make_movements_copy(movements):
    result = []
    for movement in movements:
        result.append(movement.copy())
    return result


def get_block_length(speed):
    match speed:
        case 4:
            return 16
        case 2:
            return 32
        case 8:
            return 8
    return 16


def find_rotation(movements):
    for i in range(len(movements)):
        if movements[i].rotation != 0:
            return i, movements[i].rotation
    return -1, 0


def find_rotations(movements):
    result = []
    for i in range(len(movements)):
        if movements[i].rotation != 0:
            result.append((i, movements[i].rotation))
    return result


def delete_rotation(movements):
    for movement in movements:
        movement.rotation = 0
    return movements


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

    def increase_speed(self, speed, part_number):
        block_length = get_block_length(speed // 2)
        new_movements = []
        rotations = find_rotations(self.movements)

        for x in range(1, part_number + 1):
            for y in self.movements[block_length * (x - 1):block_length * x]:
                new_movements += [y.copy().del_r()]

        for y in range(0, len(self.movements[part_number * block_length:]), 2):
            new_movements += [self.movements[part_number * block_length:][y].copy()]

        for i, r in rotations:
            new_movements[i//2].rotation = r

        self.movements = new_movements

        for i in range(len(self.movements)):
            self.movements[i].change_speed(speed)

    def decrease_speed(self, speed, part_number):
        block_length = get_block_length(speed*2)
        new_movements = []

        for x in range(1, part_number + 1):
            for y in self.movements[block_length * (x - 1):block_length * x]:
                new_movements += [y, y.copy().del_r()]

        for y in self.movements[part_number*block_length:]:
            new_movements = new_movements + 2 * [y.copy()]
        self.movements = new_movements

        for i in range(len(self.movements)):
            self.movements[i].change_speed(speed)
