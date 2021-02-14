import pygame
from pygame import Rect

class Pipe:
    def __init__(self):
        pass

    def Draw(self, screen):
        pass


class Ground:
    def __init__(self):
        self.posX = 0
        self.posY = 550
        self.width = 400
        self.height = 50
        self.rect = Rect(self.posX, self.posY, self.width, self.height)

    def Draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)