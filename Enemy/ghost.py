import pygame
import player
from Enemy.LivingCreature import Creature

# Ghost enemy
class Ghost(Creature):
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, player: player.Player):
        # Needed to follow the player
        self.player = player

        # Following Player
        self.speed = 3
        self.maxFollow = 150
        self.AttackDistance = 300
        self.distanceFromPlayer = 0

        # Damage
        self.Damage = 20
        self.CooldownTime = 0
        self.TimeBetweenAttack = 1

        # Health
        health = 30

        super().__init__(screen, position, self.CreateAnimation(), health)

    # Sets up animations (broken)
    def CreateAnimation(self):
        IdleLeft = []
        IdleRight = []
        AttackLeft = []
        AttackRight = []

        for x in range(3):
            IdleLeft.append(
                pygame.transform.scale(pygame.image.load(f"res/Enemy_Sprites/Ghost/Idle/sprite_{x}.png"), (57, 105)))

        for idle in IdleLeft:
            IdleRight.append(pygame.transform.flip(idle, True, False))

        Animations = {
            "IdleLeft":
                {"Speed": 0.1, "Animation": IdleLeft},
            "IdleRight":
                {"Speed": 0.1, "Animation": IdleRight},
        }

        return Animations

    # Follows the player
    def TrackPlayer(self):
        playpos = pygame.Vector2(self.player.hitbox.x, self.player.hitbox.y)
        selfpos = pygame.Vector2(self.rect.x, self.rect.y)

        self.distanceFromPlayer = (playpos - selfpos)

        dir = 0
        if self.distanceFromPlayer.length() > 0:
            dir = self.distanceFromPlayer.normalize()

        if self.distanceFromPlayer.length() > self.maxFollow:
            if dir.x < 0:
                self.SetAnimation("IdleLeft")
            else:
                self.SetAnimation("IdleRight")

            self.rect.x += dir.x * self.speed
            self.rect.y += dir.y * self.speed

        if self.distanceFromPlayer.length() < self.AttackDistance:
            self.Attack()

    # Attacks the player if in range
    def Attack(self):
        if self.CooldownTime <= 0:
            self.player.health -= self.Damage
            self.player.hitBoxColor = (0,0,0)
            self.CooldownTime = self.TimeBetweenAttack
        else:
            self.player.hitBoxColor = (255,0,0)
            self.CooldownTime -= 0.01

    # Draws the sprite and tracks the player
    def Update(self):
        self.Draw()
        self.TrackPlayer()
