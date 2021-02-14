import sys
import pygame
from pygame.locals import QUIT


class GameSession:
    def __init__(self):
        pygame.init()
        self.fps = 10
        self.fpsClock = pygame.time.Clock()
        self.width, self.height = 400, 400
        self.screen = pygame.display.set_mode((self.width, self.height))


    def GameLoop(self):
        while True:
            self.screen.fill((135,206,250))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                    self.Update()

                    self.Draw(self.screen)

                pygame.display.flip()
                self.fpsClock.tick(self.fps)


    def Update(self):
        pass


    def Draw(self, screen):
        pass