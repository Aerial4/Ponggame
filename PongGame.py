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

# IMPORTING FONT
pygame.font.init()


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


# 4 SCORE SYSTEM [1, 2, 3, 4]

# 1) PLAYER SCORE
SCORE_PLAYER1 = 0
SCORE_PLAYER2 = 0

# 2) DEFINING FONT
FONT = pygame.font.SysFont("Tempus Sans ITC", 20)

# 3) TWO DIFFERENT TEXTS

TEXT1 = FONT.render("P1: 0", True, WHITE)
TEXT2 = FONT.render("P2: 0", True, WHITE)
TEXTRECT1 = TEXT1.get_rect()
TEXTRECT2 = TEXT2.get_rect()

# SHOWING KEYBINDS 
TEXT_KEY1 = FONT.render("KEYBINDS: UP, DOWN", True, WHITE)
TEXT_KEY2 = FONT.render("KEYBINDS: [W], [S]", True, WHITE)
TEXTRECT_KEY1 = TEXT1.get_rect()
TEXTRECT_KEY2 = TEXT2.get_rect()
TEXTRECT_KEY1.center = (550, 550)
TEXTRECT_KEY2.center = (100, 550)


# 4) TEXT DISPLAY COORDINATES
TEXTRECT1.center = (200, 50)
TEXTRECT2.center = (600, 50)

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
PLAYERX_COORDINATE_2 = 20
PLAYERY_COORDINATE_2 = 250

# PLAYER 2 [PLAYER POSITION IN SCREEN]
PLAYERX_COORDINATE_1 = 770
PLAYERY_COORDINATE_1 = 250

 
# DEFINING PLAYER(S), SPECIFIED COORDINATES, SIZE
PLAYER1 = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(PLAYERX_COORDINATE_2, PLAYERY_COORDINATE_2, PLAYERSIZE_X, PLAYERSIZE_Y))
PLAYER2 = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(PLAYERX_COORDINATE_1, PLAYERY_COORDINATE_1, PLAYERSIZE_X, PLAYERSIZE_Y))

# BALL [1, 2, 3]

# 1) BALL SIZE
BALLSIZE_X = 20
BALLSIZE_Y = 20

# 2) BALL COORDINATES
BALLCOORDINATE_1 = 385
BALLCOORDINATE_2 = 280

# 3) DEFINING BALL, SPECIFIED COORDINATES, SIZE
BALL = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(BALLCOORDINATE_1, BALLCOORDINATE_2, BALLSIZE_X, BALLSIZE_Y))

# WHILE PROGRAM IS RUNNING
RUNNING = True

while RUNNING:
        
    SCREEN.fill(BLACK)
    
    # DISPLAYING PLAYER SCORE
    SCREEN.blit(TEXT1, TEXTRECT1)
    SCREEN.blit(TEXT2, TEXTRECT2)

    # DISPLAYING PLAYER KEYBINDS FOR 3 SECONDS
    SCREEN.blit(TEXT_KEY1, TEXTRECT_KEY1) and SCREEN.blit(TEXT_KEY2, TEXTRECT_KEY2)
    
        
   

    # DRAWING PLAYER(S)
    PLAYER1 = pygame.draw.rect(SCREEN, WHITE, PLAYER1)
    PLAYER2 = pygame.draw.rect(SCREEN, WHITE, PLAYER2)
    # DRAWING BALL
    BALL = pygame.draw.rect(SCREEN, WHITE, BALL)
    

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
        PLAYER1.y = 500

    # PLAYER 1 HOLDING [S] DOWNWARDS
    elif PLAYER1.y == 520:
        KEYS = pygame.K_s
        PLAYER1.y = 20
  
       
    # PLAYER 2 HOLDING [ARROW KEY UP]
    if PLAYER2.y == 1:
        KEYS = pygame.K_w
        PLAYER2.y = 500

    # PLAYER 2 HOLDING [ARROW KEY DOWN]
    elif PLAYER2.y == 520:
        KEYS = pygame.K_s
        PLAYER2.y = 20
    
    # PLAYER HITTING THE BALL
    
    



  # Updates every frame
    pygame.display.flip()
    
    # jjhgghma   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    # test