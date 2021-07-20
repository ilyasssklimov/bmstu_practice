from PyQt5.QtCore import Qt

from design import Ui_MainWindow
from math import radians
from models import Model, Cube
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = None
        self.k = 10
        self.angle = radians(15)
        self.load_model()

        self.loadModel.clicked.connect(self.load_model)
        self.scaleSlider.valueChanged.connect(self.scale_model)

        self.right.clicked.connect(lambda: self.turn_model_oy(self.angle))
        self.left.clicked.connect(lambda: self.turn_model_oy(-self.angle))
        self.up.clicked.connect(lambda: self.turn_model_ox(self.angle))
        self.down.clicked.connect(lambda: self.turn_model_ox(-self.angle))
        self.up_right.clicked.connect(lambda: self.turn_model_oz(self.angle))
        self.up_left.clicked.connect(lambda: self.turn_model_oz(-self.angle))
        # TODO: кастомизировать кнопки поворота

    def load_model(self):
        self.scaleSlider.setValue(10)
        self.k = 10
        model = self.models.currentText()

        if model == 'Кубик Рубика':
            self.model = Model(Cube().vertices, Cube().edges)
            self.update()
        else:
            print('Another model')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.model.draw_model(painter)
        painter.end()

    def scale_model(self):
        if not self.model or self.k == self.scaleSlider.value():
            return

        self.k = self.scaleSlider.value()
        if self.k < 1:
            self.k = 1

        self.model.scale_model(self.k / 10)
        self.update()

    def wheelEvent(self, event):
        if not self.model:
            return

        self.k += event.angleDelta().y() / 120
        if self.k < 1:
            self.k = 1
        elif self.k > 100:
            self.k = 100

        self.scaleSlider.setValue(self.k)
        self.model.scale_model(self.k / 10)
        self.update()

    def turn_model_ox(self, angle):
        self.model.turn_model_ox(angle)
        self.update()

    def turn_model_oy(self, angle):
        self.model.turn_model_oy(angle)
        self.update()

    def turn_model_oz(self, angle):
        self.model.turn_model_oz(angle)
        self.update()

    def mouseMoveEvent(self, event):
        # print(help(event))
        print(event.x(), event.y())
        if event.buttons() == QtCore.Qt.LeftButton:
            print("Left Button Clicked")
        elif event.buttons() == QtCore.Qt.RightButton:
            print("Right Button Clicked")