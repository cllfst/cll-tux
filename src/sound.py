import pygame, sys
from pygame.locals import *
import time


class Sound:
    def __init__(self):
        self.hurt = pygame.mixer.Sound('hurt8bit.aiff')
        self.jump = pygame.mixer.Sound('Jump.wav')
        self.hurt.set_volume(1)
        self.jump.set_volume(0.4)

    def playStartSong(self):
        pygame.mixer.music.load('sfd.ogg')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1, 27.0)

    def playBgSong(self):
        pygame.mixer.music.load('bgSong.ogg')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1, 0.0)

    def stopSong(self):
        pygame.mixer.music.stop()

    def playGameOver(self):
        pygame.mixer.music.load('Death.ogg')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(1, 0.0)

    def playGameOverHS(self):
        pygame.mixer.music.load('winHS.ogg')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(1, 0.0)

    def hurts(self):
        self.hurt.play()

    def jumps(self):
        self.jump.play()
