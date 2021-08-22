from robot import Robot


def count_robots_num():
    return 1


def get_robots_on_start(map_size):
    count = count_robots_num()
    robots = [Robot() for _ in range(count)]
    map_center = map_size//2
    robots[0].position = (map_center, map_center)
    for i in range(1, count):
        robots[i].position = (map_center + i, map_center + i)
    return robots


class WorkMap:
    def __init__(self, options):
        self.robots = get_robots_on_start(options.city_size)
        self.orders = []
        self.start_options = options

    def add_orders(self, orders):
        self.orders.append(orders)

    def step(self):
        # self.give_orders_to_robots()
        pass


