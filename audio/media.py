import pygame
import sys

pygame.init()

class MediaPlayer:
    def __init__(self,sound:str):
        pygame.mixer.init()
        self.sound = sound

    def load_sound(self):
        pygame.mixer.music.load(self.sound)

    def play(self):
        pygame.mixer.music.play()

    def volumeup(self):
        pass

    def volumedown(self):
        pass

    def mute(self):
        pass