import pygame
from player import Player
from res.Tilemap_Scripts.tilemap import Tilemap
from Enemy.ghost import Ghost

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('GameOfGames')
Clock = pygame.time.Clock()

running = True
TileMap = Tilemap(screen)
p1 = Player(screen, TileMap)
g = Ghost(screen, pygame.Vector2(500, 500), 10, p1)

while running:
    Clock.tick(60)
    screen.fill((23, 23, 23))

    TileMap.Update()
    p1.Update()
    g.Update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
