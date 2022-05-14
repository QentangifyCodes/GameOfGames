import pygame
import Tilemap_Scripts.tilemap


class Player:
    def __init__(self, screen: pygame.Surface, tm):
        self.screen = screen
        self.TileMap = tm

        self.speed = 5
        self.velocity = pygame.Vector2(0, 0)

        # SENSITIVE VALUES, DO NOT EDIT
        self.gravity = -7
        self.JumpPower = 0.2
        self.Hangtime = -13
        self.JumpCount = self.Hangtime * -1
        self.HangSpeed = 1
        self.isJumping = False

        # Hitbox
        self.hitBoxSize = pygame.Vector2(50, 100)
        self.hitbox = pygame.Rect(50, 350, self.hitBoxSize.x, self.hitBoxSize.y)
        self.hitBoxColor = (255, 0, 0)

        # Keys
        self.rightKeys = [pygame.K_RIGHT, pygame.K_d]
        self.leftKeys = [pygame.K_LEFT, pygame.K_a]

    def DrawHitBox(self):
        pygame.draw.rect(self.screen, self.hitBoxColor, self.hitbox)

    def GetCollided(self):
        hits = []

        for cell in self.TileMap.cells:
            if self.hitbox.colliderect(cell.rect):
                hits.append(cell)

        return hits

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
        self.hitbox.x += self.velocity.x

        hits = self.GetCollided()
        for hit in hits:
            if hit.rect.x < self.hitbox.x:
                self.hitbox.left = hit.rect.right
            else:
                self.hitbox.right = hit.rect.left

        # JUMPING
        if keys[pygame.K_SPACE] and not self.isJumping:
            self.isJumping = True

        self.hitbox.y -= self.velocity.y

        if not self.isJumping:
            self.hitbox.y -= self.gravity

        hits = self.GetCollided()
        for hit in hits:
            if hit.rect.y < self.hitbox.y:
                self.hitbox.top = hit.rect.bottom
                self.isJumping = False
            else:
                self.hitbox.bottom = hit.rect.top
                self.isJumping = False


    def Update(self):
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
        else:
            self.isJumping = False
