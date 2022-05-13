import pygame


class player:
    def __init__(self, screen: pygame.Surface,image,x: int, y: int):
        self.screen = screen
        self.x = x
        self.y = y
        self.image=image
    def Update(self):
        self.Draw()
        self.getInput()

    def Draw(self):
        self.screen.blit(self.image, (self.x,self.y))
    def getInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += .25
        if keys[pygame.K_LEFT]:
            self.x += -.25
