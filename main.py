# Import libraries
from display import *
from labyrinth_square_grid import *
import random

# Enable key holding
pygame.key.set_repeat(delay, interval)

# Define variables
running = 1
needle_check = 1
ether_check = 0
sunglasses_check = 0

draw_ether = 1
draw_sunglasses = 1
draw_needle = 1

picked_up_ether = 0
picked_up_sunglasses = 0
picked_up_needle = 0

j = 0
k = 0
win = 0

# Game main loop
while running:

    # Limit the game's hardware resource consumption
    pygame.time.Clock().tick(30)

    # Define player and sentinel starting position
    player_position = player_r.get_rect(topleft=(k * 40, j * 40))
    sentinel_position = sentinel_l.get_rect(topleft=(560, 560))

    # Check for any event
    for event in pygame.event.get():

        # Quit event
        if event.type == QUIT:
            running = 0

        # One in four chance to trigger the sentinel orientation change, whenever an arrow key is pressed
        elif event.type == KEYDOWN:
            one_in_four = random.choice(['a', 'b', 'c', 'd'])

            if one_in_four != 'd':
                sentinel_orientation = sentinel_r
            else:
                sentinel_orientation = sentinel_l

            # Move the player when arrow keys are pressed
            if event.key == K_UP and j != 0:
                j -= 1
                if grid[j][k] == "1":
                    j += 1

            if event.key == K_DOWN and j != 14:
                j += 1
                if grid[j][k] == "1":
                    j -= 1

            if event.key == K_LEFT and k != 0:
                player_orientation = player_l
                k -= 1
                if draw_sunglasses == 0:
                    player_orientation = classy_player_orientation = player_classy_l
            if grid[j][k] == "1":
                k += 1

            if event.key == K_RIGHT and k != 14:
                player_orientation = player_r
                k += 1
                if draw_sunglasses == 0:
                    player_orientation = classy_player_orientation = player_classy_r
            if grid[j][k] == "1":
                k -= 1

        # Win condition
        if player_position == sentinel_position and win == 0:
            print("you loose, missing items")

        if draw_needle == 0 and draw_sunglasses == 0 and draw_ether == 0:
            win = 1
            if player_position == sentinel_position and win == 1:
                print("you win")

    # Tile the background image
    for a in range(15):
        for b in range(15):
            screen.blit(background_tile, (a * 40, b * 40))

    # Draw the walls on top of the background wherever it matches with the layout in labyrinth_square_grid.py
    x = 0
    y = 0

    for n in range(15*15):
        if grid[x][y] == "0":
            y += 1
            if y == 15:
                y = 0
                x += 1

        elif grid[x][y] != "0":
            screen.blit(wall_tile, (y * 40, x * 40))
            y += 1
            if y == 15:
                y = 0
                x += 1

    # Loop until all 3 items are placed correctly (not in walls)
    while needle_check:
        # Randomly choose items position
        random_number_1 = random.randrange(15)
        random_number_2 = random.randrange(15)
        needle_random_x_position = random_number_1 * 40
        needle_random_y_position = random_number_2 * 40
        # Draw item if not in wall
        if grid[random_number_2][random_number_1] != "1":
            needle_position = needle.get_rect(topleft=(needle_random_x_position, needle_random_y_position))
            # Proceed to the next while loop if first loop condition is satisfied
            ether_check += 1
            needle_check = 0

    while ether_check:

        random_number_3 = random.randrange(15)
        random_number_4 = random.randrange(15)
        ether_random_x_position = random_number_3 * 40
        ether_random_y_position = random_number_4 * 40

        if grid[random_number_4][random_number_3] != "1":
            ether_position = ether.get_rect(topleft=(ether_random_x_position, ether_random_y_position))
            sunglasses_check += 1
            ether_check = 0

    while sunglasses_check:

        random_number_5 = random.randrange(15)
        random_number_6 = random.randrange(15)
        sunglasses_random_x_position = random_number_5 * 40
        sunglasses_random_y_position = random_number_6 * 40

        if grid[random_number_6][random_number_5] != "1":
            sunglasses_position = sunglasses.get_rect(topleft=(sunglasses_random_x_position, sunglasses_random_y_position))
            # End the loops
            sunglasses_check = 0

    # Make sure all 3 items are not on top of each other
    if (random_number_1 + random_number_2) == (random_number_3 + random_number_4):
        needle_check = 1
    if (random_number_1 + random_number_2) == (random_number_5 + random_number_6):
        needle_check = 1
    if (random_number_3 + random_number_4) == (random_number_5 + random_number_6):
        needle_check = 1

    # Make sure all 3 items are not on top of the player starting location
    if (random_number_1 + random_number_2) == 0:
        needle_check = 1
    if (random_number_3 + random_number_4) == 0:
        needle_check = 1
    if (random_number_5 + random_number_6) == 0:
        needle_check = 1

    # Make sure all 3 items are not on top of the sentinel location
    if (random_number_1 * random_number_2) == 196:
        needle_check = 1
    if (random_number_3 * random_number_4) == 196:
        needle_check = 1
    if (random_number_5 * random_number_6) == 196:
        needle_check = 1

    # Draw items images
    if draw_ether == 1:
        screen.blit(ether, ether_position)
    if draw_sunglasses == 1:
        screen.blit(sunglasses, sunglasses_position)
    if draw_needle == 1:
        screen.blit(needle, needle_position)

    # Stop drawing the items if the player stepped on them
    if player_position == ether_position and draw_ether == 1:
        ether_text_position = pygame.Rect(0, 0, 600, 600)
        screen.blit(ether_text, ether_text_position)

    if player_position == ether_position:
        draw_ether = 0
        # Draw ether text
        ether_text_position = pygame.Rect(0, 0, 600, 600)
        screen.blit(ether_text, ether_text_position)
    if event.type == KEYDOWN:
        picked_up_ether = 1

    if player_position == sunglasses_position:
        draw_sunglasses = 0
        # Draw sunglasses text
        sunglasses_text_position = pygame.Rect(0, 0, 600, 600)
        screen.blit(sunglasses_text, sunglasses_text_position)
        """"if event in pygame.event.get():
            picked_up_sunglasses = 1"""

    if player_position == needle_position and picked_up_needle == 0:
        draw_needle = 0
        # Draw needle text once
        needle_text_position = pygame.Rect(0, 0, 600, 600)
        screen.blit(needle_text, needle_text_position)
        """"if event in pygame.event.get():
            picked_up_needle = 1"""

    # Draw the player and it's orientation, and update the model if the player picked up the sunglasses
    if draw_sunglasses == 1:
        screen.blit(player_orientation, player_position)
    else:
        screen.blit(classy_player_orientation, player_position)

    # Draw the sentinel and update it's orientation (random)
    screen.blit(sentinel_orientation, sentinel_position)

    # Update the display
    pygame.display.flip()
