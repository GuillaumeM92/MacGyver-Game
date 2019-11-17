# Import libraries
import random
from classes import *

level = Labyrinth()
player = Player(level)

if __name__ == "__main__":

    # Game main loop
    while running:

        # Limit the game's hardware resource consumption
        pygame.time.Clock().tick(60)

        # Define player and sentinel starting position
        player_position = player_r.get_rect(topleft=(player.position()))
        sentinel_position = sentinel_l.get_rect(topleft=(560, 560))

        # qsd
        level.setup()
        level.draw(screen)

        # Check for any event
        for event in pygame.event.get():

            # Quit event
            if event.type == QUIT:
                running = 0

            # One in ten chance to trigger the sentinel orientation change, whenever a key is pressed
            elif event.type == KEYDOWN:
                one_in_ten = random.choice(range(10))

                if one_in_ten == 9:
                    sentinel_orientation = sentinel_r
                else:
                    sentinel_orientation = sentinel_l

                # Move the player when arrow keys are pressed
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        player.move("up")
                    if event.key == K_DOWN:
                        player.move("down")
                    if event.key == K_LEFT:
                        player.move("left")
                        player_orientation = player_l
                        classy_player_orientation = player_classy_l
                    if event.key == K_RIGHT:
                        player.move("right")
                        player_orientation = player_r
                        classy_player_orientation = player_classy_r

        # Loop until all 3 items are placed correctly (not in walls)
        while syringe_check:
            # Randomly choose items position
            random_number_1 = random.randrange(1, 15)
            random_number_2 = random.randrange(1, 14)
            syringe_random_x_position = random_number_1 * 40
            syringe_random_y_position = random_number_2 * 40
            # Draw item if not in wall
            if level.structure[random_number_2][random_number_1] != "1":
                syringe_position = syringe.get_rect(topleft=(syringe_random_x_position, syringe_random_y_position))
                # Proceed to the next while loop if first loop condition is satisfied
                ether_check += 1
                syringe_check = 0

        while ether_check:

            random_number_3 = random.randrange(1, 15)
            random_number_4 = random.randrange(1, 14)
            ether_random_x_position = random_number_3 * 40
            ether_random_y_position = random_number_4 * 40

            if level.structure[random_number_4][random_number_3] != "1":
                ether_position = ether.get_rect(topleft=(ether_random_x_position, ether_random_y_position))
                sunglasses_check += 1
                ether_check = 0

        while sunglasses_check:

            random_number_5 = random.randrange(1, 15)
            random_number_6 = random.randrange(1, 14)
            sunglasses_random_x_position = random_number_5 * 40
            sunglasses_random_y_position = random_number_6 * 40

            if level.structure[random_number_6][random_number_5] != "1":
                sunglasses_position = sunglasses.get_rect(topleft=(sunglasses_random_x_position, sunglasses_random_y_position))
                # End the loops
                sunglasses_check = 0

        # Make sure all 3 items are not on top of each other
        if (random_number_1 + random_number_2) == (random_number_3 + random_number_4):
            syringe_check = 1
        if (random_number_1 + random_number_2) == (random_number_5 + random_number_6):
            syringe_check = 1
        if (random_number_3 + random_number_4) == (random_number_5 + random_number_6):
            syringe_check = 1

        # Make sure all 3 items are not on top of the laser grid
        if (random_number_1 + random_number_2) == 24:
            syringe_check = 1
        if (random_number_3 + random_number_4) == 24:
            syringe_check = 1
        if (random_number_5 + random_number_6) == 24:
            syringe_check = 1

        # Stop drawing the items if the player stepped on them, and display item pickup text
        if player_position == ether_position and picked_up_ether == 0:
            ether_text_position = pygame.Rect(0, 0, 600, 600)
            draw(ether_text, ether_text_position)
            draw_ether = 0
        # Make sure to only print the item pickup text once
        if player_position != ether_position and draw_ether == 0:
            picked_up_ether = 1

        if player_position == sunglasses_position and picked_up_sunglasses == 0:
            sunglasses_text_position = pygame.Rect(0, 0, 600, 600)
            draw(sunglasses_text, sunglasses_text_position)
            draw_sunglasses = 0
        if player_position != sunglasses_position and draw_sunglasses == 0:
            picked_up_sunglasses = 1

        if player_position == syringe_position and picked_up_syringe == 0:
            syringe_text_position = pygame.Rect(0, 0, 600, 600)
            draw(syringe_text, syringe_text_position)
            draw_syringe = 0
        if player_position != syringe_position and draw_syringe == 0:
            picked_up_syringe = 1

        # Draw the player and it's orientation, and update the model if the player picked up the sunglasses
        if draw_sunglasses == 1:
            draw(player_orientation, player_position)
        else:
            draw(classy_player_orientation, player_position)

        # Draw the sentinel and update it's orientation (random)
        draw(sentinel_orientation, sentinel_position)

        # Draw items images
        if draw_ether == 1:
            draw(ether, ether_position)
        if draw_sunglasses == 1:
            draw(sunglasses, sunglasses_position)
        if draw_syringe == 1:
            draw(syringe, syringe_position)

        # Draw inventory
        if picked_up_ether or picked_up_sunglasses or picked_up_syringe == 1:
            inventory_position = pygame.Rect(0, 0, 600, 600)
            draw(inventory, inventory_position)

        if picked_up_ether == 1 and crafted_ether_syringe == 0:
            ether_inv_position = pygame.Rect(0, 0, 600, 600)
            draw(ether_inv, ether_inv_position)

        if picked_up_sunglasses == 1:
            sunglasses_inv_position = pygame.Rect(0, 0, 600, 600)
            draw(sunglasses_inv, sunglasses_inv_position)

        if picked_up_syringe == 1 and crafted_ether_syringe == 0:
            syringe_inv_position = pygame.Rect(0, 0, 600, 600)
            draw(syringe_inv, syringe_inv_position)

        if picked_up_ether and picked_up_syringe == 1 and picked_up_ether_and_syringe == 0:
            craft_ether_syringe_position = pygame.Rect(0, 0, 600, 600)
            draw(craft_ether_syringe_text, craft_ether_syringe_position)
            if event.type == KEYDOWN and event.key == K_f:
                picked_up_ether_and_syringe = 1

        if picked_up_ether_and_syringe == 1:
            crafted_ether_syringe = 1
            ether_syringe_inv_position = pygame.Rect(0, 0, 600, 600)
            draw(ether_syringe_inv, ether_syringe_inv_position)

        # Draw laser grid
        laser_grid_position = pygame.Rect(440, 520, 40, 40)
        draw(laser_grid, laser_grid_position)

        if player_position == laser_grid_position and picked_up_sunglasses == 1:
            sunglasses_laser_grid_text_position = pygame.Rect(0, 0, 600, 600)
            draw(sunglasses_laser_grid_text, sunglasses_laser_grid_text_position)

        # Lose condition
        if player_position == sentinel_position and you_win == 0:
            you_lose = 1
        if player_position == laser_grid_position and picked_up_sunglasses == 0:
            you_lose = 2

        if you_lose == 1:
            you_lose_text_position = pygame.Rect(0, 0, 600, 600)
            draw(you_lose_text, you_lose_text_position)
            if you_lose == 1 and event.type == KEYDOWN and event.key == K_x:
                running = 0
        if you_lose == 2:
            you_lose_2_text_position = pygame.Rect(0, 0, 600, 600)
            draw(you_lose_2_text, you_lose_2_text_position)
            if you_lose == 2 and event.type == KEYDOWN and event.key == K_x:
                running = 0

        # Win condition
        if player_position == sentinel_position and crafted_ether_syringe and picked_up_sunglasses == 1:
            you_win = 1

        if you_win == 1:
            you_win_text_position = pygame.Rect(0, 0, 600, 600)
            draw(you_win_text, you_win_text_position)
            if you_win == 1 and event.type == KEYDOWN and event.key == K_x:
                running = 0

        # Update the display
        pygame.display.flip()
