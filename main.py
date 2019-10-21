# Importing libraries
import pygame
from pygame.locals import *

# Initializing pygame
pygame.init()

# Setting screen resolution
width, height = 640, 480
screen = pygame.display.set_mode((width, height))#FULLSCREEN)

# Initializing 4 keys
keys = [False, False, False, False]

# Loading images
player = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/MacGyver_22.png").convert_alpha()
background_tile = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Background_tile_40x40.png").convert()
north_wall = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/North_Wall.png").convert()
south_wall = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/South_Wall.png").convert()
west_wall = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/West_Wall.png").convert()
east_wall = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/East_Wall.png").convert()

# Defining the walls
north_wall_rect = north_wall.get_rect()
south_wall_rect = south_wall.get_rect(topleft=(0, 472))
west_wall_rect = west_wall.get_rect()
east_wall_rect = east_wall.get_rect(topleft=(632, 40))


# Creating a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player
        self.x_pos, self.y_pos = 10, 448
        self.rect = player.get_rect(topleft=(10, 448))

# Defining player's updating method
    def update(self):
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.x_pos -= .2
            self.rect = (self.x_pos - .2, self.y_pos)
        if key_state[pygame.K_RIGHT]:
            self.x_pos += .2
            self.rect = (self.x_pos + .2, self.y_pos)
        if key_state[pygame.K_UP]:
            self.y_pos -= .2
            self.rect = (self.x_pos, self.y_pos - .2)
        if key_state[pygame.K_DOWN]:
            self.y_pos += .2
            self.rect = (self.x_pos, self.y_pos + .2)

    #def check_collision(self, sprite1):
        #col = pygame.sprite.spritecollide(player, sprite1, True)


# Creating a sprite class for objects
class Objects(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = north_wall
        self.rect = north_wall.get_rect()


# Attributing the classes
player = Player()
north_wall = Objects()
#walls = [north_wall, south_wall, west_wall, east_wall]
#walls = Objects()

# Creating the sprites list and adding the player and objects to it
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(north_wall)

# Looping the game
running = True
while running:

    #pygame.time.Clock().tick(250)

    # Checking for events
    for event in pygame.event.get():

        # checking for quitting event
        if event.type == pygame.QUIT:
            running = False

        #if player.check_collision(all_sprites):
            #player.y_pos += 0.1


    # Updating sprites
    all_sprites.update()

    # Drawing the background
    for x in range(40):
        for y in range(40):
            screen.blit(background_tile, (x * 40, y * 40))

    # Drawing the walls
    #screen.blit(north_wall, north_wall_rect)
    screen.blit(south_wall, south_wall_rect)
    screen.blit(west_wall, west_wall_rect)
    screen.blit(east_wall, east_wall_rect)

    # Drawing the sprites
    all_sprites.draw(screen)

    # Flipping the display
    pygame.display.flip()

# Quitting
pygame.quit()
