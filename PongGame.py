# Slutprojekt (PONG) - # Changes made by Arda

# COMMANDS TO PUBLISH [GIT.HUB]
# 1) git init
# 2) git commit
# 3) git add "pong.py"
# 4) git commit -m "comment"
# 5) git push

# LIBARIES
import pygame

# IMPORTING FONT
pygame.font.init()

pygame.init()



# DEFINING FONT THAT IS USED TO RENDER THE TEXT
FONT = pygame.font.SysFont("Tempus Sans ITC", 20)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Basic parameters of the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

CLOCK = pygame.time.Clock() 
FPS = 60

# PLAYER CLASS
class PLAYER:
		# Take the initial position, dimensions, speed and color of the object
	def __init__(self, posx, posy, width, height, speed, color):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		# Rect that is used to control the position and collision of the object
		self.PLAYERRECT = pygame.Rect(posx, posy, width, height)
		# Object that is blit on the screen
		self.PLAYER = pygame.draw.rect(SCREEN, self.color, self.PLAYERRECT)

	# Used to display the object on the screen
	def display(self):
		self.PLAYER = pygame.draw.rect(SCREEN, self.color, self.PLAYERRECT)

	def update(self, yFac):
		self.posy = self.posy + self.speed*yFac

		# Restricting the striker to be below the top surface of the screen
		if self.posy <= 0:
			self.posy = 0
		# Restricting the striker to be above the bottom surface of the screen
		elif self.posy + self.height >= SCREEN_HEIGHT:
			self.posy = SCREEN_HEIGHT-self.height

		# Updating the rect with the new values
		self.PLAYERRECT = (self.posx, self.posy, self.width, self.height)

	def displayScore(self, TEXT, score, x, y, color):
		TEXT = FONT.render(TEXT+str(score), True, color)
		TEXTRECT = TEXT.get_rect()
		TEXTRECT.center = (x, y)

		SCREEN.blit(TEXT, TEXTRECT)

	def getRect(self):
		return self.PLAYERRECT

# BALL CLASS
class Ball:
	def __init__(self, posx, posy, radius, speed, color):
		self.posx = posx
		self.posy = posy
		self.radius = radius
		self.speed = speed
		self.color = color
		self.xFac = 1
		self.yFac = -1
		self.ball = pygame.draw.circle(
			SCREEN, self.color, (self.posx, self.posy), self.radius)
		self.firstTime = 1

	def display(self):
		self.ball = pygame.draw.circle(
			SCREEN, self.color, (self.posx, self.posy), self.radius)

	def update(self):
		self.posx += self.speed*self.xFac
		self.posy += self.speed*self.yFac

		# IF THE BALL HITS THE TOP OR BOTTOM SURFACES, THEN THE SIGN OF 
  		# YFac IS CHANGED
		# AND IT RESULTS IN A REFLECTION
		
		if self.posy <= 0 or self.posy >= SCREEN_HEIGHT:
			self.yFac *= -1

		if self.posx <= 0 and self.firstTime:
			self.firstTime = 0
			return 1
		elif self.posx >= SCREEN_WIDTH and self.firstTime:
			self.firstTime = 0
			return -1
		else:
			return 0

	def reset(self):
		self.posx = SCREEN_WIDTH//2
		self.posy = SCREEN_HEIGHT//2
		self.xFac *= -1
		self.firstTime = 1

	# Used to reflect the ball along the X-axis
	def hit(self):
		self.xFac *= -1

	def getRect(self):
		return self.ball


# GAME MANAGER
def main():
	RUNNING = True

	# DEFINING PLAYERS/BALL
	PLAYER1 = PLAYER(20, 0, 10, 100, 10, WHITE)
	PLAYER2 = PLAYER(SCREEN_WIDTH-30, 0, 10, 100, 10, WHITE)
	BALL = Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 7, 7, WHITE)

	LISTOFPLAYERS = [PLAYER1, PLAYER2]

	# Initial parameters of the players
	PLAYER1_SCORE, PLAYER2_SCORE = 0, 0
	PLAYER1_YFAC, PLAYER2_YFAC = 0, 0

	while RUNNING:
		SCREEN.fill(BLACK)

		# EVENT HANDLING
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				RUNNING = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					PLAYER2_YFAC = -1
				if event.key == pygame.K_DOWN:
					PLAYER2_YFAC = 1
				if event.key == pygame.K_w:
					PLAYER1_YFAC = -1
				if event.key == pygame.K_s:
					PLAYER1_YFAC = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					PLAYER2_YFAC = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					PLAYER1_YFAC = 0

		# Collision detection
		for PLAYER_G in LISTOFPLAYERS:
			if pygame.Rect.colliderect(BALL.getRect(), PLAYER_G.getRect()):
				BALL.hit()

		# Updating the objects
		PLAYER1.update(PLAYER1_YFAC)
		PLAYER2.update(PLAYER2_YFAC)
		POINT = BALL.update()

		# -1 -> PLAYER 1 HAS SCORED
		# +1 -> PLAYER 2 HAS SCORED
		# 0 -> NONE OF THEM SCORED
		if POINT == -1:
			PLAYER1_SCORE += 1
		elif POINT == 1:
			PLAYER2_SCORE += 1

		# SOMEONE HAS SCORED
		# A POINT AND THE BALL IS OUT OF BOUNDS.
		# SO, WE RESET IT'S POSITION
		if POINT: 
			BALL.reset()

		# DISPLAYING THE PLAYERS AND BALL ON THE SCREEN
		PLAYER1.display()
		PLAYER2.display()
		BALL.display()

		# DISPLAYING THE SCORES OF THE PLAYERS
		PLAYER1.displayScore("P1 : ", 
						PLAYER1_SCORE, 100, 80, WHITE)
		PLAYER2.displayScore("P2 : ", 
						PLAYER1_SCORE, SCREEN_WIDTH-100, 80, WHITE)
		
		# ADD THE UNIQUE BOUNDARIES
		#if PLAYER1 
						
		pygame.display.update()
		CLOCK.tick(FPS)	 


if __name__ == "__main__":
	main()
	pygame.quit()
