# Press the green button in the gutter to run the script.
from options import Options
from work_cycle import WorkCycle
from work_map import WorkMap


# from pathfinding.core.diagonal_movement import DiagonalMovement
# from pathfinding.core.grid import Grid
# from pathfinding.finder.a_star import AStarFinder


def do_your_best():
    start_options = Options()
    start_options.get_input()
    work_map = WorkMap(start_options)
    cycle = WorkCycle(work_map)
    cycle.iterate()


if __name__ == '__main__':
    do_your_best()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
