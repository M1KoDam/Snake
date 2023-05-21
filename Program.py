import pygame as pg
import sys
from snake import *
from scene import *
from sprites import *
from food import *


class SnakeGame:
    def __init__(self):
        self.HEIGHT = 700
        self.WIDTH = 700
        self.FPS = 60

        # Objects
        self.clock = pg.time.Clock()
        self.food = Food(self)
        self.snake = Snake()
        self.scene = Scene(self)

        # Display
        pg.display.set_caption("Snake")
        pg.display.set_icon(pg.image.load(Sprites.ICON))
        self.display = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        # Objects
        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.scene = Scene(self)

        pg.display.update()
        self.run()

    def run(self):
        while True:
            self.display.blit(self.scene.scene, self.scene.rect)
            for snake_part in self.snake.snake_parts:
                self.display.blit(snake_part.surf, snake_part.rect)
            self.display.blit(self.food.scene, self.food.rect)

            self.scene.update()
            self.snake.update()
            self.food.update(self, self.snake)

            pg.display.flip()

            self.clock.tick(self.FPS)

            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.time.delay(10)


program = SnakeGame()
