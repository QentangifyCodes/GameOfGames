import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Placeholder')

running = True
while running:
    screen.fill((23, 23, 23))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()