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


class _CubeConfig:
    def __init__(self):
        size = Config().size

        '''
        R - right side
        L - left side
        U - up side
        D - down side
        F - front side
        B - back side
        '''
        self.vertices = {
            'LBU': (-size, -size, -size),
            'RBU': (size, -size, -size),
            'RBD': (size, size, -size),
            'LBD': (-size, size, -size),

            'LFU': (-size, -size, size),
            'RFU': (size, -size, size),
            'RFD': (size, size, size),
            'LFD': (-size, size, size)
        }

        self.carcass_edges = [
            ('LBU', 'RBU'),
            ('RBU', 'RBD'),
            ('RBD', 'LBD'),
            ('LBD', 'LBU'),

            ('LBU', 'LFU'),
            ('RBU', 'RFU'),
            ('RBD', 'RFD'),
            ('LBD', 'LFD'),

            ('LFU', 'RFU'),
            ('RFU', 'RFD'),
            ('RFD', 'LFD'),
            ('LFD', 'LFU')
        ]

        '''
              7   8
            *---*---*
         12 | 5 | 6 | 14
            *   *   *
         11 | 3 | 4 | 13
            *---*---*
              1   2 
          
        * - layers
        digit - number of node 
        '''
        # TODO: автоматизировать для n !!!
        self.inner_vertices = {
            'F01': ('LFD', 1 / 3, 0, 0),
            'F02': ('LFD', 2 / 3, 0, 0),
            'F03': ('LFD', 1 / 3, - 1 / 3, 0),
            'F04': ('LFD', 2 / 3, - 1 / 3, 0),
            'F05': ('LFU', 1 / 3, 1 / 3, 0),
            'F06': ('LFU', 2 / 3, 1 / 3, 0),
            'F07': ('LFU', 1 / 3, 0, 0),
            'F08': ('LFU', 2 / 3, 0, 0),
            'F11': ('LFD', 0, - 1 / 3, 0),
            'F12': ('LFU', 0, 1 / 3, 0),
            'F13': ('RFD', 0, - 1 / 3, 0),
            'F14': ('RFU', 0, 1 / 3, 0),

            'B01': ('RBD', - 1 / 3, 0, 0),
            'B02': ('RBD', - 2 / 3, 0, 0),
            'B03': ('RBD', - 1 / 3, - 1 / 3, 0),
            'B04': ('RBD', - 2 / 3, - 1 / 3, 0),
            'B05': ('RBU', - 1 / 3, 1 / 3, 0),
            'B06': ('RBU', - 2 / 3, 1 / 3, 0),
            'B07': ('RBU', - 1 / 3, 0, 0),
            'B08': ('RBU', - 2 / 3, 0, 0),
            'B11': ('RBD', 0, - 1 / 3, 0),
            'B12': ('RBU', 0, 1 / 3, 0),
            'B13': ('LBD', 0, - 1 / 3, 0),
            'B14': ('LBU', 0, 1 / 3, 0),

            'R01': ('RFD', 0, 0, - 1 / 3),
            'R02': ('RFD', 0, 0, - 2 / 3),
            'R03': ('RFD', 0, - 1 / 3, - 1 / 3),
            'R04': ('RFD', 0, - 1 / 3, - 2 / 3),
            'R05': ('RFU', 0, 1 / 3, - 1 / 3),
            'R06': ('RFU', 0, 1 / 3, - 2 / 3),
            'R07': ('RFU', 0, 0, - 1 / 3),
            'R08': ('RFU', 0, 0, - 2 / 3),
            'R11': ('RFD', 0, - 1 / 3, 0),
            'R12': ('RFU', 0, 1 / 3, 0),
            'R13': ('RBD', 0, - 1 / 3, 0),
            'R14': ('RBU', 0, 1 / 3, 0),

            'L01': ('LBD', 0, 0, 1 / 3),
            'L02': ('LBD', 0, 0, 2 / 3),
            'L03': ('LBD', 0, - 1 / 3, 1 / 3),
            'L04': ('LBD', 0, - 1 / 3, 2 / 3),
            'L05': ('LBU', 0, 1 / 3, 1 / 3),
            'L06': ('LBU', 0, 1 / 3, 2 / 3),
            'L07': ('LBU', 0, 0, 1 / 3),
            'L08': ('LBU', 0, 0, 2 / 3),
            'L11': ('LBD', 0, - 1 / 3, 0),
            'L12': ('LBU', 0, 1 / 3, 0),
            'L13': ('LFD', 0, - 1 / 3, 0),
            'L14': ('LFU', 0, 1 / 3, 0),

            'U01': ('LFU', 1 / 3, 0, 0),
            'U02': ('LFU', 2 / 3, 0, 0),
            'U03': ('LFU', 1 / 3, 0, - 1 / 3),
            'U04': ('LFU', 2 / 3, 0, - 1 / 3),
            'U05': ('LBU', 1 / 3, 0, 1 / 3),
            'U06': ('LBU', 2 / 3, 0, 1 / 3),
            'U07': ('LBU', 1 / 3, 0, 0),
            'U08': ('LBU', 2 / 3, 0, 0),
            'U11': ('LFU', 0, 0, - 1 / 3),
            'U12': ('LBU', 0, 0, 1 / 3),
            'U13': ('RFU', 0, 0, - 1 / 3),
            'U14': ('RBU', 0, 0, 1 / 3),

            'D01': ('LBD', 1 / 3, 0, 0),
            'D02': ('LBD', 2 / 3, 0, 0),
            'D03': ('LBD', 1 / 3, 0, 1 / 3),
            'D04': ('LBD', 2 / 3, 0, 1 / 3),
            'D05': ('LFD', 1 / 3, 0, - 1 / 3),
            'D06': ('LFD', 2 / 3, 0, - 1 / 3),
            'D07': ('LFD', 1 / 3, 0, 0),
            'D08': ('LFD', 2 / 3, 0, 0),
            'D11': ('LBD', 0, 0, 1 / 3),
            'D12': ('LFD', 0, 0, - 1 / 3),
            'D13': ('RBD', 0, 0, 1 / 3),
            'D14': ('RFD', 0, 0, - 1 / 3),
        }

        letters = ['F', 'R', 'B', 'L', 'U', 'D']
        self.sides = []
        for letter in letters:
            self.sides.extend([
                (f'{letter}01', f'{letter}03'),
                (f'{letter}02', f'{letter}04'),
                (f'{letter}03', f'{letter}05'),
                (f'{letter}04', f'{letter}06'),
                (f'{letter}05', f'{letter}07'),
                (f'{letter}06', f'{letter}08'),
                (f'{letter}11', f'{letter}03'),
                (f'{letter}03', f'{letter}04'),
                (f'{letter}04', f'{letter}13'),
                (f'{letter}12', f'{letter}05'),
                (f'{letter}05', f'{letter}06'),
                (f'{letter}06', f'{letter}14')
            ])

        self.additions = {
            'R': ('F02', 'F04', 'F06',
                  'U02', 'U04', 'U06',
                  'B05', 'B03', 'B01',
                  'D02', 'D04', 'D06'),
            'L': ('F01', 'F03', 'F05',
                  'U01', 'U03', 'U05',
                  'B06', 'B04', 'B02',
                  'D01', 'D03', 'D05'),
            'F': ('L02', 'L04', 'L06',
                  'U11', 'U03', 'U04',
                  'R05', 'R03', 'R01',
                  'D06', 'D05', 'D12'),
            'B': ('L01', 'L03', 'L05',
                  'U12', 'U05', 'U06',
                  'R06', 'R04', 'R02',
                  'D04', 'D03', 'D11'),
            'U': ('F12', 'F05', 'F06',
                  'R12', 'R05', 'R06',
                  'B12', 'B05', 'B06',
                  'L12', 'L05', 'L06'),
            'D': ('F11', 'F03', 'F04',
                  'R11', 'R03', 'R04',
                  'B11', 'B03', 'B04',
                  'L11', 'L03', 'L04')
        }

        self.angle = 10
        self.exchange_axis = {
            'R': 'x',
            'L': '-x',
            'U': '-y',
            'D': 'y',
            'F': 'z',
            'B': '-z'
        }
        '''
        self.colors = {
            'R': 'red',
            'F': 'white',
            'U': 'blue',
            'L': 'orange',
            'B': 'yellow',
            'D': 'green'
        }
        '''


# NEW_PART ----------------------------------------------


class CubeConfig:
    def __init__(self, n):
        self.n = n
        self.size = Config().size / self.n

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
