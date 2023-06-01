from Program import *
from levels import *
from sprites import *
from food import *
from menu import *
from score import *
from pause import *
from AudioManager import *

try:
    import pytest
    import pygame
except ModuleNotFoundError:
    import pip

    pip.TestSnakeGame(['install', '--quiet', 'pytest'])
    pip.TestSnakeGame(['install', '--quiet', 'pygame'])
    import pytest
    import pygame


class TestSnakeGame:

    @staticmethod
    def setup_class():
        # Создание экземпляра игры
        TestSnakeGame.game = SnakeGame()

    def test_game_init(self):
        # Проверка создания экземпляра игры
        assert TestSnakeGame.game is not None

    def test_level_init(self):
        # Проверка создания экземпляра уровня
        level = Level1(TestSnakeGame.game)
        assert level is not None

    def test_snake_init(self):
        # Проверка создания экземпляра змеи
        snake = Snake()
        assert snake is not None

    def test_food_init(self):
        # Проверка создания экземпляра еды
        snake = Snake()
        food = Food(TestSnakeGame.game, True, snake.snake_parts)
        assert food is not None

    def test_menu_init(self):
        # Проверка создания экземпляра меню
        buttons = [
            Button(TestSnakeGame.game.start_game, Sprites.BUTTON_START),
            Button(TestSnakeGame.game.settings, Sprites.BUTTON_OPTIONS),
            Button(TestSnakeGame.game.quit_game, Sprites.BUTTON_EXIT)
        ]
        menu = Menu(TestSnakeGame.game.display, TestSnakeGame.game.WIDTH,
                    TestSnakeGame.game.HEIGHT, buttons)
        assert menu is not None

    def test_music_off(self):
        # Проверка отключения музыки
        TestSnakeGame.game.pause_Music = True
        TestSnakeGame.game.run()
        assert TestSnakeGame.game.background_music.paused is True

    def test_music_on(self):
        # Проверка включения музыки
        TestSnakeGame.game.pause_Music = False
        TestSnakeGame.game.run()
        assert TestSnakeGame.game.background_music.paused is False

    def test_change_volume(self):
        # Проверка изменения громкости музыки
        TestSnakeGame.game.background_music.volume = 0.5
        TestSnakeGame.game.run()
        assert TestSnakeGame.game.background_music.volume == 0.6

    def test_next_level(self):
        # Проверка перехода на следующий уровень
        TestSnakeGame.game.TARGET = 1
        TestSnakeGame.game.HEALTH = 1
        TestSnakeGame.game.snake.snake_parts = [SnakePart(0, 0, 0, 0)]
        TestSnakeGame.game.next_level()
        assert TestSnakeGame.game.current_level == 1
        assert TestSnakeGame.game.GAME_RUNNING is True

    def test_restart_game(self):
        # Проверка перезапуска игры
        TestSnakeGame.game.GAME_RUNNING = False
        TestSnakeGame.game.restart_game()
        assert TestSnakeGame.game.GAME_RUNNING is True
