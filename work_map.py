from robot import Robot
from collections import deque


def count_robots_num():
    return 1
    # TODO Здесь будет функция рассчета оптимального количества роботов, но пока робот один.


def get_robots_on_start(map_size):
    count = count_robots_num()
    robots = [Robot(i) for i in range(count)]
    map_center = map_size//2
    robots[0].position = (map_center, map_center)
    for i in range(1, count):
        robots[i].position = (map_center + i, map_center + i)
    # TODO Здесь нужно придумать адекватное изначальное распределение роботов по карте
    return robots


class WorkMap:
    def __init__(self, options):
        self.robots = get_robots_on_start(options.city_size)
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
            print(robot.actions + 'S' * (60 - len(robot.actions)))
            robot.actions = ''

