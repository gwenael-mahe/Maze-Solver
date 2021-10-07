import random


class Maze:
    def __init__(self, width):
        self.width = 2 * width + 1  # // 2 * 2 - 1
        self.height = 2 * width + 1     # // 2 * 2 - 1
        self.cells = [["0" for x in range(self.width)] for y in range(self.height)]
        #self.recursive_backtrack(1, 1)
        self.kruskal()
        #self.set_walls()
        self.cells[0][0] = "."
        self.cells[self.width - 1][self.height - 1] = "."

        # Génération de l'entrée et de la sortie
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

    def set_walls(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.cells[j][i] == "0":
                    self.cells[j][i] = "#"

    def is_visited(self, x, y):
        if self.cells[y][x] == ".":
            return True
        else:
            return False

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
        step = 1
        for i in range(self.width):
            for j in range(self.height):
                if i % 2 == 0 or j % 2 == 0:
                    self.cells[j][i] = "#"
                else:
                    self.cells[j][i] = step
                    step += 1
        while self.all_visited() is False:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            random.shuffle(directions)
            while len(directions) > 0:
                movement = directions.pop()
                node_x = x + (movement[0] * 2)
                node_y = y + (movement[1] * 2)
                link_cells_x = x + movement[0]
                link_cells_y = y + movement[1]
                if 0 < node_x < self.width and 0 < node_y < self.height and self.is_visited(node_x, node_y) is False:
                    self.set_path(link_cells_x, link_cells_y)
                    if self.cells[y][x] > self.cells[node_y][node_x]:
                        self.cells[y][x] = self.cells[node_y][node_x]
                    else:
                        self.cells[node_y][node_x] = self.cells[y][x]
                    break


X = Maze(4)
Maze.display(X)
