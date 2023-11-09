import os
from game_core.game_functions import messages
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from tictactoe_ui import Ui_MainWindow
import sys
from players.players import Players


# Point d'entrée de l'application
class Tictactoe_main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Tictactoe_main, self).__init__()
        # Initialisation de l'interface Ui_MainWindow
        self.setupUi(self)
        self.pushButton_stop.clicked.connect(self.on_close_triggered)

    @pyqtSlot()
    def on_close_triggered(self):
        messages(self, "Quitter","Souhaitez vous vraiment quitter le jeu ?")
        self.close()


if __name__ == '__main__':
    player_one = Players("Bruno", "X")
    print(repr(player_one))

    app = QtWidgets.QApplication(sys.argv)
    window = Tictactoe_main()
    window.show()

    app.exec_()
    print(str(player_one))
