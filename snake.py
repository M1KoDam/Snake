import pygame as pg
from snake_part import *
from sprites import *
from movement import *
from snake_rotate_part import *
from AudioManager import *


class Snake:
    def __init__(self):
        self.SIZE = 64
        self.SPEED = 4
        self.START_COORDS = (64, 64)
        self.direction_delay = 0
        self.delay = self.SIZE + 2
        self.movement = Movement(self.SPEED, 0, 0)

        self.snake_parts = []
        self.change_rotation_parts = []

        self.snake_parts.append(
            SnakePart(Sprites.SNAKE_HEAD, self, 0, [self.movement],
                      self.movement))
        self.snake_parts.append(
            SnakePart(Sprites.SNAKE_TAIL, self, 1, [self.movement],
                      self.movement))

        self.get_damage = AudioManager("musics/get_damage.mp3", 0.8, True)

    def update(self):
        for snake_part in self.snake_parts:
            snake_part.move()

        temp_change_rotation_part = []
        for change_rotation_part in self.change_rotation_parts:
            if not (change_rotation_part.update(self.snake_parts[-1], self.SPEED)):
                temp_change_rotation_part.append(change_rotation_part)
        self.change_rotation_parts = temp_change_rotation_part

        if self.direction_delay > self.delay:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.change_direction(self.movement.direction[1],
                                      -self.movement.direction[0], 90)
            elif keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.change_direction(-self.movement.direction[1],
                                      self.movement.direction[0], -90)
        else:
            self.movement.rotation = 0

        for snake_part in self.snake_parts:
            snake_part.movements.insert(0, self.movement.copy())

        self.direction_delay += self.SPEED

    def change_direction(self, x, y, angle):
        new_angle = self.snake_parts[0].DIRECTION
        if angle < 0:
            new_angle += 90

        self.change_rotation_parts.append(
            SnakeRotatePart(Sprites.SNAKE_TURN, self,
                            (self.snake_parts[0].rect.x,
                             self.snake_parts[0].rect.y), new_angle))

        self.movement = Movement(x, y, angle)
        self.direction_delay = 0

    def delete_part(self):
        self.snake_parts.pop()
        self.snake_parts[-1].update_sprite(Sprites.SNAKE_TAIL, self)

    def add_part(self):
        angle = self.snake_parts[-1].DIRECTION
        self.snake_parts[-1].surf = pg.transform.rotate(
            pg.image.load(Sprites.SNAKE_BODY), angle)

        new_snake_part = SnakePart(Sprites.SNAKE_TAIL, self, 1,
                                   self.snake_parts[-1].movements.copy(),
                                   self.snake_parts[-1].movements[0])

        new_snake_part.rotate(angle)
        self.snake_parts.append(new_snake_part)

    def check_self_collision(self):
        head = self.snake_parts[0]
        for part in self.snake_parts[1:]:
            if part.rect.colliderect(
                    head.rect) and self.direction_delay > self.delay:
                return True
        return False

    def check_box_collision(self, level):
        head = self.snake_parts[0]
        for box in level.boxes:
            if box.rect.colliderect(
                    head.rect):
                self.get_damage.play_sound()
                return True
        return False

    def check_scene_collision(self, level):
        head = self.snake_parts[0].rect
        if head.x < 0 or head.x + self.SIZE > level.WIDTH:
            return True
        if head.y < 0 or head.y + self.SIZE > level.HEIGHT:
            return True
        return False

    def increase_speed(self):
        if self.SPEED == 8:
            return
        self.SPEED = min(8, self.SPEED*2)
        block_length = get_block_length(self.SPEED)
        self.snake_parts[-1].increase_speed(self.SPEED, len(self.snake_parts)-1)
        a = self.snake_parts[-1]
        for i in range(len(self.snake_parts) - 1):
            self.snake_parts[i].movements = make_movements_copy(a.movements[:(block_length * i) + 2])

        self.movement = self.snake_parts[0].movements[-1]

    def decrease_speed(self):
        if self.SPEED == 2:
            return
        self.SPEED = max(2, self.SPEED//2)
        block_length = get_block_length(self.SPEED)
        self.snake_parts[-1].decrease_speed(self.SPEED, len(self.snake_parts) - 1)
        a = self.snake_parts[-1]

        for i in range(len(self.snake_parts) - 1):
            self.snake_parts[i].movements = make_movements_copy(a.movements[:(block_length * i)+2])

        self.movement = self.snake_parts[0].movements[-1]
