import numpy as np

# import classes different to simples files in outside
# from numpy.dual import det

# from detection import Detection

import detection


class Directions:
    # 1, 0  sud
    # -1, 0  north
    # 0, 1  est
    # 0,-1  ouest
    array_direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def array_coordonnes(self, n: int):

        B_ARRAY = np.zeros((7, n, n), dtype=int, order='F')
        k: int = 0
        i: int = 0
        j: int = 0

        i = 0
        while (i < n):
            B_ARRAY[1][i][j] = i
            while (True):
                # j-eme line
                B_ARRAY[2][i][j] = j

                if (j == 0):
                    # arret ouest
                    B_ARRAY[3][i][j] = 2
                else:
                    B_ARRAY[3][i][j] = 1

                if (i == 0):
                    # arret north
                    B_ARRAY[4][i][j] = 2
                else:
                    B_ARRAY[4][i][j] = 1

                if (j == n - 1):
                    # arret est
                    B_ARRAY[5][i][j] = 2
                else:
                    # arret est
                    B_ARRAY[5][i][j] = 1

                if (i == n - 1):
                    # south
                    B_ARRAY[6][i][j] = 2
                else:
                    # south
                    B_ARRAY[6][i][j] = 1

                # id of node
                B_ARRAY[0][i][j] = k

                j = j + 1
                k = k + 1
                if (j >= n):
                    break
            # end_while_2
            i = i + 1
            j = 0
        # end_while_1
        return B_ARRAY

    # end array direction

    def move_direction(self, B_ARRAY: int, DIR_ARRAY: int):

        print("increasing_move_coordonnes_:_" + str(DIR_ARRAY))

        COO_ARRAY = np.zeros((2, 3), dtype=int, order='F')

        det = detection.Detection(0, 0)

        # initial_position
        # 0 dim for initial position
        # 1 dim for increasing position
        # 2 dim for finally/actually position coordoonne
        # COO_ARRAY[2][3] from
        # det.get_position()[0]
        COO_ARRAY[0][0] = det.get_position()[0]
        COO_ARRAY[1][0] = det.get_position()[1]

        # incrementeur of position
        COO_ARRAY[0][1] = DIR_ARRAY[0]
        COO_ARRAY[1][1] = DIR_ARRAY[1]

        # increasing position
        # 2 dim for finally/actually position coordoonne
        COO_ARRAY[0][2] = COO_ARRAY[0][0] + COO_ARRAY[0][1]
        COO_ARRAY[1][2] = COO_ARRAY[1][0] + COO_ARRAY[1][1]
        # position_update
        det.set_position(COO_ARRAY[0][2], COO_ARRAY[1][2])
        #
        print("actually_pos_:_" + str(COO_ARRAY[0][2]) + "_" + str(COO_ARRAY[1][2]))

        print(COO_ARRAY)

        # return an array with elements : B_ARRAY, initial position, direction in coord, actual position
        return (B_ARRAY, COO_ARRAY)

        # End_function_move_direction&

    def eraser_noued_by_noued(self, COMPARE_ARRAY: int, noeud: int):

        # B_ARRAY
        # print(COMPARE_ARRAY[0])
        # COO_ARRAY
        # print(COMPARE_ARRAY[1])
        print(COMPARE_ARRAY)

        det = detection.Detection(COMPARE_ARRAY[1][0][0], COMPARE_ARRAY[1][1][0])
        # det = detection.Detection()
        # COMPARE_ARRAY[1][])

        print(det.get_position()[0], det.get_position()[1])

        # detected_direction_index__by_direction_coord
        #        3,4,5,6
        det.detected_direction_by_coord(COMPARE_ARRAY, COMPARE_ARRAY[1][0][1],COMPARE_ARRAY[1][0][1])

        # opposite_dir()
        #       5 , 6 , 3 , 4



    # End_function_erase_nodeby_node