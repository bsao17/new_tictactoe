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

        self.player = None
        self.player_one = Players(self, "player_one", "x")
        self.player_two = Players(self, "player_two", "o")

        # Connexions des signaux
        self.pushButton_stop.clicked.connect(self.on_close_triggered)
        self.pushButton_start.clicked.connect(self.on_start_triggered)
        self.pushButton_reset.clicked.connect(self.on_reset_triggered)

        for i in range(1, 17):
            match i:
                case 1:
                    self.pushButton_1.clicked.connect(lambda _: self.get_attribute_key(i))
                case 2:
                    self.pushButton_2.clicked.connect(lambda _: self.get_attribute_key(i))
                case 3:
                    self.pushButton_3.clicked.connect(lambda _: self.get_attribute_key(i))
                case 4:
                    self.pushButton_4.clicked.connect(lambda _: self.get_attribute_key(i))
                case 5:
                    self.pushButton_5.clicked.connect(lambda _: self.get_attribute_key(i))
                case 6:
                    self.pushButton_6.clicked.connect(lambda _: self.get_attribute_key(i))
                case 7:
                    self.pushButton_7.clicked.connect(lambda _: self.get_attribute_key(i))
                case 8:
                    self.pushButton_8.clicked.connect(lambda _: self.get_attribute_key(i))
                case 9:
                    self.pushButton_9.clicked.connect(lambda _: self.get_attribute_key(i))
                case 10:
                    self.pushButton_10.clicked.connect(lambda _: self.get_attribute_key(i))
                case 11:
                    self.pushButton_11.clicked.connect(lambda _: self.get_attribute_key(i))
                case 12:
                    self.pushButton_12.clicked.connect(lambda _: self.get_attribute_key(i))
                case 13:
                    self.pushButton_13.clicked.connect(lambda _: self.get_attribute_key(i))
                case 14:
                    self.pushButton_14.clicked.connect(lambda _: self.get_attribute_key(i))
                case 15:
                    self.pushButton_15.clicked.connect(lambda _: self.get_attribute_key(i))
                case 16:
                    self.pushButton_16.clicked.connect(lambda _: self.get_attribute_key(i))

    def get_attribute_key(self, iteration):
        button_name = f"pushButton_{iteration}"
        button = getattr(self, button_name)
        if iteration % 2 == 0:
            button.setText(self.player_one.label)
        else:
            button.setText(self.player_one.label)

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
