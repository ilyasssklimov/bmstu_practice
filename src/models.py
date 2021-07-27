from collections import Counter
from config import Config, CubeConfig
from edge import Edge
from elements import CubeCarcass, CubeSides, CubeEdges
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
from point import Point
from matrix import Matrix3d, MatrixBody


class Model:
    # TODO: добавить матрицы преобразований (и для координат, и для матрицы тела)
    def __init__(self, carcass, sides, edges):
        self.carcass = carcass
        self.sides = sides
        self.edges = edges
        self.matrix_body = self.get_matrix_body(self.carcass.create_plane_points())
        '''
        self.vertices = vertices
        self.edges = edges
        self.inside_vertices = inside_vertices
        self.inside_edges = inside_edges
        '''
        self.k = 1

        cfg = Config()
        dx, dy, dz = cfg.dx, cfg.dy, cfg.dz
        self.center = Point(dx, dy, dz)

        self.matrix_center = [dx, dy, dz, 1]
        self.viewer = [dx, dy, 1000000, 0]

    def draw_model(self, painter):
        pen = QPen(Qt.black, 4)
        painter.setPen(pen)
        self.carcass.draw(painter)
        self.sides.draw(painter)
        '''
        for i, edge in enumerate(self.edges):
            if i not in invisible_sides:
                start, finish = self.vertices[edge.first], self.vertices[edge.second]
                painter.drawLine(start.x, start.y, finish.x, finish.y)

        for i, edge in enumerate(self.inside_edges):
            if i not in inside_invisible_sides:
                start, finish = self.inside_vertices[edge.first], self.inside_vertices[edge.second]
                painter.drawLine(start.x, start.y, finish.x, finish.y)
        '''

    def scale_model(self, k):
        k = k if k else 1
        tmp = k / self.k

        self.carcass.scale(tmp, self.center)
        self.sides.scale(tmp, self.center)

        '''
        for i in range(len(self.inside_vertices)):
            self.inside_vertices[i].scale(tmp, Point(self.dx, self.dy, self.dz))
        '''
        self.k = k

    def move_model(self, point):
        self.carcass.move(point)
        self.sides.move(point)

    def turn_model_ox(self, angle):
        self.move_model(-self.center)

        self.carcass.turn_ox(angle)
        self.sides.turn_ox(angle)

        self.move_model(self.center)

    def turn_model_oy(self, angle):
        self.move_model(-self.center)

        self.carcass.turn_oy(angle)
        self.sides.turn_oy(angle)

        self.move_model(self.center)

    def turn_model_oz(self, angle):
        self.move_model(-self.center)

        self.carcass.turn_oz(angle)
        self.sides.turn_oz(angle)

        self.move_model(self.center)

    def get_matrix_body(self, sides):
        coefficients = []

        for side in sides:
            plane = Matrix3d(side)
            coefficients.append(plane.get_determinant())

        matrix_body = MatrixBody(coefficients)
        matrix_body.adjust(self.matrix_center)

        return matrix_body

    def get_invisible_sides(self):
        result = self.matrix_body.multiplication(self.viewer)

        sides_edges = self.carcass.get_sides()
        invisible_sides = [number for side, value in zip(sides_edges, result) if value < 0 for number in side]
        invisible_sides = [key for key, value in Counter(invisible_sides).items() if value > 1]
        # inside_invisible_sides = [list(side) for side, value in zip(inside_sides_edges, result) if value < 0]

        # invisible_edges = []
        # inside_invisible_edges = []

        # for side in invisible_sides:
        #     invisible_edges.extend(side)
        # invisible_edges = [key for key, value in Counter(invisible_edges).items() if value > 1]

        # for side in inside_invisible_sides:
        #     inside_invisible_edges.extend(side)

        return invisible_sides # , inside_invisible_edges


class Cube(Model):
    def __init__(self):
        cfg = CubeConfig()
        carcass = CubeCarcass(cfg.vertices, cfg.carcass_edges)
        sides = CubeSides(cfg.inner_vertices, cfg.sides, carcass)
        edges = CubeEdges()

        super().__init__(carcass, sides, edges)

        '''
        vertices = CubeConfig().vertices
        edges = CubeConfig().edges
        inside_vertices = CubeConfig().inside_vertices
        inside_edges = CubeConfig().inside_edges
        super().__init__(vertices, edges, inside_vertices, inside_edges)

        self.sides = self.create_plane_points([(0, 3), (0, 4), (1, 5), (2, 6), (3, 7), (8, 9)])  # B, U, R, D, L, F
        self.sides_edges = [(0, 1, 2, 3), (0, 4, 8, 5), (1, 5, 9, 6), (2, 6, 10, 7), (3, 7, 11, 4), (8, 9, 10, 11)]

        self.inside_sides_edges = [(4, 5, 20, 21), (9, 11, 13, 15), (2, 3, 18, 19),
                                   (8, 10, 12, 14), (6, 7, 22, 23), (0, 1, 16, 17)]
        '''