import pygame
from player import Player
from tile import Tile

class Tilemap:
    def __init__(self, player: Player):
        self.Player = player
        self.CellSize = pygame.Vector2(50, 50)
        self.Cells = []

        x, y = 0, 0
        while x < 1000:
            while y < 700:
                y += self.CellSize.y
                self.Cells.append(Tile(self.Player, self.CellSize))
            y = 0
            x += self.CellSize.y

    def Update(self):
        for cell in self.Cells:
            cell.Update()