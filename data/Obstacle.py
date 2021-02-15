import pygame
from pygame import Rect
from random import randint

class Pipe:
    def __init__(self, initialX):
        self.initialX = initialX

        self.image = [pygame.image.load("resources/pipe-green-top.png").convert_alpha(), pygame.image.load("resources/pipe-green-bottom.png").convert_alpha()]
        self.rects = [self.image[0].get_rect(), self.image[1].get_rect()]

        self.speed = 4
        self.gapSize = 120
        self.completed = False

        self.rects = self.GeneratePipe(initialX)

    def Update(self):
        for rect in self.rects:
            rect.x -= self.speed

        if self.rects[0].x <= -50:
            self.rects = self.GeneratePipe(550)
            self.completed = False


    def GeneratePipe(self, posX):
        output = self.rects
        randomNumber = randint(175, 375)
        lowerBound = randomNumber - (self.gapSize / 2)
        upperBound = randomNumber + (self.gapSize / 2)
        output[0].x, output[1].x = posX, posX
        output[0].y, output[1].y = lowerBound-320, upperBound
        print(output[1].y - (output[0].y + output[0].height))
        return output

    def IsBirdPast(self, birdX):
        if birdX > (self.rects[0].x + 50) and self.completed == False:
            self.completed = True
            return True

    def Draw(self, screen):
        for n in range(len(self.rects)):
            screen.blit(self.image[n], self.rects[n])
            # pygame.draw.rect(screen, (255, 0, 0), self.rects[n], 5)


class Ground:
    def __init__(self):
        self.posX = 0
        self.posY = 550
        self.width = 400
        self.height = 50
        self.rect = Rect(self.posX, self.posY, self.width, self.height)

    def Draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)