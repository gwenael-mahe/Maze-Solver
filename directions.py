class Directions:
    # 1, 0  sud
    #-1, 0  north
    # 0, 1  est
    # 0,-1  ouest
    array_direction=[[1,0],[-1,0],[0,1],[0,-1]]

    def converter_direction(int_random):

        #case 0:
        return -1