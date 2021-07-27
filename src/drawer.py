from PyQt5.QtGui import QPainter


class QtDrawer(QPainter):
    # TODO: рисовать Брезенхемом с устранением ступенчатости (скорее всего)
    def create_line(self, *args):
        self.drawLine(*args)
