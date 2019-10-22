# Importing libraries
import pygame
from pygame.locals import *

# Initializing pygame
pygame.init()

# Setting screen resolution
width, height = 600, 600
screen = pygame.display.set_mode((width, height), FULLSCREEN)

# Loading images
player_img_r = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/MacGyver_32x24_R.png").convert_alpha()
player_img_l = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/MacGyver_32x24_L.png").convert_alpha()
sentinel_img_r = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Sentinel_32x28_R.png").convert_alpha()
sentinel_img_l = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Sentinel_32x28_L.png").convert_alpha()
background_tile = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Background_tile_40x40.png").convert()
north_wall_img = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/North_Wall.png").convert()
south_wall_img = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/South_Wall.png").convert()
west_wall_img = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/West_Wall.png").convert()
east_wall_img = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/East_Wall.png").convert()

# Getting player position
player_position = player_img_r.get_rect(topleft=(8, 4))
sentinel_position = sentinel_img_l.get_rect(topleft=(606, 444))

# Enabling key holding
pygame.key.set_repeat(100, 300)

# Looping the game
running = 1

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0

        if event.type == KEYDOWN:
            if event.key == K_UP:
                player_position = player_position.move(0, -40)
            if event.key == K_DOWN:
                player_position = player_position.move(0, 40)
            if event.key == K_LEFT:
                player_position = player_position.move(-40, 0)
            if event.key == K_RIGHT:
                player_position = player_position.move(40, 0)

    if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
        print("Zone dangereuse")

    for x in range(15):
        for y in range(15):
            screen.blit(background_tile, (x * 40, y * 40))

    screen.blit(player_img_r, player_position)
    screen.blit(sentinel_img_l, sentinel_position)

    pygame.display.flip()
    
