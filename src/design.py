# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1304, 858)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1304, 858))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadModel = QtWidgets.QPushButton(self.centralwidget)
        self.loadModel.setGeometry(QtCore.QRect(1110, 70, 161, 31))
        self.loadModel.setObjectName("loadModel")
        self.models = QtWidgets.QComboBox(self.centralwidget)
        self.models.setGeometry(QtCore.QRect(1110, 31, 161, 31))
        self.models.setObjectName("models")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.scaleSlider = QtWidgets.QSlider(self.centralwidget)
        self.scaleSlider.setGeometry(QtCore.QRect(1110, 130, 161, 22))
        self.scaleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.scaleSlider.setObjectName("scaleSlider")
        self.up = QtWidgets.QPushButton(self.centralwidget)
        self.up.setGeometry(QtCore.QRect(1170, 170, 41, 41))
        self.up.setObjectName("up")
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(1210, 210, 41, 41))
        self.right.setObjectName("right")
        self.down = QtWidgets.QPushButton(self.centralwidget)
        self.down.setGeometry(QtCore.QRect(1170, 210, 41, 41))
        self.down.setObjectName("down")
        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(1130, 210, 41, 41))
        self.left.setObjectName("left")
        self.up_right = QtWidgets.QPushButton(self.centralwidget)
        self.up_right.setGeometry(QtCore.QRect(1210, 170, 41, 41))
        self.up_right.setObjectName("up_right")
        self.up_left = QtWidgets.QPushButton(self.centralwidget)
        self.up_left.setGeometry(QtCore.QRect(1130, 170, 41, 41))
        self.up_left.setObjectName("up_left")
        self.canvas = QtWidgets.QWidget(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(30, 30, 1050, 760))
        self.canvas.setStyleSheet("border: 3px solid black ")
        self.canvas.setObjectName("canvas")
        self.gridLayout = QtWidgets.QGridLayout(self.canvas)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadModel.setText(_translate("MainWindow", "Загрузить"))
        self.models.setItemText(0, _translate("MainWindow", "Кубик Рубика"))
        self.models.setItemText(1, _translate("MainWindow", "Пирамидка"))
        self.models.setItemText(2, _translate("MainWindow", "Мегаминкс"))
        self.up.setText(_translate("MainWindow", "U"))
        self.right.setText(_translate("MainWindow", "R"))
        self.down.setText(_translate("MainWindow", "D"))
        self.left.setText(_translate("MainWindow", "L"))
        self.up_right.setText(_translate("MainWindow", "UR"))
        self.up_left.setText(_translate("MainWindow", "UL"))
