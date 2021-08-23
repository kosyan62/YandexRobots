from pathfinding.finder.a_star import AStarFinder
from collections import deque
from test_main import timeit

@timeit
def format_path(start, end, map_arr):
    print(start, end)
    grid = Grid(matrix=map_arr)
    start = grid.node(*start)
    end = grid.node(*end)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    # print(grid.grid_str(path=path, start=start, end=end))
    return path


class Robot:
    pick_up_coords = (-1, -1)
    give_coords = (-2, -2)
    letter_up = 'U'
    letter_down = 'D'
    letter_left = 'L'
    letter_right = 'R'
    letter_pick_up = 'T'
    letter_give = 'P'
    letter_stay = 'S'

    def __init__(self, id):
        self.id = id
        self.position = None
        self.path = deque()
        self.steps_remains = 0
        self.actions = ''

    def __repr__(self):
        return f'<pos = {self.position} ' \
               f'path = {self.path}>'

    def add_order(self, order, map_arr):
        path = deque()
        if self.path:
            path.extend(format_path(self.path[-1], order[0], map_arr))
        else:
            path.extend(format_path(self.position, order[0], map_arr))
        path.append(self.pick_up_coords)
        path.extend(format_path(order[0], order[1], map_arr))
        path.append(self.give_coords)

        self.path.extend(path)
        self.steps_remains += len(path)
        # print(self.path)

    def move(self):
        if not self.path:
            self.actions += self.letter_stay
            return
        new_coords = self.path.popleft()

        if new_coords == self.give_coords:
            self.actions += self.letter_give
        elif new_coords == self.pick_up_coords:
            self.actions += self.letter_pick_up
        else:
            cur_x, cur_y = self.position
            # print(cur_x, cur_y)
            next_x, next_y = new_coords
            # print(next_x, next_y)
            if cur_x != next_x and cur_y != next_y:
                # print(f'{cur_x} != {next_x} and {cur_y} != {next_y}')
                # print("Diagonal movement!")
                # raise IndexError
                pass
            if next_x - 1 == cur_x:
                self.actions += self.letter_right
            elif next_x + 1 == cur_x:
                self.actions += self.letter_left
            elif next_y + 1 == cur_y:
                self.actions += self.letter_up
            elif next_y - 1 == cur_y:
                self.actions += self.letter_down
            # elif next_y == cur_y and cur_x == next_y:
            #     print(self.letter_stay)
            # else:
            #     "Wrong value as coords"
                # print(f'{cur_x} != {next_x} and {cur_y} != {next_y}')
                # raise IndexError
            # print(self.path)
            self.position = new_coords
            self.steps_remains -= 1
