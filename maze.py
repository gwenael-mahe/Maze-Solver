import random
import sys
import PIL
from PIL import Image
sys.setrecursionlimit(15000)


class Maze:

    def __init__(self, width):
        self.width = 2 * width + 1
        self.cells = [["0" for x in range(self.width)] for y in range(self.width)]
        self.visited = []
        self.final_path = []
        #self.recursive_backtrack(1, 1)
        self.kruskal()
        #self.set_walls()
        self.cells[0][0] = "."
        self.cells[self.width - 1][self.width - 1] = "."

        # Generation de l' entree et de la sortie
        rand = random.randint(1, 2)
        if rand == 1:
            self.cells[0][1] = "."
        else:
            self.cells[1][0] = "."
        rand = random.randint(1, 2)
        if rand == 1:
            self.cells[self.width - 1][self.width - 2] = "."
        else:
            self.cells[self.width - 2][self.width - 1] = "."
        self.visited.clear()

    def display(self):
        file = open("data.txt", "w")
        white = (255, 255, 255)
        blue = (0, 0, 255)
        green = (0, 255, 0)
        black = (0, 0, 0)
        img = PIL.Image.new('RGB', (self.width + 2, self.width + 2), white)
        for i in range(self.width):
            for j in range(self.width):
                file.write(self.cells[j][i])
                if self.cells[j][i] == "#":
                    img.putpixel((i + 1, j + 1), black)
                elif self.cells[j][i] == "*":
                    img.putpixel((i + 1, j + 1), blue)
                elif self.cells[j][i] == "o":
                    img.putpixel((i + 1, j + 1), green)
                print(self.cells[j][i], end=' ')
            print("\n")
            file.write("\n")
        img.show()
        file.close()

    def set_path(self, x, y):
        self.cells[y][x] = "."

    def is_wall(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.width:
            return self.cells[y][x]
        else:
            return "."

    def set_walls(self):
        for i in range(self.width):
            for j in range(self.width):
                if self.cells[j][i] == "0":
                    self.cells[j][i] = "#"

    def set_visited(self, x, y):
        self.visited.append((x, y))
        list(set(self.visited))

    def is_visited(self, x, y):
        if (x, y) in self.visited:
            return True
        else:
            return False

    def recursive_backtrack(self, x, y):
        self.set_path(x, y)
        self.set_visited(x, y)
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
        for i in range(self.width):
            for j in range(self.width):
                if self.is_visited(i, j) is False:
                    return False
        return True

    def kruskal(self):
        step = 1
        node = {}
        for i in range(self.width):
            for j in range(self.width):
                if i % 2 == 0 or j % 2 == 0:
                    self.cells[j][i] = "#"
                    self.set_visited(i, j)
                else:
                    self.cells[j][i] = step
                    node[step] = [(i, j)]
                    step += 1
        while self.all_visited() is False and len(node) != 1:
            x = 0
            y = 0
            while x % 2 == 0:
                x = random.randint(1, self.width - 2)
            while y % 2 == 0:
                y = random.randint(1, self.width - 2)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            random.shuffle(directions)
            while len(directions) > 0:
                movement = directions.pop()
                node_x = x + (movement[0] * 2)
                node_y = y + (movement[1] * 2)
                link_cells_x = x + movement[0]
                link_cells_y = y + movement[1]
                if 0 < node_x < self.width - 1 and 0 < node_y < self.width - 1:
                    if self.cells[y][x] != self.cells[node_y][node_x]:
                        self.set_path(link_cells_x, link_cells_y)
                        self.set_visited(x, y)
                        self.set_visited(node_x, node_y)
                    if self.cells[y][x] > self.cells[node_y][node_x]:
                        tmp = self.cells[y][x]
                        for i in node[self.cells[y][x]]:
                            node[self.cells[node_y][node_x]].append(i)
                        del node[self.cells[y][x]]
                        for i in range(self.width):
                            for j in range(self.width):
                                if self.cells[j][i] == tmp:
                                    self.cells[j][i] = self.cells[node_y][node_x]
                                    node[self.cells[node_y][node_x]].append((i, j))
                        break
                    elif self.cells[y][x] < self.cells[node_y][node_x]:
                        tmp = self.cells[node_y][node_x]
                        for i in node[self.cells[node_y][node_x]]:
                            node[self.cells[y][x]].append(i)
                        del node[self.cells[node_y][node_x]]
                        for i in range(self.width):
                            for j in range(self.width):
                                if self.cells[j][i] == tmp:
                                    self.cells[j][i] = self.cells[y][x]
                                    node[self.cells[y][x]].append((i, j))
                        break
        for i in range(self.width):
            for j in range(self.width):
                if self.cells[j][i] != "#":
                    self.cells[j][i] = "."

    def recursive_backtrack_resolution(self, position):
        x, y = position
        self.set_visited(x, y)
        if position == (self.width - 1, self.width - 1):
            self.final_path.append(position)
            return
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        random.shuffle(directions)
        while len(directions) > 0 and (self.width - 1, self.width - 1) not in self.final_path:
            movement = directions.pop()
            next_cells_x = x + movement[0]
            next_cells_y = y + movement[1]
            if next_cells_x < self.width \
                    and next_cells_y < self.width \
                    and self.cells[next_cells_y][next_cells_x] == '.'\
                    and self.is_visited(next_cells_x, next_cells_y) is False:
                self.recursive_backtrack_resolution((next_cells_x, next_cells_y))
                if (self.width - 1, self.width - 1) in self.final_path:
                    self.final_path.append(position)

    def set_final_path(self):
        for i in range(self.width):
            for j in range(self.width):
                if (i, j) in self.final_path:
                    self.cells[j][i] = "o"
                elif self.cells[j][i] != "#" and self.is_visited(i, j) is True:
                    self.cells[j][i] = "*"
        return True


X = Maze(45)
X.recursive_backtrack_resolution((0, 0))
X.set_final_path()
X.display()
