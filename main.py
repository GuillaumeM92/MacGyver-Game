# Importing libraries
import pygame

# Initializing pygame
pygame.init()

# Setting screen resolution
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Initializing 4 keys
keys = [False, False, False, False]

# Loading images
player_img = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/MacGyver_22.png").convert_alpha()
background_tile = pygame.image.load("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/Background_tile_40x40.png").convert()
north_wall_img = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/North_Wall.png").convert()
south_wall_img = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/South_Wall.png").convert()
west_wall_img = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/West_Wall.png").convert()
east_wall_img = pygame.image.load ("C:/Users/Guillaume/PycharmProjects/MacGyver OPC Game/macgyver_resources/resource/East_Wall.png").convert()

# Defining the walls
north_wall = pygame.Rect(0,0,640,8)
south_wall = pygame.Rect(0,472,640,8)
west_wall = pygame.Rect(0,0,8,480)
east_wall = pygame.Rect(632,40,8,440)


# Creating a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.x_pos, self.y_pos = 10, 448
        self.rect = (self.x_pos, self.y_pos, 16, 22)

# Defining player's updating method
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x_pos -= .2
            self.rect = (self.x_pos - .2, self.y_pos, 16, 22)
        if keystate[pygame.K_RIGHT]:
            self.x_pos += .2
            self.rect = (self.x_pos + .2, self.y_pos, 16, 22)
        if keystate[pygame.K_UP]:
            self.y_pos -= .2
            self.rect = (self.x_pos, self.y_pos - .2, 16, 22)
        if keystate[pygame.K_DOWN]:
            self.y_pos += .2
            self.rect = (self.x_pos, self.y_pos + .2, 16, 22)


# Creating the sprites list and adding the player to it
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# looping the game
running = True
while running:

    # checking for events
    for event in pygame.event.get():

        # checking for quitting event
        if event.type == pygame.QUIT:
            running = False

    # updating sprites
    all_sprites.update()

    # drawing the background
    for x in range(40):
        for y in range(40):
            screen.blit(background_tile, (x * 40, y * 40))

    # Drawing the walls
    screen.blit(north_wall_img, north_wall)
    screen.blit(south_wall_img, south_wall)
    screen.blit(west_wall_img, west_wall)
    screen.blit(east_wall_img, east_wall)

    # drawing the sprites
    all_sprites.draw(screen)

    # flipping the display
    pygame.display.flip()

# quitting
pygame.quit()
