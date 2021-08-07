# TODO: возможно убрать классы и сделать "голые" данные


from edge import Edge
from errors import SideNameError
from point import Point


class Config:
    def __init__(self):
        self.size = 150
        self.width = 1050
        self.height = 760
        self.dx = self.width / 2 + 30
        self.dy = self.height / 2 + 30
        self.dz = 0
        self.center = Point(self.dx, self.dy, self.dz)


class CubeConfig:
    def __init__(self, n=3):
        self.n = n
        self.size = Config().size / self.n

        self.exchanges_corners = {
            'R': ['RFU', 'RBU', 'RBD', 'RFD'],
            'L': ['LFU', 'LFD', 'LBD', 'LBU'],
            'U': ['ULF', 'ULB', 'URB', 'URF'],
            'D': ['DLF', 'DRF', 'DRB', 'DLB'],
            'F': ['FLU', 'FRU', 'FRD', 'FLD'],
            'B': ['BLU', 'BLD', 'BRD', 'BRU']
        }

        self.exchanges_ribs = {
            'R': ['RU', 'RB', 'RD', 'RF'],
            'L': ['LU', 'LF', 'LD', 'LB'],
            'U': ['UF', 'UL', 'UB', 'UR'],
            'D': ['DF', 'DR', 'DB', 'DL'],
            'F': ['FU', 'FR', 'FD', 'FL'],
            'B': ['BU', 'BL', 'BD', 'BR']
        }

    def get_center_data(self, name):
        if name == 'L':
            vertices = [
                (-self.size, self.size, self.size),
                (-self.size, -self.size, self.size),
                (-self.size, -self.size, -self.size),
                (-self.size, self.size, -self.size)
            ]
        elif name == 'R':
            vertices = [
                (self.size, self.size, self.size),
                (self.size, -self.size, self.size),
                (self.size, -self.size, -self.size),
                (self.size, self.size, -self.size)
            ]
        elif name == 'F':
            vertices = [
                (-self.size, self.size, self.size),
                (-self.size, -self.size, self.size),
                (self.size, -self.size, self.size),
                (self.size, self.size, self.size)
            ]
        elif name == 'B':
            vertices = [
                (-self.size, self.size, -self.size),
                (-self.size, -self.size, -self.size),
                (self.size, -self.size, -self.size),
                (self.size, self.size, -self.size)
            ]
        elif name == 'U':
            vertices = [
                (-self.size, -self.size, -self.size),
                (-self.size, -self.size, self.size),
                (self.size, -self.size, self.size),
                (self.size, -self.size, -self.size)
            ]
        elif name == 'D':
            vertices = [
                (-self.size, self.size, -self.size),
                (-self.size, self.size, self.size),
                (self.size, self.size, self.size),
                (self.size, self.size, -self.size)
            ]
        else:
            raise SideNameError

        vertices = [Point(*vertex) for vertex in vertices]

        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0)
        ]
        edges = [Edge(*edge) for edge in edges]

        return vertices, edges

    def get_eccentric_data(self):
        vertices = [
            (-self.size, self.size, self.size),
            (-self.size, -self.size, self.size),
            (self.size, -self.size, self.size),
            (self.size, self.size, self.size),

            (-self.size, self.size, -self.size),
            (-self.size, -self.size, -self.size),
            (self.size, -self.size, -self.size),
            (self.size, self.size, -self.size),
        ]
        vertices = [Point(*vertex) for vertex in vertices]

        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),

            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),

            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4)
        ]
        edges = [Edge(*edge) for edge in edges]

        return vertices, edges

    def get_offset_corners(self):
        offset = Config().size * (self.n - 1) / self.n
        positions = {
            'LFD': (-offset, offset, offset),
            'LFU': (-offset, -offset, offset),
            'RFU': (offset, -offset, offset),
            'RFD': (offset, offset, offset),

            'LBD': (-offset, offset, -offset),
            'LBU': (-offset, -offset, -offset),
            'RBU': (offset, -offset, -offset),
            'RBD': (offset, offset, -offset)
        }

        return positions

    def get_offset_ribs(self):
        if self.n < 3:
            return None

        def add(position, value, axis):
            position.append(value)
            if axis == 'x':
                position.append((-value[0], value[1], value[2]))
            elif axis == 'y':
                position.append((value[0], -value[1], value[2]))
            elif axis == 'z':
                position.append((value[0], value[1], -value[2]))

        edges = ['RF', 'UF', 'LF', 'DF', 'RU', 'RD', 'LD', 'LU', 'RB', 'UB', 'LB', 'DB']
        positions = {edge: [] for edge in edges}

        offset = Config().size * (self.n - 1) / self.n
        if self.n % 2:
            positions['RF'].append((offset, 0, offset))
            positions['UF'].append((0, -offset, offset))
            positions['LF'].append((-offset, 0, offset))
            positions['DF'].append((0, offset, offset))

            positions['RU'].append((offset, -offset, 0))
            positions['RD'].append((offset, offset, 0))
            positions['LD'].append((-offset, offset, 0))
            positions['LU'].append((-offset, -offset, 0))

            positions['RB'].append((offset, 0, -offset))
            positions['UB'].append((0, -offset, -offset))
            positions['LB'].append((-offset, 0, -offset))
            positions['DB'].append((0, offset, -offset))

        n = (self.n - 2) // 2
        step = self.size
        t = 1 if not self.n % 2 else 2

        for i in range(n):
            addition = (i * 2 + t) * step

            add(positions['RF'], (offset, addition, offset), 'y')
            add(positions['UF'], (addition, -offset, offset), 'x')
            add(positions['LF'], (-offset, addition, offset), 'y')
            add(positions['DF'], (addition, offset, offset), 'x')

            add(positions['RU'], (offset, -offset, addition), 'z')
            add(positions['RD'], (offset, offset, addition), 'z')
            add(positions['LD'], (-offset, offset, addition), 'z')
            add(positions['LU'], (-offset, -offset, addition), 'z')

            add(positions['RB'], (offset, addition, -offset), 'y')
            add(positions['UB'], (addition, -offset, -offset), 'x')
            add(positions['LB'], (-offset, addition, -offset), 'y')
            add(positions['DB'], (addition, offset, -offset), 'x')

        return positions

    def get_offset_centers(self):
        n = self.n - 2

        sides = ['R', 'L', 'U', 'D', 'F', 'B']
        positions = {side: [] for side in sides}

        offset = Config().size * (self.n - 1) / self.n
        step = self.size
        t = 1 if not self.n % 2 else 0

        for i in range(-(n // 2), (n + 1) // 2):
            dy = (i * 2 + t) * step
            for j in range(-(n // 2), (n + 1) // 2):
                dx = (j * 2 + t) * step

                positions['F'].append((dx, dy, offset))
                positions['B'].append((dx, dy, -offset))
                positions['R'].append((offset, dy, dx))
                positions['L'].append((-offset, dy, dx))
                positions['U'].append((dx, -offset, dy))
                positions['D'].append((dx, offset, dy))

        return positions

    def get_sides_centers(self):
        offset = Config().size
        sides_centers = {
            'R': (offset, 0, 0),
            'L': (-offset, 0, 0),
            'U': (0, -offset, 0),
            'D': (0, offset, 0),
            'F': (0, 0, offset),
            'B': (0, 0, -offset)
        }
        sides_centers = {side: Point(*center) for side, center in sides_centers.items()}

        return sides_centers

