import random


class Maze:
    def __init__(self, width):
        self.width = 2 * width + 1  # // 2 * 2 - 1
        self.height = 2 * width + 1  # // 2 * 2 - 1
        self.cells = [["0" for x in range(self.width)] for y in range(self.height)]
        self.cells[0][0] = "."
        self.cells[self.width - 1][self.height - 1] = "."
        rand = random.randint(1, 2)
        if rand == 1:
            self.cells[0][1] = "."
        else:
            self.cells[1][0] = "."
        rand = random.randint(1, 2)
        if rand == 1:
            self.cells[self.width - 1][self.height - 2] = "."
        else:
            self.cells[self.width - 2][self.height - 1] = "."
        self.recursive_backtrack(1, 1)
        self.set_walls()

    def display(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.cells[j][i], end=' ')
            print("\n")

    def get_cells(self):
        return self.cells

    def set_path(self, x, y):
        self.cells[y][x] = "."

    def is_wall(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        else:
            return "."

    def set_walls(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.cells[j][i] == "0":
                    self.cells[j][i] = "#"

    def is_visited(self, x, y):
        if self.cells[y][x] == "0":
            return False
        else:
            return True

    def recursive_backtrack(self, x, y):
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
                self.recursive_backtrack(node_x, node_y)
        return

    def all_visited(self):
        for i in range(self.width - 1):
            for j in range(self.height - 1):
                if self.is_visited(i, j) is False:
                    return False
        return True

    def kruskal(self):
        while self.all_visited() is False:
            x = random.randint(0, self.width - 1)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            random.shuffle(directions)
            deplacement = directions.pop()
            y = x + (deplacement[0] * 2)
            while len(directions) > 0:
                y = False


def solve_maze(maze, position, N):
    if position == (N - 1, N - 1):
        return [(N - 1, N - 1)]
    x, y = position
    print(maze[x + 1][y])
    if x + 1 < N and maze[x + 1][y] == '.':
        a = solve_maze(maze, (x + 1, y), N)
        if a != None:
            return [(x, y)] + a

    if y + 1 < N and Maze[x][y + 1] == '.':
        b = solve_maze(maze, (x, y + 1), N)
        if b != None:
            return [(x, y)] + b


X = Maze(4)
print(X.get_cells())
# Maze.display(X)
print(solve_maze(X.get_cells(), [0, 0], 9))
