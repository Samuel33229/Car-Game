import pygame
from pygame.locals import *
pygame.init()

# Windows dimention
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Set window size
screen = pygame.display.set_mode( SIZE )

# Title
pygame.display.set_caption("Car Game in Pygame")

# Background color
screen.fill((189, 236, 182))

# Icon
ICON = pygame.image.load("caricon.png")
pygame.display.set_icon( ICON )


# Window dimention
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

## P2.1 - Road parameters
ROAD_W = 500

## P2.3 - Roadmark width
ROADMARK_W = 10


# Set window size
screen = pygame.display.set_mode( SIZE )

# Set window title
pygame.display.set_caption("Car game in Pygame")

# Set icon
ICON = pygame.image.load("caricon.png")
pygame.display.set_icon(ICON)

# Set background color
screen.fill((60, 220, 0))

## P2.2 - Draw the road
pygame.draw.rect(screen, (50, 50, 50), (SCREEN_WIDTH/2  - ROAD_W/2, 0, ROAD_W, SCREEN_HEIGHT))

## p2.4 - Draw the roadmark
pygame.draw.rect(screen, (255, 146, 139), (SCREEN_WIDTH/2 - ROADMARK_W/2, 0, ROADMARK_W, SCREEN_HEIGHT))

## p2.5 - Draw the white lines
pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 - ROAD_W/2 + ROADMARK_W * 2, 0, ROADMARK_W, SCREEN_HEIGHT))

pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 + ROAD_W/2 - ROADMARK_W * 3, 0, ROADMARK_W, SCREEN_HEIGHT))

# Update changes
pygame.display.update()

# Load car player image
car_player = pygame.image.load("mycar.png")
car_player_loc = car_player.get_rect()
car_player_loc.center = SCREEN_WIDTH/2 + ROAD_W/4, SCREEN_HEIGHT*0.7

# Load car enemy image
car_enemy = pygame.image.load("enemycar.png")
car_enemy_loc = car_enemy.get_rect()
car_enemy_loc.center = SCREEN_WIDTH/2 - ROAD_W/4, SCREEN_HEIGHT*0.2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        print( event ) 
        if event.type == QUIT:
            running = False

        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False   

    # Draw player 
    screen.blit(car_player, car_player_loc)
    
    # Draw enemy
    screen.blit(car_enemy, car_enemy_loc)

    # Update the app
    pygame.display.update()

