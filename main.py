import os

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMessageBox

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

    def closeEvent(self, event):
        message_box = QMessageBox.question(self, "Question", "Souhaitez-vous vraiment quitter le jeu ?",
                                           QMessageBox.Yes | QMessageBox.No)
        if message_box == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  # Annuler la fermeture si l'utilisateur choisit 'Non'

    @pyqtSlot()
    def on_close_triggered(self):
        self.close()  # Déclencher directement la méthode closeEvent surchargée


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Tictactoe_main()
    window.show()

    app.exec_()
