import pygame as pg
from sprites import *
from box import Box


class Level:
    def __init__(self, program):
        self.WIDTH = program.WIDTH
        self.HEIGHT = program.HEIGHT
        self.boxes = []

        self.surf = pg.image.load(Sprites.BACKGROUND)
        self.surf = pg.transform.scale(self.surf, (self.WIDTH, self.HEIGHT))
        self.rect = self.surf.get_rect(topleft=(0, 0))

    def update(self, surface):
        surface.blit(self.surf, self.rect)
        for box in self.boxes:
            self.surf.blit(box.surf, box.rect)


class Level1(Level):
    def __init__(self, program):
        super().__init__(program)
        self.create_level()

    def create_level(self):
        for y in range(200, 450, 64):
            for times in range(4):
                self.boxes.append(Box(200, y))

        for x in range(400, 400 + 129, 64):
            for times in range(3):
                self.boxes.append(Box(x, 128))


class Level2(Level):
    def __init__(self, program):
        super().__init__(program)
        self.create_level()

    def create_level(self):
        for x in range(200, 480, 64):
            for y in (130, 330, 530):
                for times in range(5):
                    self.boxes.append(Box(x, y))


class Level3(Level):
    def __init__(self, program):
        super().__init__(program)
        self.create_level()

    def create_level(self):
        self.boxes.append(Box(165, 164))
        self.boxes.append(Box(165 + 64, 164))
        self.boxes.append(Box(165, 164 + 64))
        self.boxes.append(Box(165, 164 + 240))
        self.boxes.append(Box(165, 164 + 240 + 64))
        self.boxes.append(Box(165 + 64, 164 + 240 + 64))

        self.boxes.append(Box(405, 164))
        self.boxes.append(Box(405 + 64, 164))
        self.boxes.append(Box(405 + 64, 164 + 64))
        self.boxes.append(Box(405 + 64, 164 + 240))
        self.boxes.append(Box(405 + 64, 164 + 240 + 64))
        self.boxes.append(Box(405, 164 + 240 + 64))

        self.boxes.append(Box(0, 0))
        self.boxes.append(Box(0, 700 - 64))
        self.boxes.append(Box(700 - 64, 0))
        self.boxes.append(Box(700 - 64, 700 - 64))

        self.boxes.append(Box(350 - 32, 0))
        self.boxes.append(Box(0, 350 - 32))
        self.boxes.append(Box(350 - 32, 700 - 64))
        self.boxes.append(Box(700 - 64, 350 - 32))
