def get_orders():
    order_count = int(input())
    orders = []
    for i in range(order_count):
        order_positions = input().split(' ')
        orders.append(((order_positions[0], order_positions[1]), (order_positions[2], order_positions[3])))
    return orders


class WorkCycle:
    def __init__(self, work_map):
        self.work_map = work_map

    def iterate(self):
        for i in range(self.work_map.start_options.iter_count):
            new_orders = get_orders()
            self.work_map.add_orders(new_orders)
            self.work_map.step()


