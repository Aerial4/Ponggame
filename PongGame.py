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


# SCREEN ADJUSTMENTS [1, 2, 3, 4, 5]

# 1) WINDOW SIZE
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 2) WINDOW SCREEN
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_TITLE = pygame.display.set_caption("Pong")

# 3) FRAMERATE
CLOCK = pygame.time.Clock()
FRAMERATE = CLOCK.tick(10)

# 4) COUNTDOWN
'''
while SCREEN_TITLE == pygame.display.set_caption("GET READY"):
    time.sleep(1)
    SCREEN_TITLE = pygame.display.set_caption("5")
    time.sleep(1)
    SCREEN_TITLE = pygame.display.set_caption("4")
    time.sleep(1)
    SCREEN_TITLE = pygame.display.set_caption("3")
    time.sleep(1)
    SCREEN_TITLE = pygame.display.set_caption("2")
    time.sleep(1)
    SCREEN_TITLE = pygame.display.set_caption("1")
    time.sleep(1)
    SCREEN_TITLE = pygame.display.set_caption("START")
    time.sleep(1)
    SCREEN_TITLE = pygame.display.set_caption("Pong")
    break 
'''

# 5) SCORE TEXT [W.I.P]


# PLAYERS [1, 2, 3]

# 1) PLAYER SIZE AND COORDINATES
PLAYERSIZE_X = 10
PLAYERSIZE_Y = 80

# PLAYER 1 [PLAYER POSITION IN SCREEN]
PLAYERX_COORDINATE_2 = 1
PLAYERY_COORDINATE_2 = 250

# PLAYER 2 [PLAYER POSITION IN SCREEN]
PLAYERX_COORDINATE_1 = 790
PLAYERY_COORDINATE_1 = 250


# DEFINING PLAYER(S), SPECIFIED COORDINATES, SIZE
PLAYER1 = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(PLAYERX_COORDINATE_2, PLAYERY_COORDINATE_2, PLAYERSIZE_X, PLAYERSIZE_Y))
PLAYER2 = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(PLAYERX_COORDINATE_1, PLAYERY_COORDINATE_1, PLAYERSIZE_X, PLAYERSIZE_Y))


# WHILE PROGRAM IS RUNNING
RUNNING = True
while RUNNING:
        

    SCREEN.fill(BLACK)

    PLAYER1 = pygame.draw.rect(SCREEN, WHITE, PLAYER1)
    PLAYER2 = pygame.draw.rect(SCREEN, WHITE, PLAYER2)

    # KEYBINDS
    KEYS = pygame.key.get_pressed()

    # KEYBINDS [PLAYER 1]
    
    # UP
    if KEYS[pygame.K_w]:
        time.sleep(0.005)
        PLAYER1.y -= 10 * 0.1
    
    # DOWN
    if KEYS[pygame.K_s]:
        time.sleep(0.005)
        PLAYER1.y += 10 * 0.1
        
    

    # KEYBINDS [PLAYER 2]
        
    # UP 
    if KEYS[pygame.K_UP]:
        time.sleep(0.005)
        PLAYER2.y -= 10 * 0.1
    
    # DOWN
    if KEYS[pygame.K_DOWN]:
        time.sleep(0.005)
        PLAYER2.y += 10 * 0.1
    

    # UNIQUE BOUNDARIES [TELEPORTS THE PLAYER TO THE OPPOSITE SIDE]
    
    # PLAYER 1 HOLDING [W] UPWARDS
    if PLAYER1.y == 1:
        KEYS = pygame.K_w
        PLAYER1.y = 520
    
    # PLAYER 1 HOLDING [S] DOWNWARDS
    elif PLAYER1.y == 520:
        KEYS = pygame.K_s
        PLAYER1.y = 1
    
    if PLAYER2.y == 1:
        KEYS = pygame.K_w
        PLAYER2.y = 520
    
    elif PLAYER2.y == 520:
        KEYS = pygame.K_s
        PLAYER2.y = 1


    
    
   

      
   # elif PLAYER1.y < 3:
      # pygame.K_w = True
    
   # if PLAYER1.y == -1:
       # pygame.K_s = False
    
    
  
       
    
    #elif PLAYER1.y 

   # if PLAYER1.y == -10:
    #    KEYS[pygame.K_s]

  # Updates every frame
    pygame.display.flip()
    
    # jjhgghh    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    # test