import pygame
import player
from Tilemap_Scripts.tile import Tile


class Tilemap:
    def __init__(self, screen: pygame.Surface, player:player.Player):
        self.screen = screen
        self.cellSize = pygame.Vector2(50, 50)
        self.cells = []
        self.tilemapTosprite = {
            "1": pygame.image.load("Tilemap_Scripts/Dirt.png")
        }
        self.player = player

        self.Read()

    def Read(self):
        lines = []

        with open("Tilemap_Scripts/tilemap.txt", "r") as f:
            lines = f.readlines()

        x, y = 0, 0
        for line in lines:
            for word in line:
                word = word.strip()
                if word == "0" or word == "\n" or word=="":
                    x += self.cellSize.y
                    continue
                else:
                    cell = Tile(self.screen, pygame.Vector2(x, y), self.cellSize,  pygame.transform.scale(
                        self.tilemapTosprite[word], self.cellSize), self.player)
                    self.cells.append(cell)

                x += self.cellSize.y
            y += self.cellSize.x
            x = 0

    def Update(self):
        for cell in self.cells:
            cell.DrawHitBox()
            cell.Update()

'''

    def CheckCollison(self, player:player.Player):
        for cell in self.cells:
            if player.hitbox.colliderect(cell.rect):
                player.hitbox.centery = cell.rect.topleft[1]-player.hitbox.height/2
                player.isJumping = False
'''
