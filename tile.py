import pygame
from Player import Player


class Tile:
    def __init__(self, player: Player, size:pygame.Vector2, position:pygame.Vector2):
        self.player = player
        self.sprite = pygame.transform.scale(pygame.image.load("res/Grass.png"), size)
        self.rect = self.sprite.get_rect()
        self.position = position

    def Update(self):
        self.rect.topleft = self.position
        self.player.screen.blit(self.sprite, self.rect)

        if self.player.rect.colliderect(self.rect):
            pass