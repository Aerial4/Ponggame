# Slutprojekt (PONG) - # Made by Arda


# LIBARIES
import pygame
import random
import time


# DEFINING COLORS
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)


# SCREEN ADJUSTMENTS [1, 2, 3]

# 1) WINDOW SIZE
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 2) WINDOW SCREEN
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_TITLE = pygame.display.set_caption("Pong")

# 3) FRAMERATE
CLOCK = pygame.time.Clock()
FRAMERATE = CLOCK.tick(10)


# PLAYERS [1, 2, 3]

# 1) PLAYER SIZE AND COORDINATES
PLAYERSIZE1 = 20
PLAYERSIZE2 = 20

# PLAYER 1 [PLAYER POSITION IN SCREEN]
PLAYERX_COORDINATE_1 = 360
PLAYERY_COORDINATE_1 = 600

# PLAYER 2 [PLAYER POSITION IN SCREEN]
PLAYERX_COORDINATE_2 = 20
PLAYERY_COORDINATE_2 = 20

PLAYER1 = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(PLAYERSIZE1, PLAYERSIZE2, PLAYERX_COORDINATE_1, PLAYERY_COORDINATE_1))
PLAYER2 = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(PLAYERSIZE1, PLAYERSIZE2, PLAYERX_COORDINATE_2, PLAYERY_COORDINATE_2))

# nnnn
RUNNING = True

while RUNNING:
     
    SCREEN.fill(BLACK)

    # KEYBINDS

    KEYS = pygame.key.get_pressed()

    # KEYBINDS [PLAYER 1]
    if KEYS[pygame.K_w]:
        PLAYER1.y -= 300 * 0.1

    if KEYS[pygame.K_s]:
        PLAYER1.y += 300 * 0.1
    
    # KEYBINDS [PLAYER 2]
    if KEYS[pygame.K_UP]:
        PLAYER2.y -= 300 * 0.1
    
    if KEYS[pygame.K_DOWN]:
        PLAYER2.y -= 300 * 0.1
    
    # jjhgghh    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    # test