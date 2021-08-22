class Options:
    def __init__(self):
        self.city_size = 0
        self.map_array = None
        self.max_tip = 0
        self.robot_price = 0
        self.iter_count = 0
        self.orders_num = 0

    def __str__(self):
        res = (f'city_size = {self.city_size}\n'
               f'map = {self.map_array}\n'
               f'max_tip = {self.max_tip}\n'
               f'robot_price = {self.robot_price}\n'
               f'iter_num = {self.iter_count}\n'
               f'orders_num = {self.orders_num}\n')
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
        self.iter_count, self.orders_num = int(from_input[0]), int(from_input[1])

