from math import pi


def radians(angle):
    return angle * pi / 180


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
