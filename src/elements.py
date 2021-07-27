import config
from edge import Edge
from mymath import add_repeats
from point import Point


class CubeCarcass:
    def __init__(self, vertices, edges):
        cfg = config.Config()
        dx, dy, dz = cfg.dx, cfg.dy, cfg.dz
        self.vertices = {k: Point(v[0] + dx, v[1] + dy, v[2] + dz) for k, v in vertices.items()}
        self.edges = [Edge(edge[0], edge[1]) for edge in edges]

    def draw(self, painter):
        for edge in self.edges:
            start, finish = self.vertices[edge.first], self.vertices[edge.second]
            painter.create_line(start.x, start.y, finish.x, finish.y)

    def get_edges_vertices(self, name):
        vertices = {k: v for k, v in self.vertices.items() if name in k}
        return vertices

    def transform(self, func):
        for key in self.vertices:
            func(key)

    def scale(self, k, center):
        self.transform(lambda key: self.vertices[key].scale(k, center))

    def move(self, point):
        self.transform(lambda key: self.vertices[key].move(point))

    def turn_ox(self, angle):
        self.transform(lambda key: self.vertices[key].turn_ox(angle))

    def turn_oy(self, angle):
        self.transform(lambda key: self.vertices[key].turn_oy(angle))

    def turn_oz(self, angle):
        self.transform(lambda key: self.vertices[key].turn_oz(angle))

    def create_plane_points(self):
        points = []
        sides = {'B': (0, 3), 'U': (0, 4), 'R': (1, 5), 'D': (2, 6), 'L': (3, 7), 'F': (8, 9)}

        for side in sides.values():
            points.append(add_repeats(
                self.edges[side[0]].get_points(self.vertices),
                self.edges[side[1]].get_points(self.vertices)))

        return points

    def get_sides(self):
        return [(0, 1, 2, 3), (0, 4, 8, 5), (1, 5, 9, 6), (2, 6, 10, 7), (3, 7, 11, 4), (8, 9, 10, 11)]


class CubeSide:
    def __init__(self, vertices, edges, name):
        self.vertices = {k: v for k, v in vertices.items() if name in k}
        self.edges = [edge for edge in edges if name in edge]
        self.name = name

    def draw(self, painter):
        for edge in self.edges:
            start, finish = self.vertices[edge.first], self.vertices[edge.second]
            painter.create_line(start.x, start.y, finish.x, finish.y)

    def transform(self, func):
        for key in self.vertices:
            func(key)

    def scale(self, k, center):
        self.transform(lambda key: self.vertices[key].scale(k, center))

    def move(self, point):
        self.transform(lambda key: self.vertices[key].move(point))

    def turn_ox(self, angle):
        self.transform(lambda key: self.vertices[key].turn_ox(angle))

    def turn_oy(self, angle):
        self.transform(lambda key: self.vertices[key].turn_oy(angle))

    def turn_oz(self, angle):
        self.transform(lambda key: self.vertices[key].turn_oz(angle))


class CubeSides:
    def __init__(self, vertices, edges, source):
        tmp = config.Config().size * 2
        vertices = {k: Point(source.vertices[v[0]].x + tmp * v[1],
                             source.vertices[v[0]].y + tmp * v[2],
                             source.vertices[v[0]].z + tmp * v[3])
                    for k, v in vertices.items()}
        edges = [Edge(edge[0], edge[1]) for edge in edges]

        self.sides = {
            'R': CubeSide(vertices, edges, 'R'),
            'L': CubeSide(vertices, edges, 'L'),
            'U': CubeSide(vertices, edges, 'U'),
            'D': CubeSide(vertices, edges, 'D'),
            'F': CubeSide(vertices, edges, 'F'),
            'B': CubeSide(vertices, edges, 'B')
        }

        self.changes = config.CubeConfig().changes

    def draw(self, painter):
        for side in self.sides:
            self.sides[side].draw(painter)

    def get_edges_vertices(self, name):
        change = self.changes[name]

        vertices = {k: v for k, v in self.sides[name].vertices.items() if name in k}
        for i in range(2, 8, 2):
            for j in range(4):
                vertices[f'{change[i]}0{i}'] = self.sides[change[i]].vertices[f'{change[i]}0{i}']

        '''
        edges = [edge for edge in self.sides[name].edges if name in edge]
        for i in range(4):
            edges.extend([
                Edge(f'{change[i]}02', f'{change[i]}04'),
                Edge(f'{change[i]}04', f'{change[i]}06'),
                Edge(f'{change[i]}06', f'{change[(i + 1) % 4]}02')
            ])
        '''

        return vertices

    def transform(self, func):
        for side in self.sides:
            func(side)

    def scale(self, k, center):
        self.transform(lambda side: self.sides[side].scale(k, center))

    def move(self, point):
        self.transform(lambda side: self.sides[side].move(point))

    def turn_ox(self, angle):
        self.transform(lambda side: self.sides[side].turn_ox(angle))

    def turn_oy(self, angle):
        self.transform(lambda side: self.sides[side].turn_oy(angle))

    def turn_oz(self, angle):
        self.transform(lambda side: self.sides[side].turn_oz(angle))


'''
class CubeEdge:
    def __init__(self, carcass, sides, name):
        changes = {
            'R': ('F', 'U', 'B', 'D'),
            'L': ('B', 'U', 'F', 'D'),
            'F': ('L', 'U', 'R', 'D'),
            'B': ('R', 'U', 'L', 'D'),
            'U': ('L', 'F', 'R', 'B'),
            'D': ('R', 'F', 'L', 'B')
        }
        change = changes[name]

        self.vertices = {k: v for k, v in carcass.vertices.items() if name in k}

        self.vertices.update({k: v for k, v in sides[name].vertices.items() if name in k})

        for i in range(2, 8, 2):
            for j in range(4):
                self.vertices[f'{change[i]}0{i}'] = sides[change[i]].vertices[f'{change[i]}0{i}']

        self.edges = [edge for edge in sides[name].edges if name in edge]
        for i in range(4):
            self.edges.extend([
                Edge(f'{change[i]}02', f'{change[i]}04'),
                Edge(f'{change[i]}04', f'{change[i]}06'),
                Edge(f'{change[i]}06', f'{change[(i + 1) % 4]}02')
            ])
'''


class CubeEdges:
    def __init__(self):
        self.vertices = None

    def get_vertices(self, carcass, sides, name):
        self.vertices = carcass.get_edges_vertices(name)
        self.vertices.update(sides.get_edges_vertices(name))
