import pygame
from Player import player

pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Placeholder')
image=pygame.transform.scale(pygame.image.load("New Piskel/sprite_0.png"),(100,100))
p = player(screen, image, 50, 50)

running = True
while running:
    screen.fill((23, 23, 23))
    p.Update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

