import pygame as pg
import random
from sprites import *


class Food:
    def __init__(self, program):
        self.foodx = round(random.randint(1, program.WIDTH - 20) / 20) * 20
        self.foody = round(random.randint(1, program.WIDTH - 20) / 20) * 20

        self.scene = pg.image.load(Sprites.FOOD)
        self.scene = pg.transform.scale(self.scene, (20, 20))
        self.rect = self.scene.get_rect(topleft=(self.foodx, self.foody))

    def update(self, program, snake):
        self.scene = pg.image.load(Sprites.FOOD)
        self.scene = pg.transform.scale(self.scene, (20, 20))
        self.rect = self.scene.get_rect(topleft=(self.foodx, self.foody))
        self.is_eat(program, snake)

    def is_eat(self, program, snake):

        if self.rect.colliderect(snake.snake_parts[0].rect):
            self.foodx = round(random.randrange(0, program.WIDTH - snake.SIZE) / 10.0) * 10.0
            self.foody = round(random.randrange(0, program.WIDTH - snake.SIZE) / 10.0) * 10.0
