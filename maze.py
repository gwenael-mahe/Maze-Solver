def initialize_maze(x):
    rows, columns = (2 * x + 1, 2 * x + 1)
    maze = [["." for i in range(rows)] for j in range(columns)]

    for row in maze:
        print(row)



initialize_maze(5)