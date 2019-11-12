class Cell:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.state = 0

    def kill(self):
        self.state = 0

    def activate(self):
        self.state = 1

    def is_dead(self):
        if self.state == 0:
            return True
        else:
            return False
