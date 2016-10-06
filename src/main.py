import pygame, sys
from pygame.locals import *
from parametres import *
from test import *
from man import *
from obstacle import *
from rock import *
from backgroun import *
from sound import *


#mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.init()
#pygame.mixer.init()
#print pygame.mixer.get_init()

#pygame.mixer.pre_init(44100, 16, 2, 4096)
#pygame.mixer.init()
#pygame.init()# should be called to initialise
bgsong = BgSound()
para = Param()
DISPLAYSURF = pygame.display.set_mode((para.width, para.hight))# setting the surface and size of window must be a "tuple"=>((,))
pygame.display.set_caption('CLL TUX,running for freedom!')#title of window
clock = pygame.time.Clock()
#testo = Tester("./cllfst.png",para)
#testo.backgroundsound()
while True:
    #construire object in he while to initialise
    b1 = Background1(para)
    b2 = Background2(para)
    b3 = Background3(para)
    obstacle = ObstacleGenerator(para,para.jumpDist)
    rock=Rock(para)
    tux=Man(para)
    bgsong.playBgSong()
    die = False
    restart = False
    while die == False and restart == False: # main game loop

        for event in pygame.event.get():#event get returns a list of events
            #testo.getEvent(event)
            tux.getEvent(event)
            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart = True

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        b1.affichebg(DISPLAYSURF)
        b2.affichebg(DISPLAYSURF)
        b3.affichebg(DISPLAYSURF)
        #testo.background(DISPLAYSURF)
        die=tux.collision(obstacle.getObst())
        obstacle.animateObstacles(DISPLAYSURF)
        rock.animation(DISPLAYSURF)
        #testo.animate(DISPLAYSURF)
        tux.animate(DISPLAYSURF)
        pygame.display.update()
        clock.tick(30)

    bgsong.stopBgSong()

    while restart == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        b1.affichebg(DISPLAYSURF)
        b2.affichebgDie(DISPLAYSURF)
        b3.affichebgDie(DISPLAYSURF)
        tux.animate(DISPLAYSURF)
        rock.animationDie(DISPLAYSURF)
        pygame.display.update()
        clock.tick(30)
