import random


class Maze:
    def __init__(self, width, height):
        self.width = width // 2 * 2 - 1
        self.height = height // 2 * 2 - 1
        self.cells = [[True for x in range(self.width)] for y in range(self.height)]

    def display(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.cells[j][i], end=' ')
            print("\n")

    def set_path(self, x, y):
        self.cells[y][x] = False

    def set_walls(self, x, y):
        self.cells[y][x] = True

    def is_wall(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        else:
            return "."

    def create_maze(self, x, y):
        self.set_path(x, y)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        random.shuffle(directions)
        while len(directions) > 0:
            movemement = directions.pop()
            node_x = x + (movemement[0] * 2)
            node_y = y + (movemement[1] * 2)
            link_cells_x = x + movemement[0]
            link_cells_y = y + movemement[1]
            self.set_path(link_cells_x, link_cells_y)
            self.create_maze(node_x, node_y)
        return

    def __str__(self):
        string = ""
        conv = {
            True: "#",
            False: "."
        }
        for y in range(self.height):
            for x in range(self.width):
                string += conv[self.cells[y][x]]
            string += "\n"
        return string


X = Maze(10, 10)
Maze.display(X)
