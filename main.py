import pygame
from Player import Player
from data import *

pygame.init()
screen = pygame.display.set_mode((1000, 700))  # Setting Window Size
pygame.display.set_caption('Placeholder')  # Setting Window Name

p = Player(screen, WALK_CYCLE, IDLE_CYCLE, pygame.Vector2(40, 350))   # Creating Player Object

# Game Loop
running = True
while running:
    screen.fill((23, 23, 23))
    p.Update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

    #sad
