"""
This module aims to manage the tux behavior.
"""
import pygame, sys
from pygame.locals import *


class Man:

    def __init__(self,param):
        """
            Args:
                param(param): An instance from parameters.param class, used to configure the tux's behavior.
        """
        self.x=param.posTux[0]#-taille tux a modifie
        self.posy=param.posy-100
        self.y=self.posy

        self.param=param
        #  Walking motion list
        self.pingImgWalk = [
            pygame.image.load('img/w1.png').convert_alpha(),
            pygame.image.load('img/w2.png').convert_alpha(),
            pygame.image.load('img/w3.png').convert_alpha(),
            pygame.image.load('img/w4.png').convert_alpha()
        ]

        #  Jumping motion list
        self.pingImgJump = [
            pygame.image.load('img/j1.png').convert_alpha(),
            pygame.image.load('img/j2.png').convert_alpha(),
            pygame.image.load('img/j3.png').convert_alpha()
        ]

        #  self.hurt image
        self.pingImgHurt = pygame.image.load('img/hurt.png').convert_alpha()

        #die image
        self.pingImgDie = [
            pygame.image.load('img/d1.png').convert_alpha(),
            pygame.image.load('img/d2.png').convert_alpha(),
            pygame.image.load('img/d2.png').convert_alpha(),
            pygame.image.load('img/d4.png').convert_alpha()
        ]

        self.hero = self.pingImgWalk[0]
        self.die = False
        self.hurt = False
        self.jump = False
        self.hero_moving_counter = 0
        self.img_walk_counter = 0
        self.i = 0
        #indestructible = False

    def getEvent(self,event):


        if event.type == KEYDOWN:
            if event.key == K_UP:
                if self.jump != True:
                    self.jump = True
                    self.hero_moving_counter = 0


    def animate(self,screen):
        if self.die == False :
            if self.hurt == False :
                if self.jump == False :  # walk
                    self.hero_moving_counter += 1
                    if self.hero_moving_counter == 7:
                        self.hero_moving_counter = 0
                        self.hero = self.pingImgWalk[self.img_walk_counter%4]
                        self.img_walk_counter += 1
                else :  # self.jump == True
                    self.hero_moving_counter += 1
                    if self.hero_moving_counter < self.param.framNbPerJump/7:
                        self.hero = self.pingImgJump[0]
                        #if self.hero_moving_counter % self.param.vitesse == 0:
                        self.y -= self.param.vitesse

                    elif self.hero_moving_counter < self.param.framNbPerJump/2 :
                        self.hero = self.pingImgJump[1]
                        #if self.hero_moving_counter == 300 and self.hero_moving_counter > 100:
                        self.y -= self.param.vitesse
                        #if self.hero_moving_counter == 500:
                        #    self.y += -20

                    else :
                        self.hero = self.pingImgJump[2]
                        #if self.hero_moving_counter == 800:
                        self.y += self.param.vitesse
                        #if self.hero_moving_counter == 1000:
                            #self.y += self.param.vitesse

                    if self.hero_moving_counter >= self.param.framNbPerJump :
                        self.hero = self.pingImgWalk[self.img_walk_counter%4]
                        self.y = self.posy
                        self.jump = False
                        self.hero_moving_counter = 0

            else :  #  hurt == True
                #indestructible = True
                self.hero = self.pingImgHurt
                if self.x > self.param.posTux[1] :
                    self.x -= 1
                if self.x == self.param.posTux[1] :
                    self.hurt = False

        else : #  die == True
            self.i += 1
            if self.i > 10 and self.i <= 20 :
                self.hero = self.pingImgDie[1]
            elif self.i > 20 and self.i <= 30 :
                self.hero = self.pingImgDie[2]
            else :
                self.hero = self.pingImgDie[3]

                # refresh positions
        screen.blit(self.hero,(self.x,self.y))

"""        #  test hurt or die
        if position_self.hero.right == position_obstacle.left and position_self.hero.centerx == position[0] :
            self.hurt = True
            self.hero = pingImgHurt
        if position_self.hero.right == position_obstacle.left and position_self.hero.x == position[1] and \
                        self.die == False and indestructible == False :
            self.die = True
            self.hero = pingImgDie[0]
"""
