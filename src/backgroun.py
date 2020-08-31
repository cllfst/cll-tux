import pygame, sys
from pygame.locals import *


class Background1:#far background
    """
    this class manage the far background (**the sky**)
    """

    def __init__(self,param):

        self.param=param
        self.x = 0
        self.y = 0
        self.img=pygame.image.load("img/A1.png")
        self.img = pygame.transform.scale(self.img, (param.width, param.hight))
    def affichebg(self,screen):
	    screen.blit(self.img,(self.x,self.y))



class Background2:#closee background
    """
    this class manage the closer background (the montain)
    """
    def __init__(self,param):
        self.param=param
        self.x = 0
        self.y = 0
        self.img=pygame.image.load("img/AF2.png")
        self.img = pygame.transform.scale(self.img, (2600, param.hight))

    def affichebg(self,screen):

        screen.blit(self.img,(self.x,self.y))
        self.x-= self.param.vitesse/3
        if self.x<-1500:
            self.x=0
    def affichebgDie(self,screen):
        screen.blit(self.img,(self.x,self.y))

class Background3:#runway background

    """
    this class manage the runway background
    """

    def __init__(self,param):
        self.param=param
        self.x = 0
        self.y = 0
        self.img=pygame.image.load("img/AF3.png")
        self.img = pygame.transform.scale(self.img, (2600, param.hight))

    def affichebg(self,screen):
        screen.blit(self.img,(self.x,self.y))
        self.x-=self.param.vitesse
        if self.x<-1500:
        	self.x=0

    def affichebgDie(self,screen):
        screen.blit(self.img,(self.x,self.y))
