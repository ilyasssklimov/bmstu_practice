from config import Config
from design import Ui_MainWindow
from drawer import QtDrawer
from models import Model, Cube
from mymath import sign
from point import Point
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = None
        self.k = 10
        self.angle = 15
        self.speed = 2
        self.load_model()

        self.x = 0
        self.y = 0
        self.cfg = Config()
        self.viewer = Point(self.cfg.dx, self.cfg.dy, self.cfg.dz)

        self.loadButton.clicked.connect(self.load_model)
        self.scaleSlider.valueChanged.connect(self.scale_model)

        self.rotate_y_.clicked.connect(lambda: self.turn_model_oy(self.angle))
        self.rotate_y.clicked.connect(lambda: self.turn_model_oy(-self.angle))
        self.rotate_x.clicked.connect(lambda: self.turn_model_ox(self.angle))
        self.rotate_x_.clicked.connect(lambda: self.turn_model_ox(-self.angle))
        self.rotate_z.clicked.connect(lambda: self.turn_model_oz(self.angle))
        self.rotate_z_.clicked.connect(lambda: self.turn_model_oz(-self.angle))
        # TODO: кастомизировать кнопки поворота

        self.right.clicked.connect(lambda: self.turn_edge('R'))
        self.up.clicked.connect(lambda: self.turn_edge('U'))
        self.front.clicked.connect(lambda: self.turn_edge('F'))

    def load_model(self):
        self.scaleSlider.setValue(10)
        self.k = 10
        model = self.models.currentText()

        if model == 'Кубик Рубика':
            # TODO: понять коммутативна ли операция поворота
            self.model = Cube()
            # self.model.turn_model_oy(45)
            # self.model.turn_model_ox(-30)
            self.update()
        else:
            print('Another model')

    def paintEvent(self, event):
        painter = QtDrawer()
        painter.begin(self)

        self.model.draw_model(painter)

        '''
        invisible_sides, inside_invisible_edges = self.model.get_invisible_sides(self.model.sides,
                                                                                 self.model.sides_edges,
                                                                                 self.model.inside_sides_edges)
        self.model.draw_model(painter, invisible_sides, inside_invisible_edges)
        '''
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

    def mousePressEvent(self, event):
        if self.x != event.x() or self.y != event.y():
            self.x, self.y = event.x(), event.y()

    def mouseMoveEvent(self, event):
        x1, y1 = event.x(), event.y()
        dx, dy = sign(x1 - self.x) * self.speed, sign(self.y - y1) * self.speed

        modifiers = QtWidgets.QApplication.keyboardModifiers()

        if modifiers == QtCore.Qt.ShiftModifier:
            self.turn_model_oz(dx)
        elif event.buttons() == QtCore.Qt.RightButton:
            if dx:
                self.turn_model_oy(dx)
            if dy:
                self.turn_model_ox(dy)

        self.x, self.y = x1, y1

    def turn_edge(self, name):
        self.model.turn_edge(name)
        self.update()
