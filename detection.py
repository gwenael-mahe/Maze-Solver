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
            if (B_ARRAY[k][self.i][self.j] == 1):
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

    def choix_direction(self, B_ARRAY: int):

        k: int = 0
        """r: int = -1"""
        """print(random)
        print(B_ARRAY.shape[0])
        # to improuve todo
        random=1
        while(True):
            # detecter of arretes and limites of labyritnhe
            if(B_ARRAY[k][self.i][self.j]==1):
                r = r + 1
            # in the case the lim sup of random choix is attempt
            if(r>=random and k>=(B_ARRAY.shape[0]-1)):
                break
            k = k + 1
        #end_if
        """

        k = self.pointeuse_arrets_direction(B_ARRAY)

        if (k == 3):
            # ouest
            return (0, -1)
        elif (k == 4):
            # north
            return (-1, 0)
        elif (k == 5):
            # est
            return (0, 1)
        else:
            # south
            return (1, 0)

        # return dir

    def pointeuse_arrets_direction(self, B_ARRAY: int):

        # simplified array direction
        C_ARRAY = np.zeros((2, 4), dtype=int, order='F')
        sum: int = 0
        k: int = 3
        i: int = 0
        while (k < B_ARRAY.shape[0]):
            # arrets or limites 1,2
            C_ARRAY[1][i] = B_ARRAY[k][self.i][self.j]
            # directions 3,4,5,6
            C_ARRAY[0][i] = k

            if (C_ARRAY[1][i] == 1):
                sum = sum + 1
            # end_if
            k = k + 1
            i = i + 1
        # end_loop

        # calling random function for  indicate direction
        # one calling of int_random subroutine
        random = motor_fleches.int_random(sum)

        i: int = -1
        k: int = 0
        while (i < random):
            # only direction with arrets 1,1
            if (C_ARRAY[1][k] == 1):
                i = i + 1
            # end_if
            return C_ARRAY[0][k - 1]
            k = k + 1
        # end_while

    # end_function_point_direction

    def indicate_arrets(self, COMPARE_ARRAY):

        print(COMPARE_ARRAY)

        #record of noued already visited
        self.indicate_noeud()

        return 0

    # End_function_erase_arrets

    def arrets_pile(self):
        # le arrets dejà visité
        # todo
        return 0

    # End_function_arrests_pile

    def indicate_noeud(self):
        # todo
        return 0
    # End_function_indicate_noeud
