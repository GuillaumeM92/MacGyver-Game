# Import pygame
import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen_resolution
screen_width = 600
screen_height = 600

# Key holding repeat behaviour
delay = 100
interval = 300

# Set screen resolution
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images (player, sentinel, background, walls, items, texts)
player_r = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/MacGyver_R.png").convert_alpha()
player_l = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/MacGyver_L.png").convert_alpha()
player_orientation = player_r

player_classy_r = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Classy_MacGyver_R.png").convert_alpha()
player_classy_l = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Classy_MacGyver_L.png").convert_alpha()
classy_player_orientation = player_classy_r

sentinel_r = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Sentinel_R.png").convert_alpha()
sentinel_l = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Sentinel_L.png").convert_alpha()
sentinel_orientation = sentinel_l

background_tile = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Background_tile_40x40.png").convert()
wall_tile = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Wall_tile_40x40.png").convert()

needle = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/needle.png").convert_alpha()
ether = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/ether.png").convert_alpha()
sunglasses = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/sunglasses.png").convert_alpha()

ether_text = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/text/ether_text.png").convert_alpha()
sunglasses_text = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/text/sunglasses_text.png").convert_alpha()
needle_text = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/text/needle_text.png").convert_alpha()
