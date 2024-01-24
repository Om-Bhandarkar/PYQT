from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def clicked():

    print("Clicked......!")        


def window():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setGeometry(200,200,300,300)
    main_window.setWindowTitle("Welcome")

    label = QtWidgets.QLabel(main_window)
    label.setText("My First Label")
    label.move(100,100)
    btn = QtWidgets.QPushButton(main_window)
    btn.setText("Click Me")
    btn.move(100,100)
    btn.clicked.connect(clicked)

    main_window.show()
    sys.exit(app.exec_())

window()