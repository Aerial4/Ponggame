# Slutprojekt (PONG) - # Made by Arda

# COMMANDS TO PUBLISH [GIT.HUB]
# 1) git init
# 2) git commit
# 3) git add "pong.py"
# 4) git commit -m "comment"
# 5) git push

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
PLAYERSIZE_X = 10
PLAYERSIZE_Y= 80

# PLAYER 1 [PLAYER POSITION IN SCREEN]
PLAYERX_COORDINATE_2 = 1
PLAYERY_COORDINATE_2 = 250

# PLAYER 2 [PLAYER POSITION IN SCREEN]
PLAYERX_COORDINATE_1 = 300
PLAYERY_COORDINATE_1 = 600


# WORK IN PROGRESS
PLAYER1 = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(PLAYERX_COORDINATE_2, PLAYERY_COORDINATE_2, PLAYERSIZE_X, PLAYERSIZE_Y))
PLAYER2 = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(PLAYERX_COORDINATE_1, PLAYERY_COORDINATE_1, PLAYERSIZE_X, PLAYERSIZE_Y))


# WHILE PROGRAM IS RUNNING
RUNNING = True

while RUNNING:
     
    SCREEN.fill(BLACK)
    PLAYER2 = pygame.draw.rect(SCREEN, WHITE, PLAYER2)
    PLAYER1 = pygame.draw.rect(SCREEN, WHITE, PLAYER1)


    # KEYBINDS

    KEYS = pygame.key.get_pressed()

    # KEYBINDS [PLAYER 1]
    if KEYS[pygame.K_w]:
        PLAYER1.y -= 10 * 0.1


    if KEYS[pygame.K_s]:
        PLAYER1.y += 10 * 0.1
    
    # KEYBINDS [PLAYER 2]
    if KEYS[pygame.K_UP]:
        PLAYER2.y -= 10 * 0.1
    
    if KEYS[pygame.K_DOWN]:
        PLAYER2.y += 10 * 0.1

  # Updates every frame
    pygame.display.flip()
    
    # jjhgghh    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    # test