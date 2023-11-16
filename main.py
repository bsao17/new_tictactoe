from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

from game_core.game_functions import messages
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
        self.player_one = Players("player_one", "x")
        self.player_two = Players("player_two", "o")

        # Connexions des signaux
        self.pushButton_stop.clicked.connect(self.on_close_triggered)
        self.pushButton_reset.clicked.connect(self.on_reset_triggered)

        for i in range(1, 17):
            button_number = f"pushButton_{i}"
            button = getattr(self, button_number)
            button.clicked.connect(lambda _, i=i: self.get_attribute_key(i))

    def get_attribute_key(self, iteration):
        button_name = f"pushButton_{iteration}"
        button = getattr(self, button_name)
        if not self.player_one.is_clicked:
            button.setText(self.player_one.label)
            self.player_one.is_clicked = True
        elif self.player_one.is_clicked:
            button.setText(self.player_two.label)
            self.player_one.is_clicked = False

    def closeEvent(self, event):
        """
        Handles the close event of the window.
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
    def on_reset_triggered(self):
        pass

    def check_align(self, position):
        # Ajouter la logique pour vérifier un nouvel alignement
        # et mettre à jour self.alignements_valides
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Tictactoe_main()
    window.show()

    app.exec_()
