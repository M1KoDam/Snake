import pygame as pg
import random
from sprites import *


class Food:
    def __init__(self, program, food, another_rects):
        self.sprite = Sprites.FOOD
        if not food:
            self.sprite = Sprites.BUG

        self.SIZE = 64
        self.foodx = round(random.randint(1, program.WIDTH - self.SIZE)
                           / self.SIZE) * self.SIZE
        self.foody = round(random.randint(1, program.WIDTH - self.SIZE)
                           / self.SIZE) * self.SIZE

        self.scene = pg.image.load(self.sprite)
        self.scene = pg.transform.scale(self.scene, (self.SIZE, self.SIZE))
        self.rect = self.scene.get_rect(topleft=(self.foodx, self.foody))

        self.regenerate(program, another_rects)

    def update(self, program, snake, score, another_rects):
        self.scene = pg.image.load(self.sprite)
        self.scene = pg.transform.scale(self.scene, (self.SIZE, self.SIZE))
        self.rect = self.scene.get_rect(topleft=(self.foodx, self.foody))
        self.is_eat(program, snake, score, another_rects)

    def is_eat(self, program, snake, score, another_rects):

        if self.rect.colliderect(snake.snake_parts[0].rect):
            if self.sprite is Sprites.FOOD:
                snake.add_part()
                score.increment_score()
            else:
                snake.delete_part()
                score.decrement_score()
            self.foodx = round(random.randrange(0, program.WIDTH - snake.SIZE)
                               / 10.0) * 10.0
            self.foody = round(random.randrange(0, program.WIDTH - snake.SIZE)
                               / 10.0) * 10.0
            self.regenerate(program, another_rects)

    def check_regenerate(self, another_rects):
        for other in another_rects:
            if self.rect.colliderect(other.rect):
                return True

        return False

    def regenerate(self, program, another_rects):
        while self.check_regenerate(another_rects):
            self.foodx = round(random.randint(1,
                                              program.WIDTH - self.SIZE)
                               / self.SIZE) * self.SIZE
            self.foody = round(random.randint(1,
                                              program.WIDTH - self.SIZE)
                               / self.SIZE) * self.SIZE
            self.scene = pg.image.load(self.sprite)
            self.scene = pg.transform.scale(self.scene,
                                            (self.SIZE, self.SIZE))
            self.rect = self.scene.get_rect(topleft=(self.foodx, self.foody))
