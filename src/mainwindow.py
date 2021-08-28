from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QColor

from config import Config
from design import Ui_MainWindow
from drawer import QtDrawer
from models import Cube
from mymath import sign
from point import Point
from PyQt5 import QtWidgets, QtCore


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = QRect(
            Config().offset_x + 3,
            Config().offset_y + 3,
            Config().width - 3,
            Config().height - 3
        )

        self.model = None
        self.k = 10
        self.angle = 15
        self.speed = 1
        self.sizeModel.setCurrentText('3x3x3')
        self.load_model()

        self.x = 0
        self.y = 0
        self.cfg = Config()
        self.viewer = Point(self.cfg.dx, self.cfg.dy, self.cfg.dz)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.turn_side)
        self.duration = 0
        self.turning_side = ''
        self.turning_direction = 0

        self.loadButton.clicked.connect(self.load_model)
        self.scaleSlider.valueChanged.connect(self.scale_model)
        self.sizeModel.currentTextChanged.connect(self.load_model)

        self.rotate_y_.clicked.connect(lambda: self.turn_model_oy(self.angle))
        self.rotate_y.clicked.connect(lambda: self.turn_model_oy(-self.angle))
        self.rotate_x.clicked.connect(lambda: self.turn_model_ox(self.angle))
        self.rotate_x_.clicked.connect(lambda: self.turn_model_ox(-self.angle))
        self.rotate_z.clicked.connect(lambda: self.turn_model_oz(self.angle))
        self.rotate_z_.clicked.connect(lambda: self.turn_model_oz(-self.angle))
        # TODO: кастомизировать кнопки поворота

        self.right.clicked.connect(lambda: self.start_turning_side('R', 1))
        self.up.clicked.connect(lambda: self.start_turning_side('U', 1))
        self.front.clicked.connect(lambda: self.start_turning_side('F', 1))
        self.left.clicked.connect(lambda: self.start_turning_side('L', 1))
        self.down.clicked.connect(lambda: self.start_turning_side('D', 1))
        self.back.clicked.connect(lambda: self.start_turning_side('B', 1))

        self.right_.clicked.connect(lambda: self.start_turning_side('R', -1))
        self.up_.clicked.connect(lambda: self.start_turning_side('U', -1))
        self.front_.clicked.connect(lambda: self.start_turning_side('F', -1))
        self.left_.clicked.connect(lambda: self.start_turning_side('L', -1))
        self.down_.clicked.connect(lambda: self.start_turning_side('D', -1))
        self.back_.clicked.connect(lambda: self.start_turning_side('B', -1))

    def load_model(self):
        self.scaleSlider.setValue(10)
        self.k = 10
        model = self.models.currentText()

        if model == 'Кубик Рубика':
            self.model = Cube(int(self.sizeModel.currentText().split('x')[0]))
            self.model.turn_oy(45)
            self.model.turn_ox(-30)
            self.update()
        else:
            print('Another model')

    def paintEvent(self, event):
        painter = QtDrawer()
        painter.begin(self)
        painter.setBrush(QColor('white'))
        painter.drawRect(self.image)
        self.model.draw(painter)
        painter.end()

    def scale_model(self):
        if not self.model or self.k == self.scaleSlider.value():
            return

        self.k = self.scaleSlider.value()
        if self.k < 1:
            self.k = 1

        self.model.scale(self.k / 10)
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
        self.model.scale(self.k / 10)
        self.update()

    def turn_model_ox(self, angle):
        self.model.turn_ox(angle)
        self.update()

    def turn_model_oy(self, angle):
        self.model.turn_oy(angle)
        self.update()

    def turn_model_oz(self, angle):
        self.model.turn_oz(angle)
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

    def set_turning_params(self, name, direction):
        self.turning_side = name
        self.turning_direction = direction

    def start_turning_side(self, name, direction):
        if self.duration == 0:
            self.set_turning_params(name, direction)
            self.timer.start(0)

    def turn_side(self):
        self.duration += 1
        self.model.turn_side(self.turning_side, self.turning_direction)

        if self.duration >= 90:
            self.update_sides()
            self.timer.stop()
            self.duration = 0

        self.update()

    def update_sides(self):
        self.model.update_sides(self.turning_side, self.turning_direction)
    