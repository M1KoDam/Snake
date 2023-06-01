import pygame as pg
from sprites import *


class Score:
    def __init__(self, x, y, font_size=30, font_color=(255, 255, 255)):
        pg.init()
        self.score = 0
        self.x = x
        self.y = y
        self.font_size = font_size
        self.font_color = font_color
        self.font = pg.font.SysFont(None, self.font_size)
        self.text = self.font.render(f"Score: {self.score}",
                                     True, self.font_color)

    def update(self):
        self.text = self.font.render(f"Score: {self.score}",
                                     True, self.font_color)

    def draw(self, surface):
        surface.blit(self.text, (self.x, self.y))

    def increment_score(self):
        self.score += 1
        self.update()

    def decrement_score(self):
        self.score -= 1
        self.update()
