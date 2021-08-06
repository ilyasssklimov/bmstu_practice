import sys
from random import random

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication

LINES = [
    (500*random(), 500*random(), 500*random(), 500*random())
    for _ in range(50)
]

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.max    = len(LINES)
        self.cursor = 0
        self.show()

        self.paint = False

        timer = QTimer(self)
        timer.timeout.connect(self.onTimeout)
        timer.start(250)

    def paintEvent(self, e):
        painter = QPainter(self)
        if self.paint:
            self.drawsetpbystep(painter)

    def onTimeout(self):
        self.paint = True
        self.update()

    def drawsetpbystep(self, painter):
        if self.cursor < self.max:
            painter.drawLine(*LINES[self.cursor])
            self.cursor += 1
        self.paint = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec_())