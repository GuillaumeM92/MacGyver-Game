# Importing libraries
import pygame
from pygame.locals import *

# Initializing pygame
pygame.init()

# Setting screen resolution
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Initializing 4 keys
keys = [False, False, False, False]

# Player Position
x_pos = 5
y_pos = 445
player_position = [x_pos, y_pos]

# Loading images
player = pygame.image.load \
    ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/MacGyver_Low.png").convert()
background_tile = pygame.image.load \
    ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Background_tile_40x40.png").convert()

# Idle Loop
while 1:

    # Drawing the screen
    screen.fill(0)
    
    # Drawing the background
    for x in range(40):
        for y in range(40):
            screen.blit(background_tile, (x*40, y*40))
            
    # Drawing the player
    screen.blit(player, player_position)
    
    # Updating the screen
    pygame.display.flip()
    
    # Looping through the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False

    # Moving player
    player_position = [x_pos, y_pos]
    if keys[0]:
        y_pos -= .2
    elif keys[2]:
        y_pos += .2
    if keys[1]:
        x_pos -= .2
    elif keys[3]:
        x_pos += .2


'''# Initializing all the squares for the 15x12 grid
squares = list(range(180))

# Splitting the squares into 12 rows of 15 squares each (except the first row)
row_00 = squares[0:16]
row_01 = squares[16:31]
row_02 = squares[31:46]
row_03 = squares[46:61]
row_04 = squares[61:75]
row_05 = squares[75:90]
row_06 = squares[90:105]
row_07 = squares[105:120]
row_08 = squares[120:135]
row_09 = squares[135:150]
row_10 = squares[150:165]
row_11 = squares[165:180]

# Building the grid
grid = [row_00, row_01, row_02, row_03, row_04, row_05, row_06, row_07, row_08,
        row_09, row_10, row_11]'''
