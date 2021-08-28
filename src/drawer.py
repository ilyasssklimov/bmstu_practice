from mymath import find_y_min_max, sign
from PyQt5.QtGui import QPainter


class QtDrawer(QPainter):
    def create_line(self, x1, y1, x2, y2):
        self.drawLine(x1, y1, x2, y2)

    def set_pixel(self, x, y):
        self.drawLine(x, y, x + 1, y)

    def fill(self, vertices, edges):
        pass
