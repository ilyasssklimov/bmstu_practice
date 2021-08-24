import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 500, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(100, 100)
        pixmap.fill(QColor('grey'))
        painter.drawPixmap(self.rect(), pixmap)
        painter.setPen((QPen(QColor("green"))))
        painter.drawEllipse(100, 100, 30, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())