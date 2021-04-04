# Author Lauri Putkonen
# Create a small pygame game: e.g. moving objects on a screen.
# Video - https://youtu.be/7vtKaASa0oY

import pygame
from mobs import Mob

# PRESS ARROW OR WASD KEYS TO PASS MOBS
# ESC EXIT


# Initialize the pygame
pygame.init()
clock = pygame.time.Clock()
mobs = []

# Create screen
width = 580 # Width of the window
height = 360 # Height of the window
background = pygame.image.load("background.png")
screen = pygame.display.set_mode((width,height))

# Title and Icon (Seems icon doesn't work on linux)
pygame.display.set_caption("The Buggy game")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#Music
music = pygame.mixer.music.load("bensound-dance.mp3") #Music from www.bensound.com
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound("mixkit_win.wav")  # Sound from mixkit.co
lose_sound = pygame.mixer.Sound("mixkit_long_roar.wav") # Sound from mixkit.co


# Player character
player_pic = pygame.image.load("bug.png")
playerX = 280
playerY = 310
player_speed = 10
        
def win():
    print("You passed the game")
    win_sound.play()
    pygame.time.delay(500)
    exit(0)

def draw_player(x, y):
    screen.blit(player_pic, (x, y))

# If player go out of the screen
def playerBounds():
    global playerX, playerY
    if playerX <= 0:
        playerX = 0
    if playerX >= (width - 50):
        playerX = (width - 50)
    if playerY >= 320:
        playerY = 320
    if playerY == -50:
        win()

# Create mobs - screen, y, width, height)

mobs.append( Mob(screen, 30, width, height))
mobs.append( Mob(screen, 110, width, height))
mobs.append( Mob(screen, 190, width, height))
mobs.append( Mob(screen, 270, width, height))

# Game Loop
while True:
    clock.tick(60)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY -= player_speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY += player_speed
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX -= player_speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX += player_speed
            if event.key == pygame.K_ESCAPE:
                exit()
                
    for x in mobs:
        x.draw()
        x.move()
        if x.isCollided(playerX, playerY):
            lose_sound.play()
            playerX = 280
            playerY = 310

    playerBounds() # IF player go outs of screen
    
    draw_player(playerX, playerY)
    pygame.display.update()
