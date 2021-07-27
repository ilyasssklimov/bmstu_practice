from mymath import Vector
from point import Point


class Matrix3d:
    def __init__(self, vector):
        self.matrix = []
        self.matrix.append(Vector(vector[4], Point(0, 0, 0)).get_vector())
        self.matrix.append(Vector(vector[0], vector[1]).get_vector())
        self.matrix.append(Vector(vector[2], vector[3]).get_vector())

    def get_minor(self, i):
        j = (i + 1) % 3
        k = (i + 2) % 3
        return self.matrix[1][j] * self.matrix[2][k] - self.matrix[2][j] * self.matrix[1][k]

    def get_determinant(self):
        result = []
        d = 0
        for i in range(3):
            minor = self.get_minor(i)
            result.append(minor)
            d += self.matrix[0][i] * minor

        result.append(d)
        return result


class MatrixBody:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        result = ''
        for i in range(len(self.coefficients)):
            for j in range(4):
                result += f'{self.coefficients[i][j]:^10.1f}'
            result += '\n'

        return result

    def negative(self, i):
        self.coefficients[i] = [-coefficient for coefficient in self.coefficients[i]]

    def multiplication(self, vector):
        result = []
        for i in range(len(self.coefficients)):
            tmp_result = 0
            for j in range(len(vector)):
                tmp_result += vector[j] * self.coefficients[i][j]
            result.append(tmp_result)

        return result

    def adjust(self, point):
        result = self.multiplication(point)
        for i in range(len(result)):
            if result[i] > 0:
                self.negative(i)

    def transform(self):
        pass

    def scale(self):
        pass
