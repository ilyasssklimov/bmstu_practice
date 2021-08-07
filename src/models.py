from collections import Counter
from config import Config, CubeConfig
from details import Corners, Ribs, Centers
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
from point import Point
from matrix import MatrixPlane, MatrixBody, MatrixTransform
from mymath import Vector, Angle
from math import asin, acos, degrees, cos


class Model:
    # TODO: добавить матрицы преобразований (и для координат, и для матрицы тела)
    def __init__(self, corners, ribs, centers, n):
        self.n = n
        self.corners = corners
        self.ribs = ribs
        self.centers = centers

        self.k = 1
        cfg = Config()
        dx, dy, dz = cfg.dx, cfg.dy, cfg.dz
        self.center_point = Point(dx, dy, dz)

        self.matrix_center = [dx, dy, dz, 1]
        self.viewer = [dx, dy, 1000000, 0]

        self.matrix_body = None
        self.set_matrix_body()

        # self.transform_matrix = MatrixTransform()
        self.visible_sides = []
        '''
        self.vertices = vertices
        self.edges = edges
        self.inside_vertices = inside_vertices
        self.inside_edges = inside_edges
        '''

    def draw(self, painter):
        self.set_visible_sides()

        pen = QPen(Qt.black, 4)
        painter.setPen(pen)
        self.corners.draw(painter)
        self.ribs.draw(painter)
        self.centers.draw(painter)

    def scale(self, k):
        k = k if k else 1
        tmp = k / self.k

        self.corners.scale(tmp, self.center_point)
        self.ribs.scale(tmp, self.center_point)
        self.centers.scale(tmp, self.center_point)

        self.k = k

    def move(self, point):
        self.corners.move(point)
        self.ribs.move(point)
        self.centers.move(point)

    def turn_ox(self, angle):
        self.move(-self.center_point)

        self.corners.turn_ox(angle)
        self.ribs.turn_ox(angle)
        self.centers.turn_ox(angle)

        self.move(self.center_point)

    def turn_oy(self, angle):
        self.move(-self.center_point)

        self.corners.turn_oy(angle)
        self.ribs.turn_oy(angle)
        self.centers.turn_oy(angle)

        self.move(self.center_point)

    def turn_oz(self, angle):
        self.move(-self.center_point)

        self.corners.turn_oz(angle)
        self.ribs.turn_oz(angle)
        self.centers.turn_oz(angle)

        self.move(self.center_point)

    def turn_ox_funcs(self, sin_angle, cos_angle):
        self.corners.turn_ox_funcs(sin_angle, cos_angle)
        self.ribs.turn_ox_funcs(sin_angle, cos_angle)
        self.centers.turn_ox_funcs(sin_angle, cos_angle)

    def turn_oy_funcs(self, sin_angle, cos_angle):
        self.corners.turn_oy_funcs(sin_angle, cos_angle)
        self.ribs.turn_oy_funcs(sin_angle, cos_angle)
        self.centers.turn_oy_funcs(sin_angle, cos_angle)

    def turn_oz_funcs(self, sin_angle, cos_angle):
        self.corners.turn_oz_funcs(sin_angle, cos_angle)
        self.ribs.turn_oz_funcs(sin_angle, cos_angle)
        self.centers.turn_oz_funcs(sin_angle, cos_angle)

    def turn_side_elements(self, name, angle, alpha, beta):
        self.turn_oz_funcs(alpha.sin, alpha.cos)
        self.turn_ox_funcs(beta.sin, beta.cos)

        self.corners.turn_side_oy(name, angle)
        self.ribs.turn_side_oy(name, angle)
        self.centers.turn_side_oy(name, angle)

        self.turn_ox_funcs(-beta.sin, beta.cos)
        self.turn_oz_funcs(-alpha.sin, alpha.cos)

    def turn_side(self, name, angle):
        self.move(-self.center_point)

        # TODO: вынести в отдельную функцию и возможно создть класс с данными для поворота
        direction_vector = Vector(Point(0, 0, 0), self.centers.sides_centers[name])
        direction_vector.normalize()
        d = direction_vector.get_length_xy()

        alpha = Angle()  # to yz plane
        beta = Angle()  # to y
        try:
            alpha.set_cos(direction_vector.y / d)
            alpha.set_sin(direction_vector.x / d)
        except ZeroDivisionError:
            alpha.set_cos(1)
            alpha.set_sin(0)
        beta.set_cos(d)
        beta.set_sin(-direction_vector.z)

        self.turn_side_elements(name, angle, alpha, beta)

        self.move(self.center_point)

    def update_sides(self, side, direction):
        self.corners.update_sides(side, direction)
        if self.n > 2:
            self.ribs.update_sides(side, direction)

    def set_matrix_body(self):
        '''
        sides = self.carcass.create_plane_points()
        coefficients = {}

        for key, value in sides.items():
            plane = MatrixPlane(value)
            coefficients[key] = plane.get_determinant()

        self.matrix_body = MatrixBody(coefficients)
        '''
        pass
        # TODO: понять, почему не работает
        # self.matrix_body.adjust(self.matrix_center)  # ???

    def set_visible_sides(self):
        self.set_matrix_body()
        # result = self.matrix_body.multiplication_vector(self.viewer)
        # sides = self.matrix_body.sides
        # sides_edges = self.carcass.sides

        # self.visible_sides = [side for side, value in zip(sides, result) if value >= 0]

        # for side, value in zip(sides_edges, result):

        # invisible_sides = [number for side, value in zip(sides_edges, result) if value < 0 for number in side]
        # invisible_sides = [key for key, value in Counter(invisible_sides).items() if value > 1]
        # inside_invisible_sides = [list(side) for side, value in zip(inside_sides_edges, result) if value < 0]

        # invisible_edges = []
        # inside_invisible_edges = []

        # for side in invisible_sides:
        #     invisible_edges.extend(side)
        # invisible_edges = [key for key, value in Counter(invisible_edges).items() if value > 1]

        # for side in inside_invisible_sides:
        #     inside_invisible_edges.extend(side)

        # return visible_sides  # , inside_invisible_edges

    def turn_edge(self, name):
        pass
        # self.edges.set_vertices(self.carcass, self.sides, name)
        # self.edges.turn_edge(name)


class Cube(Model):
    def __init__(self, n):
        corners = Corners(n)
        ribs = Ribs(n)
        centers = Centers(n)
        # cfg = CubeConfig()
        # carcass = CubeCarcass(cfg.vertices, cfg.carcass_edges)
        # sides = CubeSides(cfg.inner_vertices, cfg.sides, carcass)
        # edges = CubeEdges()

        super().__init__(corners, ribs, centers, n)

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