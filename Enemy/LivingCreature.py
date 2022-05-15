import pygame


class Creature:
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, Animations: dict, health: float):
        self.screen = screen

        self.Animations = Animations
        self.CurrentAnimation = self.Animations["IdleLeft"]
        self.framenumber = 0
        self.frame = self.CurrentAnimation["Animation"][0]

        self.rect = self.frame.get_rect()
        self.rect.topleft = position

        self.isAlive = True
        self.health = health

    def Animate(self):
        self.framenumber += self.CurrentAnimation["Speed"]

        if self.framenumber > len(self.CurrentAnimation["Animation"]):
            self.framenumber = 0

        self.frame = self.CurrentAnimation["Animation"][int(self.framenumber)]

    def Draw(self):
        self.Animate()
        self.screen.blit(self.frame, self.rect)

    def Damage(self, amount: float):
        if self.isAlive:
            self.health -= amount

            if self.health < 0:
                self.isAlive = False
