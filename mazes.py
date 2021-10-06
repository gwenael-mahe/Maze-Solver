import numpy as np

from numpy import chararray

print('the vesion numpy is:', np.__version__)


def definition_of_dimention():
    s_string=input("enter a dimention of labyrinth\n")
    return int(s_string,10)

def initial_solver_array():
    try:
        n=definition_of_dimention()
        print(type(n))
        A=np.empty((n,n,4),dtype=chararray,order='F')
        #note the column priority as Fortran 90

        A[0][0][0]='3'
        return A
    except ImportError:
        print("founded error in main_solver")
    #EndTry

def output_file(A):
    i=0
    print (len(A))
    while(i<=len(A)):
        j=0
        while(j<=len(A)):
            A[i][j][0]='#'
        #End if

    #End if
    print(A)




#End def

