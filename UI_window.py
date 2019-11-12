#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

simple window creation test

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    win = QWidget()
    win.resize(1080, 970)
    win.move(300, 300)
    win.setWindowTitle('Simple')
    win.show()
    
    sys.exit(app.exec_())
    