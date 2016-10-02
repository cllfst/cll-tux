#make object parametres
class Param:

    def __init__(self):
            self.vitesse = 6
            self.posy = 400
            self.width = 800
            self.hight = 500
            self.posTux = (120,180)
            self.jumpDist = 400
            self.framNbPerJump = self.jumpDist/self.vitesse
    def accelerate(self,aug):
        self.vitesse += aug
        self.framNbPerJump = self.jumpDist/self.vitesse
