import numpy as np

class Directions:
    # 1, 0  sud
    #-1, 0  north
    # 0, 1  est
    # 0,-1  ouest
    array_direction=[[1,0],[-1,0],[0,1],[0,-1]]


    def array_coordonnes(n):
        B_ARRAY=np.empty((n*n,3),dtype=int,order='F')
        k=0
        i: int=0
        while(i<n):
                # i-eme column
                B_ARRAY[i][1]=i
            j=0
            while(j<n):
                # id
                B_ARRAY[i][0] = k
                # j-eme line
                B_ARRAY[i][2] = j
                j=j+1
                k=k+1
            #end_while_2
            i =i + 1
        #end_while_1
        return B_ARRAY

    def converter_direction(int_random):


        #case 0:

        return -1