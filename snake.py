import pygame as pg


class Snake:
    def __init__(self):
        self.COLOR = (0, 255, 0)
        self.SIZE = 20
        self.hero = pg.Surface((self.SIZE, self.SIZE))
        self.hero.fill(self.COLOR)
        self.rect = self.hero.get_rect(topleft=(100, 100))

        self.speed = 3
        self.direction = (self.speed, 0)
        self.direction_delay = 0

    def update(self):
        self.hero.fill(self.COLOR)
        self.rect.move_ip(self.direction)

        if self.direction_delay >= self.SIZE:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.move((self.direction[1], -self.direction[0]))
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.move((-self.direction[1], self.direction[0]))

        self.direction_delay += self.speed

    def move(self, direction):
        self.direction = direction
        self.direction_delay = 0
