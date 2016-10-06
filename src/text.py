import pygame, sys
from pygame.locals import *
from sound import *


class Text:

    def __init__(self,param):
        self.param = param
        self.i = 0
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 128)
        self.gOfont = pygame.font.Font('freesansbold.ttf', 50)
        self.gOText = self.gOfont.render('GAME OVER', True, (0, 0, 0))
        self.gORect = self.gOText.get_rect()
        self.gORect.center = (self.param.width/2, self.param.hight/2)

        self.scfont = pygame.font.Font('freesansbold.ttf', 30)
        self.scText = self.scfont.render("score: "+str(self.param.score), True, GREEN)
        self.scRect = self.gOText.get_rect()
        self.scRect.center = (self.param.width-120, 100)

        self.comfont = pygame.font.Font('freesansbold.ttf', 30)
        self.comText = self.comfont.render(str(self.param.combo), True, GREEN)
        self.comRect = self.gOText.get_rect()
        self.comRect.center = (self.param.width- 120 , 50)

        self.refont = pygame.font.Font('freesansbold.ttf', 22)
        self.reText = self.refont.render("click 'R' to restart", True, (0, 0, 0))
        self.reRect = self.gOText.get_rect()
        self.reRect.center = (self.param.width/2 + 50, self.param.hight/2 + 50)

    def gameovera(self, screen):
        screen.blit(self.gOText, self.gORect)
        screen.blit(self.reText, self.reRect)
    def scorea(self, screen):
        self.scText = self.scfont.render("score: "+str(self.param.score), True, (0, 0, 0))
        screen.blit(self.scText, self.scRect)
    def comboa(self, screen): #max = 10
        if self.param.combo == self.param.comboMax:
            self.comText = self.comfont.render("combo: "+str(self.param.combo), True, (255, 0, 0))
        else:
            self.comText = self.comfont.render("combo: "+str(self.param.combo), True, (0, 0, 0))
        screen.blit(self.comText, self.comRect)
