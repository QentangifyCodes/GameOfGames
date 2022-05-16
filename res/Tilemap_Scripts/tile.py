import pygame


class Tile:
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, size: pygame.Vector2, sprite: pygame.Surface):
        self.screen = screen
        self.position = position
        self.size = size
        self.sprite = pygame.transform.scale(sprite, size)

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
