import pygame
from pygame import Rect
from random import randint

class Pipe:
    def __init__(self, initialX):
        self.initialX = initialX

        self.speed = 4
        self.gapSize = 100
        self.rects = self.GeneratePipe(initialX)

    def Update(self):
        for rect in self.rects:
            rect.x -= self.speed

        if self.rects[0].x <= -50:
            self.rects = self.GeneratePipe(550)


    def GeneratePipe(self, posX):
        randomNumber = randint(175, 375)
        lowerBound = randomNumber - (self.gapSize / 2)
        upperBound = randomNumber + (self.gapSize / 2)
        return [Rect(posX, 0, 50, lowerBound), Rect(posX, upperBound, 50, 550-upperBound)]
        

    def Draw(self, screen):
        for rect in self.rects:
            pygame.draw.rect(screen, (255, 0, 0), rect)


class Ground:
    def __init__(self):
        self.posX = 0
        self.posY = 550
        self.width = 400
        self.height = 50
        self.rect = Rect(self.posX, self.posY, self.width, self.height)

    def Draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)