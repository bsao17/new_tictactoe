import os
from PyQt5 import QtWidgets
from tictactoe_ui import Ui_MainWindow
import sys

# variable d'environnement afin d'utiliser wayland et non x11 sur Ubuntu
os.environ['QT_QPA_PLATFORM'] = 'wayland'


# Point d'entrée de l'application
class Tictactoe_main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Tictactoe_main, self).__init__()
        # Initialisation de l'interface Ui_MainWindow
        self.setupUi(self)
        self.pushButton_1.clicked.connect()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Tictactoe_main()
    window.show()

    app.exec_()
