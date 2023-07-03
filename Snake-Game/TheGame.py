import pygame, sys, os, random, math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

# We will declare Global constant definitions.

speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPARATION = 10 # Separation between two pixels
SCREE_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP": 1,
       "DOWN": 2,
       "LEFT": 3,
       "RIGHT": 4
       }

# We Will initialize the screen
screen = pygame.display.set_mode((SCREE_HEIGHT,SCREE_HEIGHT), pygame.HWSURFACE)
# `HWSURFACE` stands for Hardware Surface which refers to using memory on the video card for storing.
# Draws as opposed to main memory.

# REsources
score_font = pygame.font.Font(None, 38)
score_numb_font = pygame.font.Font(None, 28)
game_over_font  = pygame.font.Font(None, 48)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ", 1, pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0, 0, 0)

# for clock at the left corner
gameClock = pygame.time.Clock()


def checkCollision(posA, As, posB, Bs):  # As is the size of a and Bs is the size of b
    if posA.x < posB.b + Bs and posA.x + As > posB.x and posA.y < posB.y + Bs and posA.y + As > posB.y:
        return True
    return False

# to check the boundries here we are not limiting boundries like it can pass through screnn and come from other side.

def checkLimits(snake):
    if snake.x > SCREEN_WIDTH:
        snake.x = SNAKE_SIZE
    if snake.x< 0:
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if snake.y > SCREEN_HEIGHT:



# we will define keys


def getkey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
# For Exit
            elif event.key == pygame.K_ESCAPE:
                return "exit"
# If we want to continue playing again
            elif event.key == pygame.K_y:
                return "yes"
# If we don't want to play again
            elif event.key == pygame.K_n:
                return "no"
        if event.tyoe == pygame.QUIT:
            sys.exit(0)


def endgame():
    message = game_over_font.render("Game Over", 1, pygame.Color("white"))
    message_play_again = play_again_font.render("Play Again ? (Y/N)",1, pygame.Color("green"))
    screen.blit(message, (320, 240))
# The term blit stands for Block Transfer, and .blit() is how you copy the contents of one Surface to another.
    screen.blit(message_play_again,(320+12, 240+40))

    pygame.display.flip()
    pygame.display.update()

    mKey = getkey()
    while mKey != "exit":
        if mKey == "yes":
            main()
        elif mKey == "no":
            break
        mKey = getkey()
        gameClock.tick(FPS)
    sys.exit(0)


def drawScore(score):
    score_numb = score_numb_font.render(str(score), 1, pygame.Color("red"))
    screen.blit(score_msg, (SCREEN_WIDTH - score_msg_size[0]-60, 10))
    screen.blit(score_numb, (SCREEN_WIDTH - 45, 14))


def drawGameTime(gameTime):
    game_time = score_font.render("Time: ", 1, pygame.Color("white"))
    game_time_numb  = score_numb_font.render(str(gameTime/1000), 1, pygame.Color("white"))
    screen.blit(game_time, (30, 10))
    screen.blit(game_time_numb, (105, 14))


def

def main():




