from functions import *
from display import *


# define player class and move method
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.picked_up_syringe = 0
        self.picked_up_ether = 0
        self.picked_up_sunglasses = 0
        self.crafted_ether_syringe = 0

    def position(self):
        return self.x * 40, self.y * 40

    def move(self, direction):
        if direction == "up" and self.y != 0 and grid[self.y-1][self.x] != "1":
            self.y -= 1
        if direction == "down" and self.y != 14 and grid[self.y+1][self.x] != "1":
            self.y += 1
        if direction == "left" and self.x != 0 and grid[self.y][self.x-1] != "1":
            self.x -= 1
        if direction == "right" and self.x != 14 and grid[self.y][self.x+1] != "1":
            self.x += 1

    def item_pickup(self, item_position):
        if self.position == item_position:
            return True
