class Robot:
    def __init__(self):
        self.position = (0, 0)
        self.have_order = False
        self.path = None
        self.free_point = None

    def __repr__(self):
        return f'<pos = {self.position} ' \
               f'path = {self.path}>'
