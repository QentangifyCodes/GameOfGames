import pygame
from player import Player
from Tilemap_Scripts.tilemap import Tilemap

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('GameOfGames')
Clock = pygame.time.Clock()

running = True
Background = pygame.transform.scale(pygame.image.load("Tilemap_Scripts/TilemapAssets/Background.png"),
                                    (1000, 760)).convert()
TileMap = Tilemap(screen)
p1 = Player(screen, TileMap)

while running:
    Clock.tick(60)
    screen.fill((23, 23, 23))
    #screen.blit(Background, (0,0))

    TileMap.Update()
    p1.Update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
