import pygame as pg
from sprites import *
import sys


class PauseButton:
    def __init__(self, x, y):
        self.image = pg.image.load(Sprites.BUTTON_UNPAUSE)  # загрузка изображения с кнопкой
        self.rect = self.image.get_rect(topleft=(x, y))  # получение прямоугольника, описывающего изображение кнопки
        self.paused = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.rect.collidepoint(x, y):
                self.paused = not self.paused
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                print("Pressed esc")
                self.paused = not self.paused

    def draw(self, surface):
        surface.blit(self.image, self.rect)
