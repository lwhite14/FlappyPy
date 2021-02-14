import pygame

class Bird:
    def __init__(self):
        self.posX = 200
        self.posY = 300

        self.fallingValue = 1
        self.GRAVITY = 1.15

    def Update(self):
        self.Gravity()

    def Gravity(self):
        if not self.jumping:
            self.posY += self.fallingValue
            self.fallingValue *= self.GRAVITY

    def Jump(self):
        self.posY -= 150
        self.fallingValue = 1


    def Draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.posX, self.posY, 20, 20))