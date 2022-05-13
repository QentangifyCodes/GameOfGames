import pygame


class player:
    def __init__(self, screen: pygame.Surface, runCycle: list, position: pygame.Vector2):
        self.screen = screen
        self.position = position
        self.running = False

        # Lists of Animation
        self.runCycleRight = runCycle
        self.runCycleLeft = []

        for image in self.runCycleRight:
            self.runCycleLeft.append(pygame.transform.flip(image, True, False))

        self.currentAnimation = self.runCycleRight
        self.frameNumber = 0
        self.frameSpeed = 0.01
        self.direction = 1
        self.frame = pygame.transform.scale(self.currentAnimation[int(self.frameNumber)], (60, 60))
        self.rect = self.frame.get_rect()

    def Update(self):
        self.Draw()
        self.getInput()

    def Draw(self):
        self.rect.center = self.position

        if self.running:
            self.Animate()

        self.screen.blit(self.frame, self.rect)

    def Animate(self):
        self.frameNumber += self.frameSpeed

        if self.direction == -1:
            self.currentAnimation = self.runCycleLeft
        if self.direction == 1:
            self.currentAnimation = self.runCycleRight

        if self.frameNumber >= len(self.currentAnimation):
            self.frameNumber = 0

        self.frame = pygame.transform.scale(self.currentAnimation[int(self.frameNumber)], (60, 60))

    def getInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.position.x += .25
            self.direction = 1
            self.running = True
        elif keys[pygame.K_LEFT]:
            self.position.x -= .25
            self.direction = -1
            self.running = True
        else:
            self.running = False
