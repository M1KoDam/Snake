import pygame as pg
import random
from sprites import *
from AudioManager import *


class Food:
    def __init__(self, program, food_type, another_rects):
        self.sprite = food_type
        match self.sprite:
            case Sprites.BUG:
                self.eat_bug_sound = AudioManager("musics/sound_eating_bad_food.mp3", 0.3, True)
            case _:
                self.eat_apple_sound = AudioManager("musics/sound_eating_good_food.mp3", 0.3, True)
                # Кирилл звук ( и нельзя ли не создавать 4 разных переменных а лишь одну изменять?)

        if self.sprite is Sprites.APPLE or self.sprite is Sprites.PEAR:
            if random.randint(0, 10) < 2:
                self.sprite = Sprites.PEAR
            else:
                self.sprite = Sprites.APPLE

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
            match self.sprite:
                case Sprites.APPLE:
                    self.eat_apple_sound.play_sound()
                    snake.add_part()
                    score.increment_score()
                case Sprites.PEAR:
                    self.eat_apple_sound.play_sound()
                    snake.add_part()
                    score.increment_score(3)
                case Sprites.BUG:
                    self.eat_bug_sound.play_sound()
                    snake.delete_part()
                    score.decrement_score()
                case Sprites.PIZZA:
                    self.eat_apple_sound.play_sound()
                    snake.decrease_speed()
                case Sprites.CARROT:
                    self.eat_apple_sound.play_sound()
                    snake.increase_speed()

            self.foodx = round(random.randrange(0, program.WIDTH - snake.SIZE)
                               / 10.0) * 10.0
            self.foody = round(random.randrange(0, program.WIDTH - snake.SIZE)
                               / 10.0) * 10.0
            self.regenerate(program, another_rects)

    def check_regenerate(self, another_rects):
        for other in another_rects:
            if self.rect != other.rect and self.rect.colliderect(other.rect):
                print("aaaaa")
                return True

        return False

    def regenerate(self, program, another_rects):
        while self.check_regenerate(another_rects):
            if self.sprite is Sprites.APPLE or self.sprite is Sprites.PEAR:
                if random.randint(0, 10) < 2:
                    self.sprite = Sprites.PEAR
                else:
                    self.sprite = Sprites.APPLE
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
