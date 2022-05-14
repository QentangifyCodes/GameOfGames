import pygame

import player


class Tile:
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, size: pygame.Vector2, sprite: pygame.Surface,
                 player: player.Player):
        self.screen = screen
        self.position = position
        self.size = size
        self.sprite = sprite
        self.player = player

        # Hitbox
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.hitBoxColor = (100, 100, 100)

    def DrawHitBox(self):
        pygame.draw.rect(self.screen, self.hitBoxColor, self.rect)

    def Update(self):
        self.DrawHitBox()
        self.CheckForCollision()

    def CheckForCollision(self):
        if self.player.hitbox.colliderect(self.rect):
            if self.player.hitbox.y < self.rect.topleft[1]:
                self.player.hitbox.bottom = self.rect.top
                self.player.isJumping = False
                self.player.velocity.y = 0
            if self.player.hitbox.y > self.rect.topleft[1]:
                self.player.hitbox.top = self.rect.bottom
                self.player.hitbox.y += 1
                self.player.velocity.y = -7

