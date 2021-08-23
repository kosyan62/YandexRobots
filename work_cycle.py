def get_orders():
    order_count = int(input())
    orders = []
    for i in range(order_count):
        order_positions = list(map(int, input().split(' ')))
        orders.append(((order_positions[0] - 1, order_positions[1] - 1),
                       (order_positions[2] - 1, order_positions[3] - 1)))
    return orders


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



