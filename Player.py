import pygame


class player:
    def __init__(self, screen: pygame.Surface, color: tuple, x: int, y: int):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y

    def Update(self):
        self.Draw()
        self.getinput()

    def Draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, 50, 100))

    def getinput(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x+=.25
        if keys[pygame.K_LEFT]:
            self.x+=-.25






