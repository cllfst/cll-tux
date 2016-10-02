import pygame, sys
from pygame.locals import *

class Man:
    def __init__(self,param):
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

        #  Hurt image
        self.pingImgHurt = pygame.image.load('hurt.png').convert_alpha()

        #die image
        self.pingImgDie = [
            pygame.image.load('d1.png').convert_alpha(),
            pygame.image.load('d2.png').convert_alpha(),
            pygame.image.load('d2.png').convert_alpha(),
            pygame.image.load('d4.png').convert_alpha()
        ]

            #  Postionning of the man
            position = (350, 100)




            hero = self.pingImgWalk[0]
            DISPLAYSURF.blit(hero, (100, 100))
            position_hero = hero.get_rect(center=(position[0], 300))

            print(position_hero.x)
            print(position_hero.bottom)
            Y = position_hero.bottom

            die = False
            hurt = False
            jump = False
            obstacle_moving_counter = 0
            hero_moving_counter = 0
            img_walk_counter = 0
            i = 0
            indestructible = False

    def animate(self,screen):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if jump != True:
                    jump = True
                    hero_moving_counter = 0


    if die == False :
        if hurt == False :
            if jump == False :  # walk
                hero_moving_counter += 1
                if hero_moving_counter == 300:
                    hero_moving_counter = 0
                    hero = pingImgWalk[img_walk_counter%4]
                    img_walk_counter += 1
            else :  # Jump == True
                hero_moving_counter += 1
                if hero_moving_counter < 200:
                    hero = pingImgJump[0]
                    if hero_moving_counter == 100:
                        position_hero.bottom += -8

                if hero_moving_counter >= 200 and hero_moving_counter < 600 :
                    hero = pingImgJump[1]
                    if hero_moving_counter == 300:
                        position_hero.bottom += -20
                    if hero_moving_counter == 500:
                        position_hero.bottom += -20

                if hero_moving_counter > 600:
                    hero = pingImgJump[2]
                    if hero_moving_counter == 800:
                        position_hero.bottom += 20
                    if hero_moving_counter == 1000:
                        position_hero.bottom += 20

                if hero_moving_counter >= 1100 :
                    position_hero.bottom = Y  # original position
                    jump = False
                    hero_moving_counter = 0

        else :  #  hurt == True
            indestructible = True
            hero = pingImgHurt
            if position_hero.x > position[1] :
                position_hero.x -= 1
            if position_hero.x == position[1] :
                hurt = False

    else : #  die == True
        i += 1
        if i > 10 and i <= 20 :
            hero = pingImgDie[1]
        elif i > 20 and i <= 30 :
            hero = pingImgDie[2]
        else :
            hero = pingImgDie[3]

    #  test hurt or die
    if position_hero.right == position_obstacle.left and position_hero.centerx == position[0] :
        hurt = True
        hero = pingImgHurt
    if position_hero.right == position_obstacle.left and position_hero.x == position[1] and \
                    die == False and indestructible == False :
        die = True
        hero = pingImgDie[0]

    #  move obstacle
    obstacle_moving_counter += 1
    if obstacle_moving_counter % 10 == 0:
        k = 0
        position_obstacle.left += -1
    if position_obstacle.right == 0 :
        position_obstacle.left = 656


    #refresh positions
    DISPLAYSURF.blit(BACKGROUND, (0, 0))
    DISPLAYSURF.blit(hero, position_hero)
    DISPLAYSURF.blit(obs, position_obstacle)
