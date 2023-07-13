class Movement:
    def __init__(self, x, y, angle):
        self.direction = (x, y)
        self.rotation = angle

    def __str__(self):
        return "({}), {}".format(self.direction, self.rotation)

    def copy(self):
        return Movement(self.direction[0], self.direction[1], self.rotation)

    def del_r(self):
        self.rotation = 0
        return self

    def change_speed(self, speed):
        if self.direction[0] > 0:
            self.direction = (speed, 0)
        elif self.direction[0] < 0:
            self.direction = (-speed, 0)
        elif self.direction[1] > 0:
            self.direction = (0, speed)
        else:
            self.direction = (0, -speed)
