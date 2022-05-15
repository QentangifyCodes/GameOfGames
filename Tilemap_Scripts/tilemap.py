import pygame
from Tilemap_Scripts.tile import Tile

class Tilemap:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.cellSize = pygame.Vector2(50, 50)
        self.cells = []

        self.basefont = pygame.font.Font("Tilemap_Scripts/TilemapAssets/MomcakeThin.otf", 40)
        self.tutorial_text = self.basefont.render("Press WASD or Arrow Keys to Move. Press Space or Z to Jump", True, (201, 196, 177))
        self.tutorial_text_rect = self.tutorial_text.get_rect()
        self.tutorial_text_rect.center = (500,200)


        self.tilemapTosprite = {
            "1": pygame.image.load("Tilemap_Scripts/TilemapAssets/Dirt.png"),
            "2": pygame.image.load("Tilemap_Scripts/TilemapAssets/Grass.png")
        }

        self.Read()

    def Read(self):
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
                        self.tilemapTosprite[word], self.cellSize))
                    self.cells.append(cell)

                x += self.cellSize.y
            y += self.cellSize.x
            x = 0

    def Update(self):
        self.screen.blit(self.tutorial_text, self.tutorial_text_rect)
        for cell in self.cells:
            cell.Update()

