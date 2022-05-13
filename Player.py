import pygame


class player:
    def __init__(self, screen: pygame.Surface, color: tuple, x: int, y: int):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y

    def Update(self):
        self.x += 1
        self.Draw()

    def Draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, 50, 100))


