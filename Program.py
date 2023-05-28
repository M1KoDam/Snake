import pygame as pg
import sys

from snake import *
from levels import *
from sprites import *
from food import *
from menu import *
from score import *
from pause import *


class SnakeGame:
    def __init__(self):
        pg.init()

        self.HEIGHT = 700
        self.WIDTH = 700
        self.FPS = 60
        self.GAME_RUNNING = True
        self.HEALTH = 3
        self.TARGET = 17

        # Display
        pg.display.set_caption("Snake")
        pg.display.set_icon(pg.image.load(Sprites.ICON))
        self.display = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        # Levels
        self.levels = [Level1(self), Level2(self), Level3(self)]
        self.current_level = 0
        self.level = self.levels[self.current_level]

        # Objects
        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.food = Food(self, True, self.snake.snake_parts + self.level.boxes)
        self.bug = Food(self, False, self.snake.snake_parts + self.level.boxes)
        self.score = Score(10, 10)
        self.pause = PauseButton((self.WIDTH-118)/2, (self.HEIGHT-56)/2)

        # Menu
        buttons = [Button(self.start_game, Sprites.BUTTON_START),
                   Button(self.quit_game, Sprites.BUTTON_OPTIONS),
                   Button(self.quit_game, Sprites.BUTTON_EXIT)
                   ]
        self.menu = Menu(self.display, self.WIDTH, self.HEIGHT, buttons)
        pg.font.init()

        pg.display.update()
        self.menu.run()

    def next_level(self):
        if self.current_level >= 2:
            self.GAME_RUNNING = False
            return

        self.current_level += 1
        self.restart_game()

    def start_game(self):
        self.HEALTH = 3
        self.current_level = 0
        self.restart_game()

    def restart_game(self):
        self.GAME_RUNNING = True

        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.level = self.levels[self.current_level]
        self.food = Food(self, True,
                         self.snake.snake_parts + self.level.boxes)
        self.bug = Food(self, False,
                        self.snake.snake_parts + self.level.boxes)
        self.score = Score(10, 10)
        self.pause = PauseButton((self.WIDTH - 118) / 2,
                                 (self.HEIGHT - 56) / 2)

        # Menu
        buttons = [Button(self.restart_game, Sprites.BUTTON_START),
                   Button(self.quit_game, Sprites.BUTTON_OPTIONS),
                   Button(self.quit_game, Sprites.BUTTON_EXIT)
                   ]
        self.menu = Menu(self.display, self.WIDTH, self.HEIGHT, buttons)
        pg.font.init()

        pg.display.update()

        self.run()

    def run(self):
        while self.GAME_RUNNING:
            self.level.update(self.display)
            for snake_part in self.snake.snake_parts:
                self.display.blit(snake_part.surf, snake_part.rect)

            for change_rotation_part in self.snake.change_rotation_parts:
                self.display.blit(change_rotation_part.surf,
                                  change_rotation_part.rect)
            self.display.blit(self.food.scene, self.food.rect)
            self.display.blit(self.bug.scene, self.bug.rect)

            if self.HEALTH <= 0:
                self.GAME_RUNNING = False
                return

            print(self.HEALTH)

            if len(self.snake.snake_parts) >= self.TARGET:
                self.next_level()

            if self.snake.check_self_collision() \
                    or len(self.snake.snake_parts) < 2 \
                    or self.snake.check_scene_collision(self.level)\
                    or self.snake.check_box_collision(self.level):
                self.HEALTH -= 1
                self.restart_game()

            self.snake.update()
            self.food.update(self, self.snake, self.score, self.snake.snake_parts + self.level.boxes)
            self.bug.update(self, self.snake, self.score, self.snake.snake_parts + self.level.boxes)
            self.score.draw(self.display)

            pg.display.flip()
            self.clock.tick(self.FPS)

            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if i.type == pg.KEYDOWN:
                    if i.key == pg.K_ESCAPE:
                        print("Pressed esc")
                        self.pause.paused = not self.pause.paused

            pg.time.delay(10)

            if self.pause.paused:
                while self.pause.paused:
                    self.pause.draw(self.display)
                    pg.display.flip()
                    for key in pg.event.get():
                        self.pause.handle_event(key)

    def quit_game(self):
        pg.quit()
        sys.exit()


program = SnakeGame()
