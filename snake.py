import pygame as pg


class Snake:
    def __init__(self):
        self.COLOR = (0, 255, 0)
        self.hero = pg.Surface((20, 20))
        self.hero.fill(self.COLOR)
        self.rect = self.hero.get_rect(topleft=(100, 100))

        self.speed = 3
        self.direction = (self.speed, 0)

    def move(self):
        self.hero.fill(self.COLOR)

        self.rect.move_ip(self.direction)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction = (-self.speed, 0)
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction = (self.speed, 0)
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.direction = (0, -self.speed)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction = (0, self.speed)
