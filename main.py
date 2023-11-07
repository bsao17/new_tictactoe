import sys
import os
from tictactoe_ui import Ui_MainWindow

from PyQt5 import QtWidgets

os.environ['QT_QPA_PLATFORM'] = 'wayland'


class MyApplication(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.setupUi(self)  # Initialisation de l'interface Ui_MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApplication()
    window.show()

    app.exec_()
