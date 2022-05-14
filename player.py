import pygame


class Player:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.speed = 3
        self.velocity = pygame.Vector2(0, 0)

        # SENSITIVE VALUES, DO NOT EDIT
        self.gravity = -10
        self.JumpPower = 0.8
        self.Hangtime = -5
        self.JumpCount = self.Hangtime * -1
        self.HangSpeed = 0.05
        self.isJumping = False

        # Hitbox
        self.hitBoxSize = pygame.Vector2(50, 100)
        self.hitbox = pygame.Rect(50, 150, self.hitBoxSize.x, self.hitBoxSize.y)
        self.hitBoxColor = (255, 0, 0)

        # Keys
        self.rightKeys = [pygame.K_RIGHT, pygame.K_d]
        self.leftKeys = [pygame.K_LEFT, pygame.K_a]

    def DrawHitBox(self):
        pygame.draw.rect(self.screen, self.hitBoxColor, self.hitbox)

    def GetPlayerInput(self):
        keys = pygame.key.get_pressed()
        allkeys = self.rightKeys + self.leftKeys

        # MOVING IF ANY LEFT MOVING KEYS OR RIGHT MOVING KEYS ARE PRESSED
        notpressed = 0
        for key in allkeys:
            if key in self.rightKeys and keys[key]:
                self.velocity.x = self.speed
            elif key in self.leftKeys and  keys[key]:
                self.velocity.x = -self.speed
            else:
                notpressed += 1

            if notpressed > len(allkeys)-1:
                self.velocity.x = 0


        # JUMPING
        if keys[pygame.K_SPACE] and not self.isJumping:
            self.isJumping = True

    def Update(self):
        # GRAVITY
        self.hitbox.x += self.velocity.x
        self.hitbox.y -= self.velocity.y

        self.hitbox.y -= self.gravity

        self.GetPlayerInput()
        self.DrawHitBox()

        # JUMPING IF SPACE PRESSED AND RESETTING JUMP COUNT IF NOT
        if self.isJumping:
            self.Jump()
        else:
            self.JumpCount = self.Hangtime * -1

    def Jump(self):
        if self.JumpCount >= self.Hangtime:
            neg = 1
            if self.JumpCount < 0:
                neg = -1

            self.hitbox.y -= neg * self.JumpPower * (self.JumpCount ** 2)
            self.JumpCount -= self.HangSpeed
