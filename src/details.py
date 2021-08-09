import config
from copy import deepcopy
from mymath import find_by_key, add_repeats
from point import Point


# TODO: наследовать детьали от одного класса
# TODO: убрать дублирование кода, рефакторинг!


class Detail:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def __str__(self):
        result = 'Detail\n[\n'
        for vertex in self.vertices:
            result += f'    {vertex},\n'
        result += ']\n'
        return result

    def turn_ox(self, angle):
        for vertex in self.vertices:
            vertex.turn_ox(angle)

    def turn_oy(self, angle):
        for vertex in self.vertices:
            vertex.turn_oy(angle)

    def turn_oz(self, angle):
        for vertex in self.vertices:
            vertex.turn_oz(angle)

    def move(self, offset):
        for vertex in self.vertices:
            vertex.move(offset)

    def scale(self, k, point):
        for vertex in self.vertices:
            vertex.scale(k, point)

    def turn_ox_funcs(self, sin_angle, cos_angle):
        for vertex in self.vertices:
            vertex.turn_ox_funcs(sin_angle, cos_angle)

    def turn_oy_funcs(self, sin_angle, cos_angle):
        for vertex in self.vertices:
            vertex.turn_oy_funcs(sin_angle, cos_angle)

    def turn_oz_funcs(self, sin_angle, cos_angle):
        for vertex in self.vertices:
            vertex.turn_oz_funcs(sin_angle, cos_angle)

    def draw(self, painter, visible_sides):
        for key, edge in self.edges.items():
            if set(visible_sides) & set(key):
                start, finish = self.vertices[edge.first], self.vertices[edge.second]
                painter.create_line(start.x, start.y, finish.x, finish.y)


class Corner(Detail):
    def __init__(self, vertices, edges, offset):
        super().__init__(vertices, edges)
        self.move(offset)
        self.move(config.Config().center)


class Rib(Detail):
    def __init__(self, vertices, edges, offset):
        super().__init__(vertices, edges)
        self.move(offset)
        self.move(config.Config().center)


class Center(Detail):
    def __init__(self, vertices, edges, offset, side):
        super().__init__(vertices, edges)
        self.move(offset)
        self.move(config.Config().center)
        self.side = side

    def draw(self, painter, visible_sides=None):
        for edge in self.edges:
            start, finish = self.vertices[edge.first], self.vertices[edge.second]
            painter.create_line(start.x, start.y, finish.x, finish.y)


class Corners:
    def __init__(self, n):
        cfg = config.CubeConfig(n)
        vertices, edges = cfg.get_eccentric_data()
        positions = cfg.get_offset_corners()

        self.corners = {}
        for key, value in positions.items():
            self.corners[key] = Corner(deepcopy(vertices), edges, Point(*value))

    def draw(self, painter, visible_sides):
        for key in self.corners:
            self.corners[key].draw(painter, visible_sides)

    def move(self, point):
        for key in self.corners:
            self.corners[key].move(point)

    def turn_ox(self, angle):
        for key in self.corners:
            self.corners[key].turn_ox(angle)

    def turn_oy(self, angle):
        for key in self.corners:
            self.corners[key].turn_oy(angle)

    def turn_oz(self, angle):
        for key in self.corners:
            self.corners[key].turn_oz(angle)

    def scale(self, k, point):
        for key in self.corners:
            self.corners[key].scale(k, point)

    def turn_ox_funcs(self, sin_angle, cos_angle):
        for key in self.corners:
            self.corners[key].turn_ox_funcs(sin_angle, cos_angle)

    def turn_oy_funcs(self, sin_angle, cos_angle):
        for key in self.corners:
            self.corners[key].turn_oy_funcs(sin_angle, cos_angle)

    def turn_oz_funcs(self, sin_angle, cos_angle):
        for key in self.corners:
            self.corners[key].turn_oz_funcs(sin_angle, cos_angle)

    def turn_side_oy(self, name, angle):
        for key in self.corners:
            if name in key:
                self.corners[key].turn_oy(angle)

    def update_sides(self, side, direction):
        exchange = config.CubeConfig().get_exchanges_corners()[side]

        dir_range = range(len(exchange) - 2, -1, -1) if direction > 0 else range(1, len(exchange))
        saved_ind = -1 if direction > 0 else 0

        tmp = self.corners[find_by_key(self.corners, exchange[saved_ind])]
        for i in dir_range:
            i_to = find_by_key(self.corners, exchange[i + direction])
            i_from = find_by_key(self.corners, exchange[i])
            self.corners[i_to] = self.corners[i_from]
        self.corners[find_by_key(self.corners, exchange[saved_ind + direction])] = tmp

    def create_plane_points(self):
        sides = config.CubeConfig().get_sides()
        points = {}

        for key, value in sides.items():
            corner = self.corners[key[1]]
            points[key[0]] = add_repeats(corner.edges[value[0]].get_points(corner.vertices),
                                         corner.edges[value[1]].get_points(corner.vertices))

        return points


