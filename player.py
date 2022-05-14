import pygame

class Player:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.speed = 3
        self.gravity = -3

        # Hitbox
        self.hitBoxSize = pygame.Vector2(50, 100)
        self.hitbox = pygame.Rect(50, 350, self.hitBoxSize.x, self.hitBoxSize.y)
        self.hitBoxColor = (255,0,0)

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

    def Update(self):
        self.hitbox.y -= self.gravity
        self.GetPlayerInput()
        self.DrawHitBox()
