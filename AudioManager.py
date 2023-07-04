import pygame as pg
from sprites import *


class AudioManager:
    def __init__(self, music_file, volume, is_sound):
        pg.mixer.init()
        self.music_file = music_file
        self.volume = volume
        if is_sound:
            self.sound = pg.mixer.Sound(music_file)
        else:
            self.load_music()

    def load_music(self):
        # Загрузка музыкального файла
        pg.mixer.music.load(self.music_file)
        pg.mixer.music.set_volume(self.volume)

    def play_music(self, loop=-1):
        # Воспроизведение музыки
        pg.mixer.music.play(loop)

    def play_sound(self):
        self.sound.play()

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
