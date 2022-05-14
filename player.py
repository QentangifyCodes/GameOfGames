import pygame


class Player:
    def __init__(self, screen: pygame.Surface, runCycle: list, idleCycle: list, position: pygame.Vector2):
        # Screen and Position
        self.screen = screen
        self.position = position
        self.speed = 4
        self.gravity = -4

        # Lists of Animation
        self.runCycleRight = runCycle
        self.runCycleLeft = []

        self.idleCycleRight = idleCycle
        self.idleCycleLeft = []
        self.currentAnimation = self.idleCycleRight

        # Making the left run-cycle face left
        for image in self.idleCycleRight:
            self.idleCycleLeft.append(pygame.transform.flip(image, True, False))

        # Making the left run-cycle face left
        for image in self.runCycleRight:
            self.runCycleLeft.append(pygame.transform.flip(image, True, False))

        self.running = False  # Determining if the sprite is running or not
        self.direction = 1  # Determining what direction the sprite is facing

        # Animation Things
        self.frameNumber = 0  # The frame number
        self.frameSpeed = 0.1  # The animation speed
        # The current frame in the animation
        self.frame = pygame.transform.scale(self.currentAnimation[0], (200, 200))
        self.rect = self.frame.get_rect()  # Don't worry about this

    def Update(self):
        self.position.y -= self.gravity
        self.Draw()  # Drawing the sprite
        self.GetInput()  # Getting player input and moving the sprite

    def Draw(self):
        self.rect.center = self.position  # Centering the sprite at the current position

        self.Animate()  # Playing all animation
        self.screen.blit(self.frame, self.rect)

    def Animate(self):
        self.frameNumber += self.frameSpeed  # Playing each frame

        # Choosing what animation to play if the player is running
        if self.direction == -1:
            if self.running:
                self.currentAnimation = self.runCycleLeft
            else:
                self.currentAnimation = self.idleCycleLeft
        if self.direction == 1:
            if self.running:
                self.currentAnimation = self.runCycleRight
            else:
                self.currentAnimation = self.idleCycleRight

        # Looping animation
        if self.frameNumber >= len(self.currentAnimation):
            self.frameNumber = 0

        # Making the current frame larger
        self.frame = pygame.transform.scale(self.currentAnimation[int(self.frameNumber)], (200,200))

    def GetInput(self):
        keys = pygame.key.get_pressed()  # Getting all keys pressed

        # Moving depending on which key is pressed
        if keys[pygame.K_RIGHT]:
            self.position.x += self.speed
            self.direction = 1
            self.running = True
        elif keys[pygame.K_LEFT]:
            self.position.x -= self.speed
            self.direction = -1
            self.running = True
        else:
            self.running = False
