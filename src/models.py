from collections import Counter
from config import Config
from edge import Edge
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
from point import Point
from matrix import Matrix3d, MatrixBody
from mymath import remove_repeats


class Model:
    # TODO: добавить матрицы преобразований (и для координат, и для матрицы тела)
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.k = 1

        cfg = Config()
        self.dx, self.dy, self.dz = cfg.dx, cfg.dy, cfg.dz
        self.center = [self.dx, self.dy, self.dz, 1]
        self.viewer = [self.dx, self.dy, 1000000, 0]

    def draw_model(self, painter, invisible_sides):
        # TODO: брать размеры канваса из интерфейса
        pen = QPen(Qt.black)
        painter.setPen(pen)

        for i, edge in enumerate(self.edges):
            if i not in invisible_sides:
                start, finish = self.vertices[edge.first], self.vertices[edge.second]
                painter.drawLine(start.x, start.y, finish.x, finish.y)

    def move_model(self, point):
        for i in range(len(self.vertices)):
            self.vertices[i].move(point)

    def scale_model(self, k):
        k = k if k else 1
        tmp = k / self.k

        for i in range(len(self.vertices)):
            self.vertices[i].scale(tmp, Point(self.dx, self.dy, self.dz))

        self.k = k

    def turn_model_ox(self, angle):
        self.move_model(Point(-self.dx, -self.dy, -self.dz))
        for i in range(len(self.vertices)):
            self.vertices[i].turn_ox(angle)
        self.move_model(Point(self.dx, self.dy, self.dz))

    def turn_model_oy(self, angle):
        self.move_model(Point(-self.dx, -self.dy, -self.dz))
        for i in range(len(self.vertices)):
            self.vertices[i].turn_oy(angle)
        self.move_model(Point(self.dx, self.dy, self.dz))

    def turn_model_oz(self, angle):
        self.move_model(Point(-self.dx, -self.dy, -self.dz))
        for i in range(len(self.vertices)):
            self.vertices[i].turn_oz(angle)
        self.move_model(Point(self.dx, self.dy, self.dz))

    def create_plane_points(self, numbers):
        points = []
        for number in numbers:
            points.append(remove_repeats(
                self.edges[number[0]].get_points(self.vertices),
                self.edges[number[1]].get_points(self.vertices)))

        return points

    def get_matrix_body(self, sides):
        coefficients = []

        for side in sides:
            plane = Matrix3d(side)
            coefficients.append(plane.get_determinant())

        matrix_body = MatrixBody(coefficients)
        matrix_body.adjust(self.center)

        return matrix_body

    def get_invisible_sides(self, sides, sides_edges):
        matrix_body = self.get_matrix_body(sides)
        result = matrix_body.multiplication(self.viewer)

        invisible_sides = [list(side) for side, value in zip(sides_edges, result) if value < 0]

        invisible_edges = []
        for side in invisible_sides:
            invisible_edges.extend(side)
        invisible_edges = [key for key, value in Counter(invisible_edges).items() if value > 1]

        return invisible_edges


class Cube(Model):
    def __init__(self):
        cfg = Config()
        size = cfg.size
        dx, dy, dz = cfg.dx, cfg.dy, cfg.dz

        vertices = [
            Point(-size + dx, -size + dy, -size + dz),
            Point(size + dx, -size + dy, -size + dz),
            Point(size + dx, size + dy, -size + dz),
            Point(-size + dx, size + dy, -size + dz),

            Point(-size + dx, -size + dy, size + dz),
            Point(size + dx, -size + dy, size + dz),
            Point(size + dx, size + dy, size + dz),
            Point(-size + dx, size + dy, size + dz),
        ]

        edges = [
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

        super().__init__(vertices, edges)
        self.sides = self.create_plane_points([(0, 3), (0, 4), (1, 5), (2, 6), (3, 7), (8, 9)])
        self.sides_edges = [(0, 1, 2, 3), (0, 4, 8, 5), (1, 5, 9, 6), (2, 6, 10, 7), (3, 7, 11, 4), (8, 9, 10, 11)]