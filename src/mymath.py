from math import pi
from point import Point


class Vector:
    def __init__(self, start, finish):
        self.x = finish.x - start.x
        self.y = finish.y - start.y
        self.z = finish.z - start.z

    def __str__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'

    def __neg__(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        return self

    def negative(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    def get_vector(self):
        return [self.x, self.y, self.z]

    def get_normal(self):  # , start_2, finish_2):
        if self.x:
            normal = Vector(Point(1, 0, 0), Point(-self.y / self.x, 1, 0))
        else:
            normal = Vector(Point(0, 0, 0), Point(1, 0, 0))

        # if scalar_multiplication(normal, -Vector(start_2, finish_2)) < 0:
        #     normal.negative()

        return normal


def radians(angle):
    return angle * pi / 180


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


def remove_repeats(points_1, points_2):
    general = list(set(points_1) & set(points_2))
    return points_1 + points_2 + general


def scalar_multiplication(vector_1, vector_2):
    return vector_1.x * vector_2.x + vector_1.y * vector_2.y + vector_1.z * vector_2.z
