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
        A=np.empty((4,n,n),dtype=chararray,order='F')
        #note the column priority as Fortran 90

        return A
    except ImportError:
        print("founded error in main_solver")
    #EndTry


def output_file(A):
    i=0
    print ('shape individual by dimention []_'+str(A.shape[1]))
    while(i<A.shape[1]):
        j=0
        while(j<A.shape[1]):
            A[0][j][i]='#'
            j = j + 1
        #End if
        i = i + 1
    #End if
    print(A)
#End def

def temporary_chemin():
    #todo
    #output in array []   
    return 0
