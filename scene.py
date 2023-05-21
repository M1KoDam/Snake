import pygame as pg


class Scene:
    def __init__(self):
        self.HEIGHT = 200
        self.WIDTH = 200
        self.COLOR = (255, 255, 255)
        self.scene = pg.Surface((self.WIDTH, self.HEIGHT))
        self.scene.fill(self.COLOR)
        self.rect = self.scene.get_rect(topleft=(100, 100))

    def update(self):
        self.scene.fill(self.COLOR)
