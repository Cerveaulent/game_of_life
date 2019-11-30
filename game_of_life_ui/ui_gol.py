import sys
import os
from PyQt5 import QtWidgets, QtGui, uic

app = QtWidgets.QApplication(sys.argv)

dir_path = os.path.dirname(os.path.realpath(__file__))
window = uic.loadUi(os.path.join(dir_path, "mainwindow.ui"))
print(type(window))
painter = QtGui.QPainter()
painter.begin(window)

painter.drawChord(9, 9, 912, 713, 0, 0)
window.show()
app.exec()
