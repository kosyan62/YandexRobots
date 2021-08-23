# Press the green button in the gutter to run the script.
import time
from collections import deque
import heapq
from test import aStar


class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(maze, start, end, allow_diagonal_movement=False):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (len(maze[0]) * len(maze) // 2)

    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    # Loop until you find the end
    while len(open_list) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
            # if we hit this point return the path such as it is
            # it will not contain the destination
            return return_path(current_node)

            # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []

        for new_position in adjacent_squares:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if
                    child.position == open_node.position and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

    return None


def do_your_best():
    start_options = Options()
    start_options.get_input()
    work_map = WorkMap(start_options)
    cycle = WorkCycle(work_map)
    cycle.iterate()


class WorkCycle:
    def __init__(self, work_map):
        self.work_map = work_map

    def iterate(self):
        # for i in range(self.work_map.start_options.orders_count):
        for k in range(self.work_map.start_options.iter_count):
            new_orders = get_orders()
            self.work_map.add_orders(new_orders)
            for _ in range(60):
                self.work_map.step()
            self.work_map.print_actions()


class Options:
    def __init__(self):
        self.city_size = 0
        self.map_array = None
        self.max_tip = 0
        self.robot_price = 0
        self.iter_count = 0
        self.orders_count = 0

    def __str__(self):
        res = (f'city_size = {self.city_size}\n'
               f'map = {self.map_array}\n'
               f'max_tip = {self.max_tip}\n'
               f'robot_price = {self.robot_price}\n'
               f'iter_num = {self.iter_count}\n'
               f'orders_num = {self.orders_count}\n')
        return res

    def parse_first_line(self, line: str):
        args = line.split(' ')
        self.city_size, self.max_tip, self.robot_price = list(map(int, args))

    def parse_map(self, lines):
        lines_array = lines.split('\n')
        final_map = [[] for _ in range(self.city_size)]
        for k in range(self.city_size):
            for char in lines_array[k]:
                value = 1 if char == '#' else 0
                final_map[k].append(value)
        self.map_array = final_map

    def get_input(self):
        from_input = input()
        self.parse_first_line(from_input)

        from_input = input()
        if '.' not in from_input and '#' not in from_input:
            print(from_input)
            print('Parse error')
            raise ValueError
        char_map = ''
        while '.' in from_input or '#' in from_input:
            char_map += from_input + '\n'
            from_input = input()
        self.parse_map(char_map)
        from_input = from_input.split(' ')
        self.iter_count, self.orders_count = int(from_input[0]), int(from_input[1])


def format_path(start, end, map_arr):
    # path = astar(map_arr, start, end)
    path = aStar(start, end, map_arr)
    # print(pa)
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
            # print('path not empty')
            # print(self.path)
            i = len(self.path)
            if self.path[-1] == self.give_coords or self.path[-1] == self.pick_up_coords:
                i -= 1
                while self.path[i] == self.give_coords or self.path[i] == self.pick_up_coords:
                    i -= 1
            # print(self.path)
            path.extend(format_path(self.path[i], order[0], map_arr))
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
            cur_y, cur_x = self.position
            # print(cur_x, cur_y)
            next_y, next_x = new_coords
            # print(next_x, next_y)
            if cur_x != next_x and cur_y != next_y:
                # print(f'{cur_x} != {next_x} and {cur_y} != {next_y}')
                # print("Diagonal movement!")
                # raise IndexError
                pass
            # print(f'{cur_x}, {cur_y} --> {next_x}, {next_y}')
            if next_x - cur_x == 1:
                self.actions += self.letter_right
            elif cur_x - next_x == 1:
                self.actions += self.letter_left
            elif next_y - cur_y == 1:
                self.actions += self.letter_down
            elif cur_y - next_y == 1:
                self.actions += self.letter_up
            self.position = new_coords
            self.steps_remains -= 1


def count_robots_num():
    return 1
    # TODO Здесь будет функция рассчета оптимального количества роботов, но пока робот один.


def get_robots_on_start(options):
    count = count_robots_num()
    robots = [Robot(i) for i in range(count)]
    map_center = options.city_size // 2
    position = (map_center, map_center)
    print(count, flush=True)
    for i in range(map_center):
        if options.map_array[i][i - 1] == 0 and i >= 1:
            position = (i, i - 1)
            break
        elif options.map_array[i - 1][i] == 0 and i >= 1:
            position = (i - 1, i)
            break
        elif options.map_array[i + 1][i + 1] == 0:
            position = (i + 1, i + 1)
            break
        elif options.map_array[i - 1][i - 1] == 0 and i >= 1:
            position = (i - 1, i - 1)
            break
        if options.map_array[i][i + 1] == 0:
            position = (i, i + 1)
            break
        elif options.map_array[i + 1][i] == 0:
            position = (i + 1, i)
            break
        else:
            i -= 1
    position = (3,3)
    for i in range(count):
        print(position[0] + 1, position[1] + 1, flush=True)
        robots[i].position = position
    # TODO Здесь нужно придумать адекватное изначальное распределение роботов по карте
    return robots


class WorkMap:
    def __init__(self, options):
        self.robots = get_robots_on_start(options)
        self.orders = deque()
        self.start_options = options

    def add_orders(self, orders):
        for order in orders:
            min_steps_remains = self.robots[0].steps_remains
            min_id = self.robots[0].id
            for robot in self.robots:
                if robot.steps_remains < min_steps_remains:
                    min_steps_remains = robot.steps_remains
                    # TODO Добавить рассчет от конечной точки робота до забора заказа
                    min_id = robot.id
            self.robots[min_id].add_order(order, self.start_options.map_array)
            # print(self.robots[min_id].path)

    def step(self):
        for robot in self.robots:
            robot.move()

    def print_actions(self):
        for robot in self.robots:
            print(robot.actions + 'S' * (60 - len(robot.actions)), flush=True)
            robot.actions = ''


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def get_orders():
    order_count = int(input())
    orders = []
    for i in range(order_count):
        order_positions = list(map(int, input().split(' ')))
        orders.append(((order_positions[0] - 1, order_positions[1] - 1),
                       (order_positions[2] - 1, order_positions[3] - 1)))
    return orders


if __name__ == '__main__':
    do_your_best()
