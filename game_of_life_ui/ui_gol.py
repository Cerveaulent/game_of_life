import sys
import os
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

dir_path = os.path.dirname(os.path.realpath(__file__))
window = uic.loadUi(os.path.join(dir_path, "mainwindow.ui"))
window.show()
app.exec()
