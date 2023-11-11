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
    def __init__(self, i=None):
        super(Tictactoe_main, self).__init__()
        # Initialisation de l'interface Ui_MainWindow
        self.setupUi(self)

        self.grid_1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.grid_2 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],]

        # Connexions des signaux
        self.pushButton_stop.clicked.connect(self.on_close_triggered)
        self.pushButton_start.clicked.connect(self.on_start_triggered)
        self.pushButton_reset.clicked.connect(self.on_reset_triggered)

        for i in range(1, 17):
            if i % 2 == 0:
                self.player = 2
            else:
                self.player = 1
            match i:
                case 1:
                    if self.player == self.player_one:
                        self.pushButton_1.setText("x")
                    else:
                        self.pushButton_1.setText("o")
                case 2:
                    if self.player == self.player_one:
                        self.pushButton_5.setText("x")
                    else:
                        self.pushButton_5.setText("o")
                case 3:
                    if self.player == self.player_one:
                        self.pushButton_9.setText("x")
                    else:
                        self.pushButton_9.setText("o")
                case 4:
                    if self.player == self.player_one:
                        self.pushButton_2.setText("x")
                    else:
                        self.pushButton_2.setText("o")
                case 5:
                    if self.player == self.player_one:
                        self.pushButton_6.setText("x")
                    else:
                        self.pushButton_6.setText("o")
                case 6:
                    if self.player == self.player_one:
                        self.pushButton_10.setText("x")
                    else:
                        self.pushButton_10.setText("o")
                case 7:
                    if self.player == self.player_one:
                        self.pushButton_3.setText("x")
                    else:
                        self.pushButton_3.setText("o")
                case 8:
                    if self.player == self.player_one:
                        self.pushButton_7.setText("x")
                    else:
                        self.pushButton_7.setText("o")
                case 9:
                    if self.player == self.player_one:
                        self.pushButton_11.setText("x")
                    else:
                        self.pushButton_11.setText("o")
                case 10:
                    if self.player == self.player_one:
                        self.pushButton_4.setText("x")
                    else:
                        self.pushButton_4.setText("o")
                case 11:
                    if self.player == self.player_one:
                        self.pushButton_8.setText("x")
                    else:
                        self.pushButton_8.setText("o")
                case 12:
                    if self.player == self.player_one:
                        self.pushButton_12.setText("x")
                    else:
                        self.pushButton_12.setText("o")
                case 13:
                    if self.player == self.player_one:
                        self.pushButton_13.setText("x")
                    else:
                        self.pushButton_13.setText("o")
                case 14:
                    if self.player == self.player_one:
                        self.pushButton_14.setText("x")
                    else:
                        self.pushButton_14.setText("o")
                case 15:
                    if self.player == self.player_one:
                        self.pushButton_15.setText("x")
                    else:
                        self.pushButton_15.setText("o")
                case 16:
                    if self.player == self.player_one:
                        self.pushButton_16.setText("x")
                    else:
                        self.pushButton_16.setText("o")


    def get_attribute_key(self, index):
        return lambda: messages(
            self, "Information", f"Case {index} clique !"
        )
        # TODO: Corriger l'affichage

    def closeEvent(self, event):
        """
        Handles the close event of the window.

        Args:
            event (QCloseEvent): The close event triggered by the user.

        Returns:
            None
        """
        message_box = QMessageBox.question(self, "Question", "Souhaitez-vous vraiment quitter le jeu ?",
                                           QMessageBox.Yes | QMessageBox.No)
        if message_box == QMessageBox.Yes:
            event.accept()  # Accepter la fermeture
        else:
            event.ignore()  # Annuler la fermeture

    @pyqtSlot()
    def on_close_triggered(self):
        """
        Trigger the overridden closeEvent method directly.

        This function is a slot that is triggered when the "close" action is triggered.
        It calls the closeEvent method which is overridden in the class.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        self.close()  # Déclencher directement la méthode closeEvent surchargée

    @pyqtSlot()
    def on_start_triggered(self):
        pass

    @pyqtSlot()
    def on_reset_triggered(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Tictactoe_main()
    window.show()

    app.exec_()
