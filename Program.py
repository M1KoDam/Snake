import pygame as pg
import sys

from snake import *
from scene import *
from sprites import *
from food import *
from menu import *


class SnakeGame:
    def __init__(self):
        pg.init()

        self.HEIGHT = 700
        self.WIDTH = 700
        self.FPS = 60
        self.GAME_RUNNING = True

        # Display
        pg.display.set_caption("Snake")
        pg.display.set_icon(pg.image.load(Sprites.ICON))
        self.display = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        # Objects
        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.scene = Scene(self)
        self.food = Food(self, True)
        self.bug = Food(self, False)

        # Menu
        buttons = [Button(self.start_game, Sprites.BUTTON_START),
                   Button(self.quit_game, Sprites.BUTTON_OPTIONS),
                   Button(self.quit_game, Sprites.BUTTON_EXIT)
                   ]
        self.menu = Menu(self.display, self.WIDTH, self.HEIGHT, buttons)
        pg.font.init()

        pg.display.update()
        self.menu.run()

    def start_game(self):
        self.GAME_RUNNING = True

        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.scene = Scene(self)
        self.food = Food(self, True)
        self.bug = Food(self, False)

        # Menu
        buttons = [Button(self.start_game, Sprites.BUTTON_START),
                   Button(self.quit_game, Sprites.BUTTON_OPTIONS),
                   Button(self.quit_game, Sprites.BUTTON_EXIT)
                   ]
        self.menu = Menu(self.display, self.WIDTH, self.HEIGHT, buttons)
        pg.font.init()

        pg.display.update()

        self.run()

    def run(self):
        while self.GAME_RUNNING:
            self.display.blit(self.scene.scene, self.scene.rect)

            for snake_part in self.snake.snake_parts:
                self.display.blit(snake_part.surf, snake_part.rect)

            for change_rotation_part in self.snake.change_rotation_parts:
                self.display.blit(change_rotation_part.surf,
                                  change_rotation_part.rect)

            self.display.blit(self.food.scene, self.food.rect)
            self.display.blit(self.bug.scene, self.bug.rect)

            self.scene.update()
            self.snake.update()

            if len(self.snake.snake_parts) >= 20:
                print("WIN")

            if self.snake.check_self_collision() \
                    or len(self.snake.snake_parts) < 2 \
                    or self.snake.check_scene_collision(self.scene):
                self.GAME_RUNNING = False

            self.food.update(self, self.snake)
            self.bug.update(self, self.snake)

            pg.display.flip()
            self.clock.tick(self.FPS)

            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.time.delay(10)

    def quit_game(self):
        pg.quit()
        sys.exit()


program = SnakeGame()
