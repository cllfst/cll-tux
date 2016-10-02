import pygame, sys
from pygame.locals import *
from parametres import *
from test import *
from man import *
from obstacle import *
from rock import *
from backgroun import *

pygame.init()#should be called to initialise
para = param()
obstacle = obstacleGenerator(para)
rock=rock(para)
DISPLAYSURF = pygame.display.set_mode((para.width, para.hight))#setting the surface and size of window must be a "tuple"=>((,))
pygame.display.set_caption('CLL MAN,running for freedom!')#title of window
clock = pygame.time.Clock()
testo = tester("./cllfst.png",para)
testo.backgroundsound()

while True: # main game loop
    for event in pygame.event.get():  # event get returns a list of events
        testo.getEvent(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    testo.background(DISPLAYSURF)
    rock.animation(DISPLAYSURF)
    obstacle.animateObstacles(DISPLAYSURF)
    #testo.animate(DISPLAYSURF)
    pygame.display.update()
    clock.tick(30)
