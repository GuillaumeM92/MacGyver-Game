from display import *


# Define player class and move method
class Player:
    def __init__(self, level):
        self.x = 0
        self.y = 0
        self.picked_up_syringe = 0
        self.picked_up_ether = 0
        self.picked_up_sunglasses = 0
        self.crafted_ether_syringe = 0
        self.level = level

    def position(self):
        return self.x * 40, self.y * 40

    def move(self, direction):
        if direction == "up" and self.y != 0 and self.level.structure[self.y-1][self.x] != "1":
            self.y -= 1
        if direction == "down" and self.y != 14 and self.level.structure[self.y+1][self.x] != "1":
            self.y += 1
        if direction == "left" and self.x != 0 and self.level.structure[self.y][self.x-1] != "1":
            self.x -= 1
        if direction == "right" and self.x != 14 and self.level.structure[self.y][self.x+1] != "1":
            self.x += 1

    def item_pickup(self, item_position):
        if self.position == item_position:
            return True


# Labyrinth class
class Labyrinth:

    def __init__(self):
        self.level = "labyrinth_grid.txt"
        self.structure = 0

    def setup(self):
        with open(self.level, "r") as level:
            level_structure = []
            for row in level:
                level_row = []
                for sprite in row:
                    if sprite != '\n':
                        level_row.append(sprite)
                level_structure.append(level_row)
            self.structure = level_structure

    def draw(self, screen):
        wall = wall_tile
        background = background_tile
        start = background_tile
        finish = background_tile

        row_number = 0
        for row in self.structure:
            tile_number = 0
            for sprite in row:
                x = tile_number * 40
                y = row_number * 40
                if sprite == "1":  # 1 = Wall
                    screen.blit(wall, (x, y))
                elif sprite == "0":  # 0 = Background
                    screen.blit(background, (x, y))
                elif sprite == "S":  # S = Start
                    screen.blit(start, (x, y))
                elif sprite == "E":  # E = Exit
                    screen.blit(finish, (x, y))
                tile_number += 1
            row_number += 1
