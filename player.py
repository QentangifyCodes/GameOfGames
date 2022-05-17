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
        self.dashTime = 2
        self.dashdown = self.dashTime
        self.dashDistance = 300

        # SENSITIVE VALUES, DO NOT EDIT. Jumping values
        self.gravity = -13
        self.JumpPower = 0.2
        self.Hangtime = -13
        self.JumpCount = self.Hangtime * -1
        self.HangSpeed = 1
        self.isJumping = False
        self.Grounded = False
        self.canMove = True
        self.oldGravity = self.gravity

        # Hitbox
        self.hitBoxSize = pygame.Vector2(50, 100)
        self.hitbox = pygame.Rect(50, 350, self.hitBoxSize.x, self.hitBoxSize.y)
        self.hitBoxColor = (255, 0, 0)

        # Keys
        self.rightKeys = [pygame.K_RIGHT, pygame.K_d]
        self.leftKeys = [pygame.K_LEFT, pygame.K_a]
        self.jumpKeys = [pygame.K_SPACE, pygame.K_z]
        self.dashRightKeys = [pygame.K_c]
        self.dashLeftKeys = [pygame.K_x, pygame.K_q]

        self.health = 100

    # For debugging. basically draws the player's hitbox and shows their health
    def DrawHitBox(self):
        pygame.draw.rect(self.screen, self.hitBoxColor, self.hitbox)

        basefont = pygame.font.Font("res/Tilemap_Scripts/TilemapAssets/MomcakeThin.otf", 20)
        playerHealth = basefont.render(f"Player Health: {self.health}", True, (201, 196, 177))
        playerPosition = basefont.render(f"Dash Cool Down: {int(self.dashdown * 100)}", True, (201, 196, 177))
        dashCoolDown = basefont.render(f"Player Position: ({self.hitbox.x}, {self.hitbox.y})", True, (201, 196, 177))

        self.screen.blit(playerPosition, (10, 10))
        self.screen.blit(playerHealth, (10, 40))
        self.screen.blit(dashCoolDown, (10, 70))

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

        self.HandeHorizontalMovement(keys)
        self.HandleVerticalMovement(keys)
        self.HandleDash(keys)

        # JUMPING IF SPACE PRESSED AND RESETTING JUMP COUNT IF NOT
        if self.isJumping:
            self.Jump()
        else:
            self.JumpCount = self.Hangtime * -1

    # Moving Horizontally and using collision
    def HandeHorizontalMovement(self, keys):
        allkeys = self.rightKeys + self.leftKeys

        # MOVING IF ANY LEFT MOVING KEYS OR RIGHT MOVING KEYS ARE PRESSED
        notpressed = 0
        if self.canMove:
            for key in allkeys:
                if key in self.rightKeys and keys[key]:
                    self.velocity.x = self.speed
                elif key in self.leftKeys and keys[key]:
                    self.velocity.x = -self.speed
                else:
                    notpressed += 1

            if notpressed > len(allkeys) - 1:
                self.velocity.x = 0
        self.hitbox.x += self.velocity.x

        if self.hitbox.left < 0:
            self.hitbox.left = 0
        if self.hitbox.right > 1000:
            self.hitbox.right = 1000

        if len(self.GetCollided()) > 0:
            hit = self.GetCollided()[0]

            hit.DrawHitBox()

            if hit.rect.bottom <= self.hitbox.bottom:
                if self.velocity.x < 0:
                    self.hitbox.left = hit.rect.right
                elif self.velocity.x > 0:
                    self.hitbox.right = hit.rect.left

    # Moving Vertically and using collision
    def HandleVerticalMovement(self, keys):
        # JUMPING
        if self.canMove:
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

    def HandleDash(self, keys):
        if self.dashing:
            self.dashdown -= 0.05
        if self.dashdown <= 0:
            self.dashing = False
            self.dashdown = self.dashTime

        rect = self.hitbox
        x = rect.x

        for key in self.dashRightKeys:
            if keys[key] and not self.dashing:
                while rect.x < x + self.dashDistance:
                    self.canMove = False
                    rect.x += 1
                    for cell in self.TileMap.cells:
                        if rect.colliderect(cell) and cell.rect.bottom == rect.bottom:
                            self.hitbox.right = cell.rect.left
                            self.dashing = True
                            self.canMove = True
                            return
                self.canMove = True
                self.hitbox = rect
                self.dashing = True

        for key in self.dashLeftKeys:
            if keys[key] and not self.dashing:
                self.canMove = False
                while rect.x > x - self.dashDistance:
                    rect.x -= 1
                    for cell in self.TileMap.cells:
                        if rect.colliderect(cell) and cell.rect.bottom == rect.bottom:
                            self.hitbox.left = cell.rect.right
                            self.dashing = True
                            self.canMove = True
                            return

                self.hitbox = rect
                self.canMove = True
                self.dashing = True

    # Updating the player. Drawing the player, getting input, jumping, etc.
    def Update(self):
        self.GetPlayerInput()
        self.DrawHitBox()

