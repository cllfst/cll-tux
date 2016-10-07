import pygame, sys
from pygame.locals import *
import time
"""
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
"""

class Sound:
    def __init__(self):
        pass

    def playStartSong(self):
        pygame.mixer.music.load('sfd.ogg')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1, 27.0)

    def playBgSong(self):
        pygame.mixer.music.load('bgSong.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1, 0.0)

    def stopSong(self):
        pygame.mixer.music.stop()

    def playGameOver(self):
        pygame.mixer.music.load('Death.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(1, 0.0)

    def playGameOverHS(self):
        pygame.mixer.music.load('no_one_has.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(1, 0.0)
