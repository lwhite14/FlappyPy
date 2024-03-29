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

        self.score = Score()
        self.SetUpRound()


    def GameLoop(self):
        while self.runningGame:
            self.screen.fill((78,192,202))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.runningGame = False
                if event.type == pygame.KEYDOWN:
                    if not self.bird.dead:
                        if event.key == pygame.K_SPACE:
                            self.bird.Jump()
                    else:
                        self.SetUpRound()

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

        if self.deathFlash != None:
            if not self.deathFlash.alpha == 5:
                self.deathFlash.Update()
            else:
                self.deathFlash = None

        if not self.bird.dead:
            self.ground.Update()

            if self.bird.Collide(self.ground.rect):
                self.Die()

            for pipe in self.pipes:
                pipe.Update()
                if pipe.IsBirdPast(self.bird.posX):
                    self.score.AddScore()
                for rect in pipe.rects:
                    if self.bird.Collide(rect):
                        self.Die()


    def Draw(self):
        self.backDrop.Draw(self.screen)

        for pipe in self.pipes:
            pipe.Draw(self.screen)

        self.ground.Draw(self.screen)

        self.bird.Draw(self.screen)
        
        self.score.Draw(self.screen)

        if self.deathFlash != None:
            self.deathFlash.Draw(self.screen)


    def SetUpRound(self):
        self.bird = Bird()
        self.ground = Ground()
        self.pipes = [Pipe(450), Pipe(650), Pipe(850)]
        self.backDrop = BackDrop()
        self.deathFlash = None
        self.score.scoreCurrent = 0
        self.score.FormatScore()
    
    def Die(self):
        self.bird.dead = True
        self.score.HighScore()
        self.deathFlash = DeathFlash()


class Score:
    def __init__(self):
        self.scoreCurrent = 0
        self.scoreHigh = 0
        self.fontCurrent = pygame.font.Font("resources/arcadeclassic.ttf", 45)
        self.fontHigh = pygame.font.Font("resources/arcadeclassic.ttf", 30)
        self.textCurrent = self.fontCurrent.render(str(self.scoreCurrent), 1, (255,255,255))
        self.textHigh = self.fontHigh.render(str(self.scoreHigh), 1, (255,255,255))

    def AddScore(self):
        self.scoreCurrent += 1
        self.FormatScore()

    def FormatScore(self):
        self.textCurrent = self.fontCurrent.render(str(self.scoreCurrent), 1, (255,255,255))
        self.textHigh = self.fontHigh.render(str(self.scoreHigh), 1, (255,255,255))

    def HighScore(self):
        if self.scoreCurrent > self.scoreHigh:
            self.scoreHigh = self.scoreCurrent
        self.FormatScore()


    def Draw(self, screen):
        screen.blit(self.textCurrent, (180, 75))
        screen.blit(self.textHigh, (183, 110))


class BackDrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/background.png").convert_alpha()
        # self.rect = Rect(0, 0, 400, 600)

    def Draw(self, screen):
        screen.blit(self.image, (0, 88, 400, 600))
        screen.blit(self.image, (288, 88, 400, 600))


class DeathFlash:
    def __init__(self):
        self.alpha = 255
        self.flashSurface = pygame.Surface((1000,750), pygame.SRCALPHA)   # per-pixel alpha
        self.flashSurface.fill((255, 255, 255, self.alpha))                         # notice the alpha value in the color
        # windowSurface.blit(self.flashSurface, (0,0))

    def Update(self):
        self.alpha -= 10
        self.flashSurface.fill((255, 255, 255, self.alpha))  

    def Draw(self, screen):
        # pygame.rect.draw(screen, (255, 255, 255), self.rect)
        screen.blit(self.flashSurface, (0,0))