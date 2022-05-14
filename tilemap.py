import pygame
from player import Player


class Tilemap:
    def __init__(self, Player: Player):
        self.Player = Player
        self.CellSize = pygame.Vector2(50, 50)
