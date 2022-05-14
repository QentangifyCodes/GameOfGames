import pygame

class Player:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.position = pygame.Vector2(50, 350)
        self.speed = 3

        # Hitbox
        self.hitBoxSize = pygame.Vector2(50, 100)
        self.hitBoxColor = (255,0,0)

        # Keys
        self.rightKeys = [pygame.K_RIGHT, pygame.K_d]
        self.leftKeys = [pygame.K_LEFT, pygame.K_a]

    def DrawHitBox(self):
        pygame.draw.rect(self.screen, self.hitBoxColor, (self.position.x, self.position.y, self.hitBoxSize.x, self.hitBoxSize.y))

    def GetPlayerInput(self):
        keys = pygame.key.get_pressed()

        for key in self.rightKeys:
            if keys[key]:
                self.position.x += self.speed

        for key in self.leftKeys:
            if keys[key]:
                self.position.x -= self.speed

    def Update(self):
        self.GetPlayerInput()
        self.DrawHitBox()
