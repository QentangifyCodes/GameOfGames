import pygame
from player import Player


class Tile:
    def __init__(self, player: Player, size:pygame.Vector2):
        self.player = player
        self.sprite = pygame.transform.scale(pygame.image.load("res/Grass.png"), size)
        self.rect = self.sprite.get_rect()

    def Update(self):
        self.player.screen.blit(self.sprite, self.rect)

        if self.player.rect.colliderect(self.rect):
            pass