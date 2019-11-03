from display import *
from labyrinth_grid import *


# Draw the tiled background image
def draw_background():
    for a in range(15):
        for b in range(15):
            screen.blit(background_tile, (a * 40, b * 40))


# Draw the walls on top of the background wherever it matches with the layout defined in labyrinth_square_grid.py
def draw_walls():
    x = 0
    y = 0

    for n in range(15 * 15):
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


# Draw function
def draw(item, position):
    screen.blit(item, position)
