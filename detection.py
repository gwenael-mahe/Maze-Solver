import numpy as np


class Detection:


    j: int
    i: int

    # constructor

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def get_position(self):
        # is an array return
        return (self.i, self.j)

    def set_position(self, i, j):
        self.i = i
        self.j = j

    def arrets_num_random(self, B_ARRAY: int):
        # found the number of arrets
        print(self.i, self.j)
        k: int = 0
        sum: int = 0
        while (k < B_ARRAY.shape[1]):
            sum = sum + 1


    def num_random_arrets(self, B_ARRAY: int, int_random: int):
        # olny four directionws
        switcher = {
            0:
                choix_direction(0),

            1:
                choix_direction(1),

            2:
                choix_direction(2),

            3:
                choix_direction(3),
        }
        return switcher.get(int_random, "not found selection")

def choix_direction(self, B_ARRAY: int, random: int):
    k: int = 3
    r: int = 0
    while(k<B_ARRAY.shape[1] and r == random):

        if(B_ARRAY[k][self.i][self.j]==1):
            r = r + 1

        k = k + 1

    if (k==3):
        dir='o'
    elif (k==4):
        dir = 'n'
    elif (k==5):
        dir = 'e'
    else:
        dir = 's'

    return dir