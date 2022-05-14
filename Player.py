import pygame


class Player:
    def __init__(self, screen: pygame.Surface, runCycle: list, idleCycle:list, position: pygame.Vector2):
        # Screen and Position
        self.screen = screen
        self.position = position

        # Lists of Animation
        self.runCycleRight = runCycle
        self.runCycleLeft = []
        self.idleCycle = idleCycle

        self.currentAnimation = self.runCycleRight  # The current animation that is playing

        # Making the left run-cycle face left
        for image in self.runCycleRight:
            self.runCycleLeft.append(pygame.transform.flip(image, True, False))

        self.running = False  # Determining if the sprite is running or not
        self.direction = 1  # Determining what direction the sprite is facing

        # Animation Things
        self.frameNumber = 0  # The frame number
        self.frameSpeed = 0.01  # The animation speed
        # The current frame in the animation
        self.frame = pygame.transform.scale(self.currentAnimation[int(self.frameNumber)], (60, 60))
        self.rect = self.frame.get_rect()                 # Don't worry about this

    def Update(self):
        self.Draw()        # Drawing the sprite
        self.GetInput()    # Getting player input and moving the sprite

    def Draw(self):
        self.rect.center = self.position     # Centering the sprite at the current position

        self.Animate()      # Playing all animation
        self.screen.blit(self.frame, self.rect)

    def Animate(self):
        self.frameNumber += self.frameSpeed     # Playing each frame

        # Choosing what animation to play if the player is running
        if self.running:
            if self.direction == -1:
                self.currentAnimation = self.runCycleLeft
            if self.direction == 1:
                self.currentAnimation = self.runCycleRight

        # Looping animation
        if self.frameNumber >= len(self.currentAnimation):
            self.frameNumber = 0

        # Making the current frame larger
        self.frame = pygame.transform.scale(self.currentAnimation[int(self.frameNumber)], (60, 60))

    def GetInput(self):
        keys = pygame.key.get_pressed()     # Getting all keys pressed

        # Moving depending on which key is pressed
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
