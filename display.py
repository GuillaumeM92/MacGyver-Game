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
screen = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN)

# Load images (player, sentinel, background, walls, items, texts, inventory)
player_r = pygame.image.load("macgyver_resources/resource/Characters/MacGyver_R.png").convert_alpha()
player_l = pygame.image.load("macgyver_resources/resource/Characters/MacGyver_L.png").convert_alpha()
player_orientation = player_r

player_classy_r = pygame.image.load("macgyver_resources/resource/Characters/Classy_MacGyver_R.png").convert_alpha()
player_classy_l = pygame.image.load("macgyver_resources/resource/Characters/Classy_MacGyver_L.png").convert_alpha()
classy_player_orientation = player_classy_r

sentinel_r = pygame.image.load("macgyver_resources/resource/Characters/Sentinel_R.png").convert_alpha()
sentinel_l = pygame.image.load("macgyver_resources/resource/Characters/Sentinel_L.png").convert_alpha()
sentinel_orientation = sentinel_l

background_tile = pygame.image.load("macgyver_resources/resource/Background/Background_tile_40x40.png").convert()
wall_tile = pygame.image.load("macgyver_resources/resource/Background/Wall_tile_40x40.png").convert()
laser_grid = pygame.image.load("macgyver_resources/resource/Background/laser_grid_40x40.png").convert_alpha()

syringe = pygame.image.load("macgyver_resources/resource/Items/syringe.png").convert_alpha()
ether = pygame.image.load("macgyver_resources/resource/Items/ether.png").convert_alpha()
sunglasses = pygame.image.load("macgyver_resources/resource/Items/sunglasses.png").convert_alpha()

ether_text = pygame.image.load("macgyver_resources/resource/Text/EN/ether_text.png").convert_alpha()
sunglasses_text = pygame.image.load("macgyver_resources/resource/Text/EN/sunglasses_text.png").convert_alpha()
syringe_text = pygame.image.load("macgyver_resources/resource/Text/EN/syringe_text.png").convert_alpha()
craft_ether_syringe_text = pygame.image.load("macgyver_resources/resource/Text/EN/craft_ether_syringe_text.png").convert_alpha()

you_win_text = pygame.image.load("macgyver_resources/resource/Text/EN/you_win_text.png").convert()
you_lose_text = pygame.image.load("macgyver_resources/resource/Text/EN/you_lose_text.png").convert()
you_lose_2_text = pygame.image.load("macgyver_resources/resource/Text/EN/you_lose_2_text.png").convert()
sunglasses_laser_grid_text = pygame.image.load("macgyver_resources/resource/Text/EN/sunglasses_laser_grid_text.png").convert_alpha()

inventory = pygame.image.load("macgyver_resources/resource/Inventory/inventory.png").convert_alpha()
ether_inv = pygame.image.load("macgyver_resources/resource/Inventory/ether_inv.png").convert_alpha()
sunglasses_inv = pygame.image.load("macgyver_resources/resource/Inventory/sunglasses_inv.png").convert_alpha()
syringe_inv = pygame.image.load("macgyver_resources/resource/Inventory/syringe_inv.png").convert_alpha()
ether_syringe_inv = pygame.image.load("macgyver_resources/resource/Inventory/ether_syringe_inv.png").convert_alpha()
