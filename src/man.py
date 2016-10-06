"""
This module aims to manage the tux behavior.
"""
import pygame, sys
from pygame.locals import *
from sound import *


class Man:

    def __init__(self,param):
        """
            Args:
                param(param): An instance from parameters.param class, used to configure the tux's behavior.
        """
        self.sound = Sound()
        self.param=param
        self.x=param.posTux[1]# taille tux a modifie
        self.taille=65
        self.posy=param.posy-self.taille
        self.y=self.posy
        # Walking motion list
        self.pingImgWalk = [
            pygame.transform.scale(pygame.image.load('img/w1.png').convert_alpha(), (self.taille, self.taille)),
            pygame.transform.scale(pygame.image.load('img/w2.png').convert_alpha(), (self.taille, self.taille)),
            pygame.transform.scale(pygame.image.load('img/w3.png').convert_alpha(), (self.taille, self.taille)),
            pygame.transform.scale(pygame.image.load('img/w4.png').convert_alpha(), (self.taille, self.taille))
        ]

        # Jumping motion list
        self.pingImgJump = [
            pygame.transform.scale(pygame.image.load('img/j1.png').convert_alpha(), (self.taille, self.taille)),
            pygame.transform.scale(pygame.image.load('img/j2.png').convert_alpha(), (self.taille, self.taille)),
            pygame.transform.scale(pygame.image.load('img/j3.png').convert_alpha(), (self.taille, self.taille))
        ]

        # self.hurt image
        self.pingImgHurt = pygame.transform.scale(pygame.image.load('img/hurt.png').convert_alpha(), (self.taille, self.taille))

        # die image
        self.pingImgDie = [
            pygame.transform.scale(pygame.image.load('img/d1.png').convert_alpha(), (self.taille, self.taille)),
            pygame.transform.scale(pygame.image.load('img/d2.png').convert_alpha(), (self.taille, self.taille)),
            pygame.transform.scale(pygame.image.load('img/d2.png').convert_alpha(), (self.taille, self.taille)),
            pygame.transform.scale(pygame.image.load('img/d4.png').convert_alpha(), (self.taille, self.taille))
        ]

        self.hero = self.pingImgWalk[0]
        self.die = False
        self.hurt = False
        self.jump = False
        self.hero_moving_counter = 0
        self.img_walk_counter = 0
        self.i = 0
        self.indestructible = False

    def getEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if self.jump != True:
                    self.sound.jumps()
                    self.jump = True
                    self.hero_moving_counter = 0

    def collision(self, obs):
        if self.x <= obs.x and self.x + self.taille >= obs.x and self.y + self.param.tailleObs > obs.y + self.param.tolerateObsHit and self.indestructible==False :
            if self.x>self.param.posTux[0]:
                self.y = self.posy
                self.jump = False
                self.hurt = True
                self.param.obsCount=-1
            else :
                self.y = self.posy
                self.die = True
                return True
        if self.x >= obs.x :
            self.indestructible = False
        return False

    def animate(self,screen):
        if self.die == False :
            if self.hurt == False :
                if self.param.obsCount >= self.param.nbObsAdv and self.x < self.param.posTux[1]:
                    self.x += self.param.vitesse/2
                if self.jump == False :  # walk
                    self.hero_moving_counter += 1
                    if self.hero_moving_counter >= (self.param.vitesseMax + 4 -self.param.vitesse)/4:
                        self.hero_moving_counter = 0
                        self.img_walk_counter += 1
                        self.hero = self.pingImgWalk[self.img_walk_counter%4]
                else :  # self.jump == True
                    self.hero_moving_counter += 1
                    if self.hero_moving_counter < self.param.framNbPerJump/7:
                        self.hero = self.pingImgJump[0]
                        self.y -= self.param.vitesse
                    elif self.hero_moving_counter <= self.param.framNbPerJump/2 :
                        self.hero = self.pingImgJump[1]
                        self.y -= self.param.vitesse
                    else :
                        self.hero = self.pingImgJump[2]
                        if self.y + self.param.vitesse < self.param.posy :
                            self.y += self.param.vitesse
                        else:
                            self.y = self.param.posy

                    if self.hero_moving_counter >= self.param.framNbPerJump :
                        self.hero = self.pingImgWalk[self.img_walk_counter%4]
                        self.y = self.posy
                        self.jump = False
                        self.hero_moving_counter = 0

            else :  #  hurt == True
                self.indestructible = True
                self.hero = self.pingImgHurt
                if self.x > self.param.posTux[0] :
                    self.x -= self.param.vitesse/2
                if self.x <= self.param.posTux[0] :
                    self.x = self.param.posTux[0]
                    self.hurt = False

        else : #  die == True
            self.i += 1
            if self.i > 10 and self.i <= 20 :
                self.hero = self.pingImgDie[1]
            elif self.i > 20 and self.i <= 30 :
                self.hero = self.pingImgDie[2]
            elif self.i > 30 :
                self.hero = self.pingImgDie[3]
            else :
                self.hero = self.pingImgHurt

                # refresh positions
        screen.blit(self.hero,(self.x,self.y))
