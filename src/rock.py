import pygame, sys
from pygame.locals import *


class rock:
    """
    This class manage the animation of the rock
    """
    def __init__(self, param, l):
        """
        Args:
            param(parameters.param): An instance from parameters.param class, used to configure the rock's behavior.
        Notes:
            If you want to change the rock image, consider change the file img/boule.png.
        """
        self.param=param
        self.rockImg = pygame.image.load('img/boule.png')
        self.taille = 100
        self.rockImg = pygame.transform.scale(self.rockImg, (self.taille, self.taille ))
        self.rockx = -self.taille/2
        self.rocky = param.posy-self.taille
        self.i=0
        self.angle=0

    def animation(self, screen):
        """starts the rock's animation process

        Args:
            screen : The screen created from pygame
        Examples:
            To create a screen you should invoke the `set_mode()`_ function::

                screen_width=700
                screen_height=400
                screen = pygame.display.set_mode([screen_width,screen_height])
                r.animation(screen)  # Where r is an instance from rock
            .. _set_mode():
                http://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
        """
        self.i+=1
        # if self.i%10==0 :
        #    self.rockImg=pygame.transform.rotate(self.rockImg,-370)
        self.angle-=self.param.vitesse
        # screen.blit(self.rockImg,(self.rockx,self.rocky))

        if self.i == 30 and self.taille<200 :
            self.rockx -= 1.5
            self.rocky -= 3
            self.i=0
            self.taille += 3
            self.rockImg = pygame.image.load('img/boule.png')
            self.rockImg = pygame.transform.scale(self.rockImg, (self.taille,self.taille ))
        screen.blit(pygame.transform.rotate(self.rockImg, self.angle), (self.rockx, self.rocky))
