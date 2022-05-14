from math import floor
import pygame


class Player:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.speed = 3
        self.gravity = -5

        self.JumpPower = 0.6
        self.Hangtime = -5
        self.JumpCount = self.Hangtime*-1
        self.HangSpeed = 0.05
        self.isJumping = False

        # Hitbox
        self.hitBoxSize = pygame.Vector2(50, 100)
        self.hitbox = pygame.Rect(50, 350, self.hitBoxSize.x, self.hitBoxSize.y)
        self.hitBoxColor = (255, 0, 0)

        # Keys
        self.rightKeys = [pygame.K_RIGHT, pygame.K_d]
        self.leftKeys = [pygame.K_LEFT, pygame.K_a]

    def DrawHitBox(self):
        pygame.draw.rect(self.screen, self.hitBoxColor, self.hitbox)

    def GetPlayerInput(self):
        keys = pygame.key.get_pressed()

        for key in self.rightKeys:
            if keys[key]:
                self.hitbox.x += self.speed

        for key in self.leftKeys:
            if keys[key]:
                self.hitbox.x -= self.speed

        if keys[pygame.K_SPACE] and not self.isJumping:
            self.isJumping = True

    def Update(self):
        self.hitbox.y -= self.gravity
        self.GetPlayerInput()
        self.DrawHitBox()

        if self.isJumping:
            self.Jump()

    def Jump(self):
        if self.JumpCount >= self.Hangtime:
            neg = 1
            if self.JumpCount < 0:
                neg = -1

            self.hitbox.y -= neg*self.JumpPower*(self.JumpCount**2)
            self.JumpCount -= self.HangSpeed
            print(self.JumpCount, self.hitbox.y)
        elif floor(self.JumpCount) < 0:
            self.JumpCount = self.Hangtime*-1
            self.isJumping = False
            print("BITCHCH TF")