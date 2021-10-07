import numpy as np
import mazes

#import class in python
from directions import Directions


def demands_the_name():
    name_file = input("put a name of file\n")
    return name_file


def main():
    # Use a breakpoint in the code line below to debug your script.
    try:
        print(demands_the_name())
        dir=Directions()
        print(dir.array_direction[1][1])

        mazes.output_file(mazes.initial_solver_array())



    except ImportError:
        print("founded error in main")
    # EndTry


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/