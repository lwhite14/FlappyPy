import sys
import pygame
from pygame.locals import *

from data.Player import Bird


class GameSession:
    def __init__(self):
        pygame.init()
        self.fps = 30
        self.fpsClock = pygame.time.Clock()
        self.width, self.height = 400, 600
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.bird = Bird()


    def GameLoop(self):
        while True:
            self.screen.fill((135,206,250))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.Jump()

            #Update
            self.Update()

            #Draw
            self.Draw()

            pygame.display.flip()
            self.fpsClock.tick(self.fps)


    def Update(self):
        self.bird.Update()


    def Draw(self):
        self.bird.Draw(self.screen)