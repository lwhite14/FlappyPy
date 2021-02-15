import sys
import os
import pygame
import pygame.freetype
from pygame.locals import *
from pygame import Rect

from data.Player import Bird
from data.Obstacle import Ground, Pipe


class GameSession:
    def __init__(self):
        pygame.init()
        self.runningGame = True
        self.fps = 30
        self.fpsClock = pygame.time.Clock()
        self.width, self.height = 400, 600
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.bird = Bird()
        self.ground = Ground()
        self.pipes = [Pipe(450), Pipe(650), Pipe(850)]
        self.score = Score()
        self.backDrop = BackDrop()


    def GameLoop(self):
        while self.runningGame:
            self.screen.fill((78,192,202))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.runningGame = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.Jump()

            #Update
            self.Update()

            #Draw
            self.Draw()

            pygame.display.flip()
            self.fpsClock.tick(self.fps)

        pygame.quit()
        sys.exit()


    def Update(self):
        self.bird.Update()

        if not self.bird.dead:
            if self.bird.Collide(self.ground.rect):
                self.Die()

            for pipe in self.pipes:
                pipe.Update()
                if pipe.IsBirdPast(self.bird.posX):
                    self.score.AddScore()
                for rect in pipe.rects:
                    if self.bird.Collide(rect):
                        self.Die()

            self.ground.Update()


    def Draw(self):
        self.backDrop.Draw(self.screen)

        for pipe in self.pipes:
            pipe.Draw(self.screen)

        self.ground.Draw(self.screen)

        self.bird.Draw(self.screen)
        
        self.score.Draw(self.screen)

        

    
    def Die(self):
        self.bird.dead = True


class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font("resources/arcadeclassic.ttf", 45)
        self.text = self.font.render(str(self.score), 1, (255,255,255))

    def AddScore(self):
        self.score += 1
        self.text = self.font.render(str(self.score), 1, (255,255,255))

    def Draw(self, screen):
        screen.blit(self.text, (180, 75))


class BackDrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/background.png").convert_alpha()
        # self.rect = Rect(0, 0, 400, 600)

    def Draw(self, screen):
        screen.blit(self.image, (0, 88, 400, 600))
        screen.blit(self.image, (288, 88, 400, 600))