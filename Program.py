import pygame as pg
import sys
from snake import *
from scene import *


class SnakeGame:
    def __init__(self):
        self.HEIGHT = 600
        self.WIDTH = 800
        self.FPS = 60

        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.scene = Scene()

        pg.display.set_caption("Snake")
        pg.display.set_icon(pg.image.load("SnakeIcon.png"))
        self.display = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        pg.display.update()
        self.run()

    def run(self):
        while True:
            self.display.fill((0, 0, 0))
            self.display.blit(self.scene.scene, self.scene.rect)
            self.display.blit(self.snake.hero, self.snake.rect)

            self.scene.update()
            self.snake.move()

            pg.display.flip()

            self.clock.tick(self.FPS)

            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.time.delay(10)


program = SnakeGame()
