import pygame, sys
from pygame.locals import *
from random import randrange

class obstacle:
    def __init__(self,param,type=1):#list image et l'obstacle est choisie a l'aleatoire
        self.param = param
        self.x = param.width - 10
        self.y = param.hight - 20
        self.rec = Rect(self.x,self.y, 10, 20)
        self.out = False
    def animate(self,screen):      
        self.x -= self.param.vitesse
        self.rec = Rect(self.x,self.y, 10, 20)
        pygame.draw.rect(screen, 0, self.rec)
        if self.x < 0 :
           self.out = True 
        
class obstacleGenerator :
    def __init__(self,param,max=2,minDist=210):
        self.param = param
        self.obstacleBuffer = []
        self.maxObstacles = max
        self.minDistance = minDist
        self.randomDistance = minDist
        self.addObstacle()
        
    def addObstacle(self):
        obstacleType = randrange(1,4)
        obstacleObject = obstacle(self.param,obstacleType)
        self.obstacleBuffer.append(obstacleObject)
    def randomize(self):
        #print len(self.obstacleBuffer)
        #print self.obstacleBuffer[-1].x
        #print '-%d' % (self.param.width -self.randomDistance)
        if (self.obstacleBuffer[-1].x < (self.param.width -self.randomDistance)):
            self.addObstacle()
            self.randomDistance = randrange(self.minDistance,self.param.width)
    def animateObstacles(self,screen):
        self.randomize()
        if self.obstacleBuffer[0].out :
            del self.obstacleBuffer[0]
        for obs in self.obstacleBuffer :
            obs.animate(screen) 
        print self.randomDistance    
      
