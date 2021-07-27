class Edge:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f'{self.first}, {self.second}'

    def get_points(self, vertices):
        return [vertices[self.first], vertices[self.second]]

    def __contains__(self, item):
        return item in self.first or item in self.second
