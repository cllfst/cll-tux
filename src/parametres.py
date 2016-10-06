# make object parametres
from sound import *

class Param:
    """
    This class define parameters of the application
    """
    def __init__(self):
        self.combo = 0
        self.comboMax = 10
        self.score = 0
        self.obsCount =  0
        self.vitesse = 8
        self.vitesseMax = 40
        self.posy = 500
        self.width = 1100
        self.hight = 600
        self.posTux = (120,230)
        self.jumpDist = 370
        self.framNbPerJump = self.jumpDist/self.vitesse
        self.tailleObs = 100
        self.nbObsAdv = 10
        self.tolerateObsHit = 35
        self.sound = Sound()

    def accelerate(self,aug):
        """
            manage the speed of the game

            Args:
                aug (float) : the chosen speed
        """
        self.vitesse += aug
        self.framNbPerJump = self.jumpDist/self.vitesse