class Ribs:
    def __init__(self, n):
        self.ribs = {}
        if n > 2:
            cfg = config.CubeConfig(n)
            vertices, edges = cfg.get_eccentric_data()
            positions = cfg.get_offset_ribs()
            for key, value in positions.items():
                self.ribs[key] = []
                for position in positions[key]:
                    self.ribs[key].append(Rib(deepcopy(vertices), edges, Point(*position)))

    def draw(self, painter, visible_sides):
        for key in self.ribs:
            for rib in self.ribs[key]:
                rib.draw(painter, visible_sides)

    def move(self, point):
        for key in self.ribs:
            for rib in self.ribs[key]:
                rib.move(point)

    def turn_ox(self, angle):
        for key in self.ribs:
            for rib in self.ribs[key]:
                rib.turn_ox(angle)

    def turn_oy(self, angle):
        for key in self.ribs:
            for rib in self.ribs[key]:
                rib.turn_oy(angle)

    def turn_oz(self, angle):
        for key in self.ribs:
            for rib in self.ribs[key]:
                rib.turn_oz(angle)

    def scale(self, k, point):
        for key in self.ribs:
            for rib in self.ribs[key]:
                rib.scale(k, point)

    def turn_ox_funcs(self, sin_angle, cos_angle):
        for key in self.ribs:
            for rib in self.ribs[key]:
                rib.turn_ox_funcs(sin_angle, cos_angle)

    def turn_oy_funcs(self, sin_angle, cos_angle):
        for key in self.ribs:
            for rib in self.ribs[key]:
                rib.turn_oy_funcs(sin_angle, cos_angle)

    def turn_oz_funcs(self, sin_angle, cos_angle):
        for key in self.ribs:
            for rib in self.ribs[key]:
                rib.turn_oz_funcs(sin_angle, cos_angle)

    def turn_side_oy(self, name, angle):
        for key in self.ribs:
            if name in key:
                for rib in self.ribs[key]:
                    rib.turn_oy(angle)

    def update_sides(self, side, direction):
        exchange = config.CubeConfig().get_exchanges_ribs()[side]

        dir_range = range(len(exchange) - 2, -1, -1) if direction > 0 else range(1, len(exchange))
        saved_ind = -1 if direction > 0 else 0

        tmp = self.ribs[find_by_key(self.ribs, exchange[saved_ind])]
        for i in dir_range:
            i_to = find_by_key(self.ribs, exchange[i + direction])
            i_from = find_by_key(self.ribs, exchange[i])
            self.ribs[i_to] = self.ribs[i_from]
        self.ribs[find_by_key(self.ribs, exchange[saved_ind + direction])] = tmp


class Centers:
    def __init__(self, n):
        self.n = n
        self.sides_centers = self.init_sides_centers()
        self.centers = {}
        if n > 2:
            cfg = config.CubeConfig(n)
            positions = cfg.get_offset_centers()
            for key, value in positions.items():
                vertices, edges = cfg.get_center_data(key)
                self.centers[key] = []
                for position in positions[key]:
                    self.centers[key].append(Center(deepcopy(vertices), edges, Point(*position), key))

    def init_sides_centers(self):
        sides_centers = config.CubeConfig(self.n).get_sides_centers()
        for key in sides_centers:
            sides_centers[key].move(config.Config().center)

        return sides_centers

    def draw(self, painter, visible_sides):
        for key in visible_sides:
            for center in self.centers[key]:
                center.draw(painter)

    def move(self, point):
        for key in self.centers:
            for center in self.centers[key]:
                center.move(point)
        for key in self.sides_centers:
            self.sides_centers[key].move(point)

    def turn_ox(self, angle):
        for key in self.centers:
            for center in self.centers[key]:
                center.turn_ox(angle)
        for key in self.sides_centers:
            self.sides_centers[key].turn_ox(angle)

    def turn_oy(self, angle):
        for key in self.centers:
            for center in self.centers[key]:
                center.turn_oy(angle)
        for key in self.sides_centers:
            self.sides_centers[key].turn_oy(angle)

    def turn_oz(self, angle):
        for key in self.centers:
            for center in self.centers[key]:
                center.turn_oz(angle)
        for key in self.sides_centers:
            self.sides_centers[key].turn_oz(angle)

    def scale(self, k, point):
        for key in self.centers:
            for center in self.centers[key]:
                center.scale(k, point)
        for key in self.sides_centers:
            self.sides_centers[key].scale(k, point)

    def turn_ox_funcs(self, sin_angle, cos_angle):
        for key in self.centers:
            for center in self.centers[key]:
                center.turn_ox_funcs(sin_angle, cos_angle)

    def turn_oy_funcs(self, sin_angle, cos_angle):
        for key in self.centers:
            for center in self.centers[key]:
                center.turn_oy_funcs(sin_angle, cos_angle)

    def turn_oz_funcs(self, sin_angle, cos_angle):
        for key in self.centers:
            for center in self.centers[key]:
                center.turn_oz_funcs(sin_angle, cos_angle)

    def turn_side_oy(self, name, angle):
        for key in self.centers:
            if name in key:
                for rib in self.centers[key]:
                    rib.turn_oy(angle)

