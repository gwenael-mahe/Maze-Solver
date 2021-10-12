import mazes
import motor_fleches

#import classes different to simples files in outside
from detection import Detection
from directions import Directions


def demands_the_name():
    name_file = input("put a name of file\n")
    return name_file


def main():
    # Use a breakpoint in the code line below to debug your script.
    try:
        print(demands_the_name())
        n = mazes.definition_of_dimention()
        dir = Directions()
        print(dir.array_direction[1][1])

        mazes.output_file(mazes.initial_solver_array(n)[0])

       # print(motor_fleches.int_random(mazes.initial_solver_array(n)[1]))

        print(n)
        # print(dir.array_coordonnes(n))
        det = Detection(0, 0)

        det.pointeuse_arrets_direction(dir.array_coordonnes(n))

        print("first increasing ouest_est:_"+str(det.choix_direction(dir.array_coordonnes(n),motor_fleches.int_random(det.arrets_num_random(dir.array_coordonnes(n))))[0]))

        print("second increasing noth_sud:_"+str(det.choix_direction(dir.array_coordonnes(n),motor_fleches.int_random(det.arrets_num_random(dir.array_coordonnes(n))))[1]))


        # dir.move_direction(dir.array_coordonnes(n),
        # det.choix_direction(dir.array_coordonnes(n),motor_fleches.int_random(det.arrets_num_random(dir.array_coordonnes(n))))[0],
        # det.choix_direction(dir.array_coordonnes(n),motor_fleches.int_random(det.arrets_num_random(dir.array_coordonnes(n))))[1])

    except ImportError:
        print("founded error in main")
    #EndTry


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/