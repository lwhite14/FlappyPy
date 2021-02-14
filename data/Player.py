import pygame
from pygame import Rect

class Bird:
    def __init__(self):
        self.posX = 160
        self.posY = 300
        self.rect = Rect(self.posX, self.posY, 20, 20)

        self.fallingValue = 1
        self.GRAVITY = 1.15

        self.isJumping = False
        self.jumpCounterTotal = 2

        self.jumpCounter = 0 

    def Update(self):
        self.Gravity()

    def ChangeRect(self):
        self.rect = Rect(self.posX, self.posY, 20, 20)

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
        self.isJumping = True

    def Collide(self, otherRect):
        if self.rect.colliderect(otherRect):
            print("Died!")

    def Draw(self, screen):
        pygame.draw.rect(screen, (255,255,0), (self.posX, self.posY, 20, 20))