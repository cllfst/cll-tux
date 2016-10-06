import pygame, sys
from pygame.locals import *
import time

class Sound:
    def __init__(self):
        self.hurt = pygame.mixer.Sound('hurt.mp3')
        self.jump = pygame.mixer.Sound('Jump.mp3')
        self.die = pygame.mixer.Sound('hurt.mp3')

    def hurts(self):
        self.hurt.play()

    def dies(self):
        self.die.play()

    def jumps(self):
        self.jump = pygame.mixer.Sound('Jump.mp3')
        self.jump.play()


class BgSound:
    def __init__(self):
        pygame.mixer.music.load('bgSong.mp3')
        pygame.mixer.music.set_volume(0.3)
    def playBgSong(self):
        pygame.mixer.music.play(-1, 0.0)

    def stopBgSong(self):
        pygame.mixer.music.stop()
