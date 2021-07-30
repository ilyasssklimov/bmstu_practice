from mymath import sin_deg, cos_deg


class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Point({self.x}, {self.y}, {self.z})'

    def __repr__(self):
        return str(self)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)

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
        self.y = y * cos_deg(angle) - z * sin_deg(angle)
        self.z = y * sin_deg(angle) + z * cos_deg(angle)

    def turn_oy(self, angle):
        x, z = self.x, self.z
        self.x = x * cos_deg(angle) + z * sin_deg(angle)
        self.z = -x * sin_deg(angle) + z * cos_deg(angle)

    def turn_oz(self, angle):
        x, y = self.x, self.y
        self.x = x * cos_deg(angle) - y * sin_deg(angle)
        self.y = x * sin_deg(angle) + y * cos_deg(angle)
