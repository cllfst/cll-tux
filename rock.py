import pygame, sys
from pygame.locals import *

class Rock:
    def __init__(self,param):
        self.param=param
        self.rockImg = pygame.image.load('img/boule.png')
        self.taille=100
        self.rockImg = pygame.transform.scale(self.rockImg, (self.taille,self.taille ))
        self.rockx = -self.taille*2/3
        self.rocky = param.posy-self.taille
        self.i=0
        self.angle=0

    def animation(self,screen):
        self.i+=1
        #if self.i%10==0 :
        #    self.rockImg=pygame.transform.rotate(self.rockImg,-370)
        self.angle-=self.param.vitesse
        #screen.blit(self.rockImg,(self.rockx,self.rocky))
        if self.i==30  and self.taille<200 :
            self.rockx-=1.5
            self.rocky-=3
            self.i=0
            self.taille+=3
            self.rockImg = pygame.image.load('img/boule.png')
            self.rockImg = pygame.transform.scale(self.rockImg, (self.taille,self.taille ))
        screen.blit(pygame.transform.rotate(self.rockImg,self.angle),(self.rockx,self.rocky))
