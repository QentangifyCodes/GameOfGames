import pygame
from Player import Player
from data import WALK_CYCLE, IDLE_CYCLE
from tilemap import Tilemap

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 700))  # Setting Window Size
pygame.display.set_caption('Placeholder')  # Setting Window Name

p = Player(screen, WALK_CYCLE, IDLE_CYCLE, pygame.Vector2(40, 150))   # Creating player Object
tilemap = Tilemap(p)

# Game Loop
running = True
while running:
    clock.tick(60)
    screen.fill((23, 23, 23))
    tilemap.Update()
    p.Update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
