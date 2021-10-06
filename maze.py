import random


class Maze:
    def __init__(self, width):
        self.width = 2 * width + 1 # // 2 * 2 - 1
        self.height = 2 * width + 1 # // 2 * 2 - 1
        self.cells = [["#" for x in range(self.width)] for y in range(self.height)]
        self.cells[0][0] = "."
        self.cells[0][1] = "."
        self.cells[self.width - 1][self.height - 2] = "."
        self.cells[self.width - 1][self.height - 1] = "."
    def display(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.cells[j][i], end=' ')
            print("\n")

    def set_path(self, x, y):
        self.cells[y][x] = "."

    def is_wall(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        else:
            return "."

    def is_visited(self, x, y):
        if self.cells[y][x] == "#":
            return False
        else:
            return True

    def create_maze(self, x, y):
        self.set_path(x, y)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        random.shuffle(directions)
        while len(directions) > 0:
            movement = directions.pop()
            node_x = x + (movement[0] * 2)
            node_y = y + (movement[1] * 2)
            link_cells_x = x + movement[0]
            link_cells_y = y + movement[1]
            if 0 <= node_x < self.width and 0 <= node_y < self.width and self.is_visited(node_x, node_y) is False:
                self.set_path(link_cells_x, link_cells_y)
                self.create_maze(node_x, node_y)
        return


X = Maze(5)
X.create_maze(1, 1)
Maze.display(X)
