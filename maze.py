import random


def initialize_maze(x):
    rows, columns = (2 * x + 1, 2 * x + 1)
    maze = [["." for i in range(rows)] for j in range(columns)]

    # for row in maze:
    #   print(row)

    return maze


def test(x, y, maze):
    directions = ["N", "S", "E", "W"]
    random.shuffle(directions)
    print(directions)


test(0, 0, initialize_maze(5))
