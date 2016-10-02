import pygame, sys
from pygame.locals import *

class Man:

    def __init__(self,param):
        self.x=param.posTux[0]
        self.y=param.posy
        self.param=param
        #  Walking motion list
        self.pingImgWalk = [
            pygame.image.load('w1.png').convert_alpha(),
            pygame.image.load('w2.png').convert_alpha(),
            pygame.image.load('w3.png').convert_alpha(),
            pygame.image.load('w4.png').convert_alpha()
        ]

        #  Jumping motion list
        self.pingImgJump = [
            pygame.image.load('j1.png').convert_alpha(),
            pygame.image.load('j2.png').convert_alpha(),
            pygame.image.load('j3.png').convert_alpha()
        ]

        #  self.hurt image
        self.pingImgHurt = pygame.image.load('hurt.png').convert_alpha()

        #die image
        self.pingImgDie = [
            pygame.image.load('d1.png').convert_alpha(),
            pygame.image.load('d2.png').convert_alpha(),
            pygame.image.load('d2.png').convert_alpha(),
            pygame.image.load('d4.png').convert_alpha()
        ]

        self.hero = self.pingImgWalk[0]
        position_hero = self.hero.get_rect(center=(position[0], 300))



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
                    self.hero_moving_counter = 0()


    def animate(self,screen):
        if self.die == False :
            if self.hurt == False :
                if self.jump == False :  # walk
                    self.hero_moving_counter += 1
                    if self.hero_moving_counter == 300:
                        self.hero_moving_counter = 0
                        self.hero = pingImgWalk[self.img_walk_counter%4]
                        self.img_walk_counter += 1
                else :  # self.jump == True
                    self.hero_moving_counter += 1
                    if self.hero_moving_counter < 200:
                        self.hero = pingImgJump[0]
                        if self.hero_moving_counter == 100:
                            position_self.hero.bottom += -8

                    if self.hero_moving_counter >= 200 and self.hero_moving_counter < 600 :
                        self.hero = pingImgJump[1]
                        if self.hero_moving_counter == 300:
                            position_self.hero.bottom += -20
                        if self.hero_moving_counter == 500:
                            position_self.hero.bottom += -20

                    if self.hero_moving_counter > 600:
                        self.hero = pingImgJump[2]
                        if self.hero_moving_counter == 800:
                            position_self.hero.bottom += 20
                        if self.hero_moving_counter == 1000:
                            position_self.hero.bottom += 20

                    if self.hero_moving_counter >= 1100 :
                        position_self.hero.bottom = Y  # original position
                        self.jump = False
                        self.hero_moving_counter = 0

            else :  #  hurt == True
                #indestructible = True
                self.hero = pingImgHurt
                if position_hero.x > position[1] :
                    position_hero.x -= 1
                if position_hero.x == position[1] :
                    self.hurt = False

        else : #  die == True
            self.i += 1
            if self.i > 10 and self.i <= 20 :
                self.hero = pingImgDie[1]
            elif self.i > 20 and self.i <= 30 :
                self.hero = pingImgDie[2]
            else :
                self.hero = pingImgDie[3]

"""        #  test hurt or die
        if position_self.hero.right == position_obstacle.left and position_self.hero.centerx == position[0] :
            self.hurt = True
            self.hero = pingImgHurt
        if position_self.hero.right == position_obstacle.left and position_self.hero.x == position[1] and \
                        self.die == False and indestructible == False :
            self.die = True
            self.hero = pingImgDie[0]
"""

        #refresh positions
        screen.blit(self.hero, position_self.hero)
