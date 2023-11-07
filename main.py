import sys
import os
from tictactoe_gui import Ui_MainWindow

from PyQt5 import QtWidgets

os.environ['QT_QPA_PLATFORM'] = 'wayland'


class MyApplication(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.setupUi(self)  # Initialisation de l'interface utilisateur


app = QtWidgets.QApplication(sys.argv)
window = MyApplication()
window.show()

sys.exit(app.exec_())
