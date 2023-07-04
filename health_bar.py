import pygame as pg


class Health:
    def __init__(self, display):
        self.display = display

    def show_health(self, health):
        health_bar = pg.font.SysFont(None, 30).render("Health: " + str(health), True,
                                                       (255, 255, 255))
        self.display.blit(health_bar, (600, 10))
