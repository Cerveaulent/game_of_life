class Cell:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.state = 0
        self.next_state = 0

    def __repr__(self):
        return str(self.state)

    def kill(self):
        self.state = 0

    def activate(self):
        self.state = 1

    def is_dead(self):
        return self.state == 0

    def update(self):
        if self.state != self.next_state:
            self.state = self.next_state
