import pygame

import player


class Tile:
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, size: pygame.Vector2, sprite: pygame.Surface,
                 player: player.Player):
        self.screen = screen
        self.position = position
        self.size = size
        self.sprite = pygame.transform.scale(sprite, size)
        self.player = player

        # Hitbox
        self.rect = self.sprite.get_rect()
        self.rect.topleft = self.position
        self.hitBoxColor = (100, 100, 100)

    def DrawHitBox(self):
        pygame.draw.rect(self.screen, self.hitBoxColor, self.rect)

    def Draw(self):
        self.screen.blit(self.sprite, self.rect)

    def Update(self):
        self.Draw()
        self.CheckForCollision()

    def CheckForCollision(self):
        if self.player.hitbox.colliderect(self.rect):
            if self.player.hitbox.y < self.rect.top:
                self.player.hitbox.bottom = self.rect.top
                self.player.isJumping = False
                self.player.velocity.y = 0
            elif self.player.hitbox.y > self.rect.centery:
                self.player.hitbox.top = self.rect.bottom
                self.player.velocity.y = self.player.gravity
                if self.player.velocity.x > 0:
                    self.player.hitbox.x += 10
