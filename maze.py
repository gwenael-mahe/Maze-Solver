import random

class Maze:

    def __init__(self, taille):
        self.width = (2 * taille + 1)
        self.grid = [["0" for i in range(self.width)] for j in range(self.width)]

    def set_path(self, x, y):
        self.grid[y][x] = "."

    def set_wall(self, x, y):
        self.grid[y][x] = "#"

    def is_visited(self, x, y):
        if self.grid[y][x] == "0":
            return False
        else:
            return True

    def direction(self):
        direction = ["N", "S", "E", "W"]
        return random.shuffle(direction)

