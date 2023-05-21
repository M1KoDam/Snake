class Movement:
    def __init__(self, x, y, angle):
        self.direction = (x, y)
        self.rotation = angle

    def copy(self):
        return Movement(self.direction[0], self.direction[1], self.rotation)
