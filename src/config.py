# TODO: возможно убрать классы и сделать "голые" данные


class Config:
    def __init__(self):
        self.size = 150
        self.width = 1050
        self.height = 760
        self.dx = self.width / 2 + 30
        self.dy = self.height / 2 + 30
        self.dz = 0


class CubeConfig:
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

        self.changes = {
            'R': ('F', 'U', 'B', 'D'),
            'L': ('B', 'U', 'F', 'D'),
            'F': ('L', 'U', 'R', 'D'),
            'B': ('R', 'U', 'L', 'D'),
            'U': ('L', 'F', 'R', 'B'),
            'D': ('R', 'F', 'L', 'B')
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