# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/ccantin/Documents/game_of_life/game_of_life_ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.game_win = QtWidgets.QVBoxLayout()
        self.game_win.setContentsMargins(-1, 700, -1, -1)
        self.game_win.setSpacing(6)
        self.game_win.setObjectName("game_win")
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.game_win)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delay = QtWidgets.QSpinBox(self.centralwidget)
        self.delay.setWrapping(False)
        self.delay.setFrame(True)
        self.delay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.delay.setMinimum(1)
        self.delay.setMaximum(99999)
        self.delay.setProperty("value", 1000)
        self.delay.setObjectName("delay")
        self.horizontalLayout_2.addWidget(self.delay)
        self.l_delay = QtWidgets.QLabel(self.centralwidget)
        self.l_delay.setObjectName("l_delay")
        self.horizontalLayout_2.addWidget(self.l_delay)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setObjectName("play")
        self.horizontalLayout.addWidget(self.play)
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setObjectName("pause")
        self.horizontalLayout.addWidget(self.pause)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setObjectName("reset")
        self.horizontalLayout_3.addWidget(self.reset)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_delay.setText(_translate("MainWindow", "Delay (ms)"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.pause.setText(_translate("MainWindow", "Pause"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.reset.setText(_translate("MainWindow", "Reset all"))
