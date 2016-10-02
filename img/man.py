import  pygame

class Man:
    def __init__(self, param, img, pos, height):
        self.param = param
        self.currentImg = img[0]
        self.posX = pos[0]
        self.posY = height
        self.man = pygame.image.load(self.currentImg)
        self.rect = self.man.get_rect(center=(self.posX, self.posY))

    def loadImg(self):
        man = pygame.image.load(self.currentImg)

    def changeImge(self, img, pos):
        if self.pos == pos[0]:
            self.currentImg = pos[1]
        elif self.currentImg == pos[0]:
            self.currentImg = pos[3]

    def run(self, img):
        i = 0
        yield  i
        i += 1
        if i >= 40:
            i = 0
            self.currentImg = img[1]
            self.man = pygame.image.load(self.currentImg)

    def jump(self):
        pass

def animateMan(test):
    if (test == 'jump'):
        i = 0
