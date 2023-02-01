import pygame
from pygame.locals import *
import random 
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

# Road parameters
ROAD_W = 500
ROADMARK_W = 10

# Lanes limitation
RIGHT_LANE = SCREEN_WIDTH/2 + ROAD_W/4
LEFT_LANE = SCREEN_WIDTH/2 - ROAD_W/4

# Roadmark width
ROADMARK_W = 10


# Set window size
screen = pygame.display.set_mode( SIZE )

# Set window title
pygame.display.set_caption("Car game in Pygame")

# Icon
ICON = pygame.image.load("caricon.png")
pygame.display.set_icon( ICON )

# Enemy speed
speed = 1

# Game Over font
go_font = pygame.font.Font("font.ttf", 64)
go_x = 400
go_y = 400

# Game Over function
def game_over(x, y):
    go_text = go_font.render("You Lost!", True, (227, 0, 50))
    screen.blit( go_text, (x, y))


# Set background color
screen.fill((60, 220, 0))

# Update changes
pygame.display.update()

# Load car player image
car_player = pygame.image.load("mycar.png")
car_player_loc = car_player.get_rect()
car_player_loc.center = RIGHT_LANE, SCREEN_HEIGHT*0.8

# Load car enemy image
car_enemy = pygame.image.load("enemycar.png")
car_enemy_loc = car_enemy.get_rect()
car_enemy_loc.center = LEFT_LANE, SCREEN_HEIGHT*0.200

# Game loop
counter = 0
running = True
while running:

    counter += 1

    # Enemy car movement
    car_enemy_loc[1] += speed

    # Enemy car appears again
    if car_enemy_loc.y > SCREEN_HEIGHT:
        car_enemy_loc.y = -200

        # Enemy car appears again randomly
        if random.randint(0, 1) == 0:
            car_enemy_loc.center = RIGHT_LANE, -200

        else:
            car_enemy_loc.center = LEFT_LANE, -200

    # End game logic
    if car_player_loc[0] == car_enemy_loc[0] and car_enemy_loc[1] > car_player_loc[1] - 64:
        #game_over(go_x, go_y)
        print("You lost!")
        break

    for event in pygame.event.get():
        print( event ) 
        if event.type == QUIT:
            running = False

        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False   

            if event.key in [K_a, K_LEFT]:
                car_player_loc = car_player_loc.move(-ROAD_W/2, 0)

            if event.key in [K_d, K_RIGHT]:
                car_player_loc = car_player_loc.move(ROAD_W/2, 0)

    ## P2.2 - Draw the road
    pygame.draw.rect(screen, (50, 50, 50), (SCREEN_WIDTH/2  - ROAD_W/2, 0, ROAD_W, SCREEN_HEIGHT))

    ## p2.4 - Draw the roadmark
    pygame.draw.rect(screen, (255, 146, 139), (SCREEN_WIDTH/2 - ROADMARK_W/2, 0, ROADMARK_W, SCREEN_HEIGHT))

    ## p2.5 - Draw the white lines
    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 - ROAD_W/2 + ROADMARK_W * 2, 0, ROADMARK_W, SCREEN_HEIGHT))

    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 + ROAD_W/2 - ROADMARK_W * 3, 0, ROADMARK_W, SCREEN_HEIGHT))

    # Draw player 
    screen.blit(car_player, car_player_loc)
    
    # Draw enemy
    screen.blit(car_enemy, car_enemy_loc)

    # Update the app
    pygame.display.update()

