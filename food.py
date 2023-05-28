import pygame as pg
import random
from sprites import *


class Food:
    def __init__(self, program, food):
        self.sprite = Sprites.FOOD
        if not food:
            self.sprite = Sprites.BUG

        self.SIZE = 64
        self.foodx = round(random.randint(1, program.WIDTH - self.SIZE) / self.SIZE) * self.SIZE
        self.foody = round(random.randint(1, program.WIDTH - self.SIZE) / self.SIZE) * self.SIZE

        self.scene = pg.image.load(self.sprite)
        self.scene = pg.transform.scale(self.scene, (self.SIZE, self.SIZE))
        self.rect = self.scene.get_rect(topleft=(self.foodx, self.foody))

    def update(self, program, snake):
        self.scene = pg.image.load(self.sprite)
        self.scene = pg.transform.scale(self.scene, (self.SIZE, self.SIZE))
        self.rect = self.scene.get_rect(topleft=(self.foodx, self.foody))
        self.is_eat(program, snake)

    def is_eat(self, program, snake):

        if self.rect.colliderect(snake.snake_parts[0].rect):
            if self.sprite is Sprites.FOOD:
                snake.add_part()
            else:
                snake.delete_part()
            self.foodx = round(random.randrange(0, program.WIDTH - snake.SIZE) / 10.0) * 10.0
            self.foody = round(random.randrange(0, program.WIDTH - snake.SIZE) / 10.0) * 10.0
