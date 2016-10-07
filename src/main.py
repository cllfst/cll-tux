import pygame, sys
from pygame.locals import *
from parametres import *
from test import *
from man import *
from obstacle import *
from rock import *
from backgroun import *
from sound import *
from text import *

pygame.init()
bgsong = Sound()
para = Param()
DISPLAYSURF = pygame.display.set_mode((para.width, para.hight))# setting the surface and size of window must be a "tuple"=>((,))
pygame.display.set_caption('CLL TUX,running for freedom!')#title of window
clock = pygame.time.Clock()
testo = Tester("./cllfst.png",para)
highscore = 0
while True:
    #construire object in he while to initialise
    para = Param()
    text = Text(para)
    b1 = Background1(para)
    b2 = Background2(para)
    b3 = Background3(para)
    obstacle = ObstacleGenerator(para, para.jumpDist)
    rock=Rock(para)
    tux=Man(para)
    die = False
    restart = False
    start = False
    bgsong.playStartSong()
    while start == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                start = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        testo.background(DISPLAYSURF)
        text.starta(DISPLAYSURF)
        testo.animate(DISPLAYSURF)
        pygame.display.update()
        clock.tick(30)

    bgsong.playBgSong()

    while die == False and restart == False: # main game loop

        for event in pygame.event.get():#event get returns a list of events
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
        text.scorea(DISPLAYSURF)
        text.comboa(DISPLAYSURF)
        die=tux.collision(obstacle.getObst())
        obstacle.animateObstacles(DISPLAYSURF)
        rock.animation(DISPLAYSURF)
        tux.animate(DISPLAYSURF)
        pygame.display.update()
        clock.tick(30)

    bgsong.stopSong()
    if para.score > highscore:
        bgsong.playGameOverHS()
        highscore = para.score
        para.newHS = True
    else:
        bgsong.playGameOver()
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
        text.gameovera(DISPLAYSURF)
        text.scorea(DISPLAYSURF)
        text.comboa(DISPLAYSURF)
        if para.newHS == True:
            text.newHS(DISPLAYSURF)
        else:
            text.ShowHS(DISPLAYSURF,highscore)
        tux.animate(DISPLAYSURF)
        rock.animationDie(DISPLAYSURF)
        pygame.display.update()
        clock.tick(30)
