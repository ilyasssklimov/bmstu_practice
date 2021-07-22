from config import Config
from edge import Edge
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
from point import Point


class Model:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.dx = Config().dx
        self.dy = Config().dy
        self.dz = Config().dz
        self.k = 1

    def draw_model(self, painter):
        # TODO: брать размеры канваса из интерфейса
        pen = QPen(Qt.black)
        painter.setPen(pen)

        for edge in self.edges:
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


class Cube:
    def __init__(self):
        self.size = Config().size
        self.dx = Config().dx
        self.dy = Config().dy
        self.dz = Config().dz

        self.vertices = [
            Point(-self.size + self.dx, -self.size + self.dy, -self.size + self.dz),
            Point(self.size + self.dx, -self.size + self.dy, -self.size + self.dz),
            Point(self.size + self.dx, self.size + self.dy, -self.size + self.dz),
            Point(-self.size + self.dx, self.size + self.dy, -self.size + self.dz),

            Point(-self.size + self.dx, -self.size + self.dy, self.size + self.dz),
            Point(self.size + self.dx, -self.size + self.dy, self.size + self.dz),
            Point(self.size + self.dx, self.size + self.dy, self.size + self.dz),
            Point(-self.size + self.dx, self.size + self.dy, self.size + self.dz),
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

