import pygame

# EDIT THESE
WALK_CYCLE_PATH = "Player_Walk_Cycle"
WALK_FRAMES = 4

IDLE_CYCLE_PATH = ""
IDLE_FRAMES = 4

# DO NOT TOUCH!
WALK_CYCLE = []
IDLE_CYCLE = []

for i in range(WALK_FRAMES):
    WALK_CYCLE.append(pygame.image.load(f"res/{WALK_CYCLE_PATH}/sprite_{i}.png"))

for i in range(IDLE_FRAMES):
    IDLE_CYCLE.append(pygame.image.load(f"res/{WALK_CYCLE_PATH}/sprite_{i}.png"))

print(WALK_CYCLE)
