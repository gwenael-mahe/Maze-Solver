import numpy as np


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
            B_ARRAY[2][i][j] = i
            while (True):
                # j-eme line
                B_ARRAY[1][i][j] = j

                if (j == 0) :
                    # arret ouest
                    B_ARRAY[3][i][j] = 2
                else:
                    B_ARRAY[3][i][j] = 1

                if (i == 0):
                    # arret north
                    B_ARRAY[4][i][j] = 2
                else:
                    B_ARRAY[4][i][j] = 1

                if(j == n-1):
                    # arret est
                    B_ARRAY[5][i][j] = 2
                else:
                    # arret est
                    B_ARRAY[5][i][j] = 1

                if(i == n-1):
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

            j=0
        # end_while_1
        return B_ARRAY
    # end array direction


def move_direction(num_random_arrets):
    # case 0:


    return -1
