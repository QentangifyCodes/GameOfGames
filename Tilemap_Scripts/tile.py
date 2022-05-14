import pygame


class Tile:
    def __init__(self, screen:pygame.Surface, position:pygame.Vector2, size:pygame.Vector2, sprite:pygame.Surface):
        self.screen = screen
        self.position = position
        self.size = size
        self.sprite = sprite

        # Hitbox
        self.hitBoxColor = (100,100,100)

    def DrawHitBox(self):
        pygame.draw.rect(self.screen, self.hitBoxColor, (self.position.x, self.position.y, self.size.x, self.size.y))

    def Update(self):
        self.DrawHitBox()