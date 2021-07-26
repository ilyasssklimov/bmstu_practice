from edge import Edge
from point import Point


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
        cfg = Config()
        size = cfg.size
        dx, dy, dz = cfg.dx, cfg.dy, cfg.dz

        '''
        R - right side
        L - left side
        U - up side
        D - down side
        F - front side
        B - back side
        '''
        self.vertices = [
            Point(-size + dx, -size + dy, -size + dz),  # LBU
            Point(size + dx, -size + dy, -size + dz),  # RBU
            Point(size + dx, size + dy, -size + dz),  # RBD
            Point(-size + dx, size + dy, -size + dz),  # LBD

            Point(-size + dx, -size + dy, size + dz),  # LFU
            Point(size + dx, -size + dy, size + dz),  # RFU
            Point(size + dx, size + dy, size + dz),  # RFD
            Point(-size + dx, size + dy, size + dz),  # LFD
        ]

        self.edges = [
            Edge(0, 1),
            Edge(1, 2),
            Edge(2, 3),
            Edge(3, 0),

            Edge(0, 4),
            Edge(1, 5),
            Edge(2, 6),
            Edge(3, 7),

            Edge(4, 5),
            Edge(5, 6),
            Edge(6, 7),
            Edge(7, 4)
        ]

        self.inside_vertices = [
            self.vertices[7].add_x(size * 2 * (1 / 3)),
            self.vertices[4].add_x(size * 2 * (1 / 3)),

            self.vertices[7].add_x(size * 2 * (2 / 3)),
            self.vertices[4].add_x(size * 2 * (2 / 3)),

            self.vertices[6].add_z(-size * 2 * (1 / 3)),
            self.vertices[5].add_z(-size * 2 * (1 / 3)),

            self.vertices[6].add_z(-size * 2 * (2 / 3)),
            self.vertices[5].add_z(-size * 2 * (2 / 3)),

            self.vertices[2].add_x(-size * 2 * (1 / 3)),
            self.vertices[1].add_x(-size * 2 * (1 / 3)),

            self.vertices[2].add_x(-size * 2 * (2 / 3)),
            self.vertices[1].add_x(-size * 2 * (2 / 3)),

            self.vertices[3].add_z(size * 2 * (1 / 3)),
            self.vertices[0].add_z(size * 2 * (1 / 3)),

            self.vertices[3].add_z(size * 2 * (2 / 3)),
            self.vertices[0].add_z(size * 2 * (2 / 3)),

            self.vertices[7].add_y(-size * 2 * (1 / 3)),
            self.vertices[6].add_y(-size * 2 * (1 / 3)),

            self.vertices[7].add_y(-size * 2 * (2 / 3)),
            self.vertices[6].add_y(-size * 2 * (2 / 3)),

            self.vertices[2].add_y(-size * 2 * (1 / 3)),
            self.vertices[2].add_y(-size * 2 * (2 / 3)),

            self.vertices[3].add_y(-size * 2 * (1 / 3)),
            self.vertices[3].add_y(-size * 2 * (2 / 3)),
        ]

        self.inside_edges = [
            Edge(0, 1),
            Edge(2, 3),
            Edge(4, 5),
            Edge(6, 7),
            Edge(8, 9),
            Edge(10, 11),
            Edge(12, 13),
            Edge(14, 15),

            Edge(0, 10),
            Edge(1, 11),
            Edge(2, 8),
            Edge(3, 9),
            Edge(4, 14),
            Edge(5, 15),
            Edge(6, 12),
            Edge(7, 13),

            Edge(16, 17),
            Edge(18, 19),
            Edge(17, 20),
            Edge(19, 21),
            Edge(20, 22),
            Edge(21, 23),
            Edge(22, 16),
            Edge(23, 18)
        ]