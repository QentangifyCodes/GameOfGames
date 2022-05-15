import pygame

import player
from Enemy.LivingCreature import Creature


class Ghost(Creature):
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, health: float, player: player.Player):
        self.player = player
        self.speed = 2
        self.maxFollow = 50
        super().__init__(screen, position, self.CreateAnimation(), health)

    def CreateAnimation(self):
        IdleLeft = []
        IdleRight = []

        for x in range(3):
            IdleLeft.append(
                pygame.transform.scale(pygame.image.load(f"res/Enemy_Sprites/Ghost/sprite_{x}.png"), (57, 105)))

        for idle in IdleLeft:
            IdleRight.append(pygame.transform.flip(idle, True, False))

        Animations = {
            "IdleLeft":
                {"Speed": 0.1, "Animation": IdleLeft},
            "IdleRight":
                {"Speed": 0.1, "Animation": IdleRight}
        }

        return Animations

    def TrackPlayer(self):
        playpos = pygame.Vector2(self.player.hitbox.x, self.player.hitbox.y)
        selfpos = pygame.Vector2(self.rect.x, self.rect.y)

        dir = (playpos - selfpos)

        if dir.length() > self.maxFollow:
            dir = dir.normalize()

            if dir.x < 0:
                self.CurrentAnimation = self.Animations["IdleLeft"]
            else:
                self.CurrentAnimation = self.Animations["IdleRight"]

            self.rect.x += dir.x * self.speed
            self.rect.y += dir.y * self.speed

    def Update(self):
        self.Draw()
        self.TrackPlayer()
