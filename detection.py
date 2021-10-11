import numpy as np
import motor_fleches

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

    def arrets_num_random(self, B_ARRAY):
        # found the number of arrets
        print(self.i, self.j)
        k: int = 3
        sum: int = 0
        print(B_ARRAY.shape[0])
        while (k < B_ARRAY.shape[0]):
            if (B_ARRAY[k][self.i][self.j]==1):
                sum = sum + 1
            k = k + 1
        return sum

    def num_random_arrets(self, int_random, B_ARRAY):
        # olny four directionws
        int_random=3
        #only one dummy argument in switcher??
        switcher = {
                0: lambda: self.choix_direction(B_ARRAY,0),

                1: lambda: self.choix_direction(B_ARRAY,1),

                2: lambda: self.choix_direction(B_ARRAY,2),

                3: lambda: self.choix_direction(B_ARRAY,3),
            }
        return switcher.get(int_random, "not found selectio")

    def choix_direction(self, B_ARRAY: int, random: int):
        k: int = 3
        r: int = 0
        print(B_ARRAY.shape[0])
        while(k<B_ARRAY.shape[0] and r < random):
            if(B_ARRAY[k][self.i][self.j]==1):
                r = r + 1
            k = k + 1
        if (k==3):
            # ouest
            return (0,-1)
        elif (k==4):
            # north
            return (-1,0)
        elif (k==5):
            # est
            return (0,1)
        else:
            # south
            return (1,0)

        # return dir