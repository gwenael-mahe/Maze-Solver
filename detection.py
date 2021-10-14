import numpy as np
import motor_fleches
import io_file


class Detection:
    j: int
    i: int
    det_noeuds = []

    # constructor

    def __init__(self):
        self.det_noeuds = []

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def get_position(self):
        # is an array return
        return (self.i, self.j)

    def set_position(self, i, j):
        self.i = i
        self.j = j

    def get_list(self):
        return self.det_noeuds

    def set_list(self, noeud):
        self.det_noeuds.append(noeud)

    """
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
                # la plus important fonction du programme :
                # records pointeuse to direction noeuds
                # sert pour records of noeuds pointes avec arrets
                # et ne pas les choisir comme direction dans les actuelles positions suivantes
                self.input_detection_noeuds(self.detected_noeud_by_direction(B_ARRAY, k, self.i, self.j))

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
            k = k + 1
        # end_while

        return C_ARRAY[0][k - 1]

    # end_function_point_direction

    def indicate_arrets(self, COMPARE_ARRAY):

        # B_ARRAY
        print(COMPARE_ARRAY[0])
        # COO_ARRAY
        print(COMPARE_ARRAY[1])

        # output of record of noued already visited
        self.output_detected_noeuds()

        return 0

    # End_function_erase_arrets

    def arrets_pile(self):
        # le arrets dejà visité
        # peut etre pas necessaire
        # todo
        return 0

    # End_function_arrests_pile

    def detected_noeud_by_direction(self, B_ARRAY, dir: int, i: int, j: int):

        print(B_ARRAY)
        if (dir == 3):
            # ouest
            noeud = B_ARRAY[0][self.i + 0][self.j - 1]
        elif (dir == 4):
            # north
            noeud = B_ARRAY[0][self.i - 1][self.j + 0]
        elif (dir == 5):
            # est
            noeud = B_ARRAY[0][self.i + 0][self.j + 1]
        else:
            # sud
            noeud = B_ARRAY[0][self.i + 1][self.j + 0]
        # end_if

        return noeud

    # End_function_indicate_noeud

    def input_detection_noeuds(self, noeud):
        # todo

        print("the value in input detectrion noueud_:_"+ str(noeud))

        # append to list array one dimentional

        self.set_list(noeud)

        print(self.output_detected_noeuds())

        return 0

    def output_detected_noeuds(self):
        list_actually=self.get_list()
        return list_actually

    def coord_by_noeud(self):
        # todo
        return 0
    # end_function
