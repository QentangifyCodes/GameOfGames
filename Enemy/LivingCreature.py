import pygame


# Base class for all living creatures
class Creature:
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, Animations: dict, health: float):
        self.screen = screen

        # Animation things
        self.Animations = Animations
        self.CurrentAnimation = self.Animations["IdleLeft"]
        self.framenumber = 0
        self.frame = self.CurrentAnimation["Animation"][0]

        # Hitbox
        self.rect = self.frame.get_rect()
        self.rect.topleft = position

        # Health
        self.isAlive = True
        self.health = health

    # Changes the current animation (Broken)
    def SetAnimation(self, str):
        self.CurrentAnimation = self.Animations[str]

    # Animates the creature
    def Animate(self):
        self.framenumber += self.CurrentAnimation["Speed"]

        if self.framenumber >= len(self.CurrentAnimation["Animation"]) - 1:
            self.framenumber = 0

        self.frame = self.CurrentAnimation["Animation"][int(self.framenumber)]

    # Drwas/Animates the creature
    def Draw(self):
        self.Animate()
        self.screen.blit(self.frame, self.rect)

    # Damages the creature
    def Damage(self, amount: float):
        if self.isAlive:
            self.health -= amount

            if self.health < 0:
                self.isAlive = False
