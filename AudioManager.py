import pygame as pg
from sprites import *


class AudioManager:
    def __init__(self, music_file, volume):
        pg.mixer.init()
        self.music_file = music_file
        self.volume = volume
        self.load_music()

    def load_music(self):
        # Загрузка музыкального файла
        pg.mixer.music.load(self.music_file)
        pg.mixer.music.set_volume(self.volume)

    def play(self, loop=-1):
        # Воспроизведение музыки
        pg.mixer.music.play(loop)

    def pause(self):
        # Воспроизведение музыки
        pg.mixer.music.pause()

    def unpause(self):
        # Воспроизведение музыки
        pg.mixer.music.unpause()

    def set_volume(self, volume):
        # Настройка громкости проигрывания музыки
        self.volume = volume
        pg.mixer.music.set_volume(self.volume)
