import pygame
from pygame import Rect

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = [pygame.image.load("resources/yellowbird-midflap.png").convert_alpha(), pygame.image.load("resources/yellowbird-upflap.png").convert_alpha(), pygame.image.load("resources/yellowbird-downflap.png").convert_alpha()]
        self.rect = self.image[0].get_rect()
        self.animCounter = 0
        self.animCounterNextIter = 0

        self.posX = 160
        self.posY = 300
        # self.rect = Rect(self.posX, self.posY, 20, 20)
        self.rect.x, self.rect.y = self.posX, self.posY
        self.dead = False

        self.fallingValue = 1
        self.GRAVITY = 1.15
        self.isJumping = False
        self.jumpCounterTotal = 2
        self.jumpCounter = 0 

    def Update(self):
        self.Gravity()

    def ChangeRect(self):
        # self.rect = Rect(self.posX, self.posY, 20, 20)
        self.rect.x, self.rect.y = self.posX, self.posY

    def Gravity(self):
        if self.isJumping:
            self.posY -= 37.5
            self.ChangeRect()
            self.jumpCounter += 1
            if self.jumpCounter == self.jumpCounterTotal:
                self.isJumping = False
                self.jumpCounter = 0
                self.fallingValue = 1
        else:
            self.posY += self.fallingValue
            self.ChangeRect()
            self.fallingValue *= self.GRAVITY

    def Jump(self):
        if not self.dead:
            self.isJumping = True

    def Collide(self, otherRect):
        if self.rect.colliderect(otherRect):
            return True
        else:
            return False

    def Draw(self, screen):
        screen.blit(self.image[self.animCounter], self.rect)
        self.animCounterNextIter += 1
        if (self.animCounterNextIter % 2) == 0:
            self.animCounter += 1
        if self.animCounter == 3:
            self.animCounter = 0
        #pygame.draw.rect(screen, (255,255,0), (self.posX, self.posY, 20, 20))