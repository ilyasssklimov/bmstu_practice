from math import sin, cos


class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def move(self, point):
        self.x += point.x
        self.y += point.y
        self.z += point.z

    def scale(self, k, point):
        self.x = point.x + (self.x - point.x) * k
        self.y = point.y + (self.y - point.y) * k
        self.z = point.z + (self.z - point.z) * k

    def turn_ox(self, angle):
        y, z = self.y, self.z
        self.y = y * cos(angle) - z * sin(angle)
        self.z = y * sin(angle) + z * cos(angle)

    def turn_oy(self, angle):
        x, z = self.x, self.z
        self.x = x * cos(angle) + z * sin(angle)
        self.z = -x * sin(angle) + z * cos(angle)

    def turn_oz(self, angle):
        x, y = self.x, self.y
        self.x = x * cos(angle) - y * sin(angle)
        self.y = x * sin(angle) + y * cos(angle)

    def add_x(self, number):
        point = Point(self.x + number, self.y, self.z)
        return point

    def add_y(self, number):
        point = Point(self.x, self.y + number, self.z)
        return point

    def add_z(self, number):
        point = Point(self.x, self.y, self.z + number)
        return point
