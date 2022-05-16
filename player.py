import pygame

# Player object class
class Player:
    def __init__(self, screen: pygame.Surface, tm):
        # Screen and tilemap objects. Needed for collision and drawing
        self.screen = screen
        self.TileMap = tm
        self.speed = 5
        self.velocity = pygame.Vector2(0, 0)

        # Dashing
        self.DashDir = 0
        self.dashing = False
        self.dashdown = 2 #dashing cool down
        # SENSITIVE VALUES, DO NOT EDIT. Jumping values
        self.gravity = -13
        self.JumpPower = 0.2
        self.Hangtime = -13
        self.JumpCount = self.Hangtime * -1
        self.HangSpeed = 1
        self.isJumping = False
        self.Grounded = False
        self.oldGravity=self.gravity

        # Hitbox
        self.hitBoxSize = pygame.Vector2(50, 100)
        self.hitbox = pygame.Rect(50, 350, self.hitBoxSize.x, self.hitBoxSize.y)
        self.hitBoxColor = (255, 0, 0)

        # Keys
        self.rightKeys = [pygame.K_RIGHT, pygame.K_d]
        self.leftKeys = [pygame.K_LEFT, pygame.K_a]
        self.jumpKeys = [pygame.K_SPACE, pygame.K_z]
        self.dashKeys = [pygame.K_c]
        self.reset = [pygame.K_r]
        self.health = 100

    # For debugging. basically draws the player's hitbox and shows their health
    def DrawHitBox(self):
        pygame.draw.rect(self.screen, self.hitBoxColor, self.hitbox)

        basefont = pygame.font.Font("res/Tilemap_Scripts/TilemapAssets/MomcakeThin.otf", 20)
        playerHealth = basefont.render(f"Player Health: {self.health}", True, (201, 196, 177))
        dashCoolDown = basefont.render(f"Dash Cool Down: {self.dashdown}", True, (201, 196, 177))
        self.screen.blit(playerHealth, (10, 10))
        self.screen.blit(dashCoolDown, (10, 40))
    # Returns everything the player has collided with
    def GetCollided(self):
        hits = []

        for cell in self.TileMap.cells:
            if self.hitbox.colliderect(cell.rect):
                hits.append(cell)

        return hits

    # Very messy. DO NOT touch this, it'll probably break. Get's payer input and checks for collision.
    def GetPlayerInput(self):
        keys = pygame.key.get_pressed()
        allkeys = self.rightKeys + self.leftKeys

        # MOVING IF ANY LEFT MOVING KEYS OR RIGHT MOVING KEYS ARE PRESSED
        notpressed = 0
        for key in allkeys:
            if key in self.rightKeys and keys[key]:
                self.velocity.x = self.speed
                self.DashDir = 1
            elif key in self.leftKeys and keys[key]:
                self.velocity.x = -self.speed
                self.DashDir = -1
            else:
                notpressed += 1

            if notpressed > len(allkeys) - 1:
                self.velocity.x = 0
        self.hitbox.x += self.velocity.x

        # Horizontal Collision
        if len(self.GetCollided()) > 0:
            hit = self.GetCollided()[0]

            hit.DrawHitBox()

            if hit.rect.bottom <= self.hitbox.bottom:
                if self.velocity.x < 0:
                    self.hitbox.left = hit.rect.right
                elif self.velocity.x > 0:
                    self.hitbox.right = hit.rect.left

        # JUMPING
        for key in self.jumpKeys:
            if keys[key] and not self.isJumping and self.Grounded:
                self.Jump()

        self.hitbox.y -= self.velocity.y

        if not self.isJumping:
            self.hitbox.y -= self.gravity

        # Vertical Collision
        hits = self.GetCollided()
        if len(hits) == 0:
            self.Grounded = False

        if len(self.GetCollided()) > 0:
            hit = self.GetCollided()[0]
            hit.DrawHitBox()
            if hit.rect.y < self.hitbox.y:
                self.hitbox.top = hit.rect.bottom
                self.isJumping = False
            else:
                self.hitbox.bottom = hit.rect.top
                self.isJumping = False
                self.Grounded = True

    # Updating the player. Drawing the player, getting input, jumping, etc.
    def Update(self):
        self.GetPlayerInput()
        self.DrawHitBox()
        self.checkDash()
        self.back()
        if self.dashing:
            self.dashdown -=0.1
        if self.dashdown <= 0:
            self.dashing=False
            self.dashdown = 2

        # JUMPING IF SPACE PRESSED AND RESETTING JUMP COUNT IF NOT
        if self.isJumping:
            self.Jump()
        else:
            self.JumpCount = self.Hangtime * -1

    # Jumping with Math (epic)
    def Jump(self):
        self.isJumping = True
        if self.JumpCount >= self.Hangtime:
            neg = 1
            if self.JumpCount < 0:
                neg = -.45

            self.hitbox.y -= neg * self.JumpPower * (self.JumpCount ** 2)
            self.JumpCount -= self.HangSpeed
        else:
            self.isJumping = False

    # Dashing (broken)
    def checkDash(self):
        keys = pygame.key.get_pressed()

        for key in self.dashKeys:
            if keys[key] and not self.dashing:
                self.gravity=0
                self.hitbox.x += 150 * self.DashDir
                self.gravity=-13
                self.dashing = True
    def back(self):
        keys = pygame.key.get_pressed()

        for key in self.reset:
            if keys[key]:
                self.hitbox.topleft=(50,350)



