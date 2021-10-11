from unittest import case

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
        # range 1-n
        print(self.i, self.j)
        k: int = 3
        sum: int = 0
        print(B_ARRAY.shape[0])
        while (k < B_ARRAY.shape[0]):
            if (B_ARRAY[k][self.i][self.j]==1):
                sum = sum + 1
            k = k + 1
        return sum
    """
    def num_random_arrets(self, int_random, B_ARRAY):
        # olny four directionws
        int_random=3
        #only one dummy argument in switcher??
        switch ={
            0:
                self.choix_direction(B_ARRAY,0),

            1:
                self.choix_direction(B_ARRAY,1),

            2:
                self.choix_direction(B_ARRAY,2),

            3:
                self.choix_direction(B_ARRAY,3),
        }
        return switch.get(int_random, "not found selectio")  
    """

    def choix_direction(self, B_ARRAY: int, random: int):
        k: int = 3
        r: int = -1
        print(random)
        print(B_ARRAY.shape[0])
        # to improuve todo
        random=3
        while(True):
            # detecter of arretes and limites of labyritnhe
            if(B_ARRAY[k][self.i][self.j]==1):
                r = r + 1
            # in the case the lim sup of random choix is attempt
            if(r>=random and k<B_ARRAY.shape[0]-1):
                break
            k = k + 1
        #end_if

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