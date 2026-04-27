from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMessageBox
from PySide6 import QtWidgets

from tictactoe_ui import Ui_MainWindow
import sys
from players.players import Players

from game_core.board import Board
from game_core.minimax_algo import find_best_move, evaluate_board


# Entry point for the program
class Tictactoe_main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Tictactoe_main, self).__init__()
        # Initialisation de l'interface Ui_MainWindow
        self.setupUi(self)

        self.player = None
        self.player_one = Players("player_one", "x")
        self.player_two = Players("player_two", "o")

        self.board = Board()

        # signals and slots connections
        self.pushButton_stop.clicked.connect(self.on_close_triggered)
        self.pushButton_reset.clicked.connect(self.on_reset_triggered)

        for i in range(1, 17):
            button_number = f"pushButton_{i}"
            button = getattr(self, button_number)
            button.clicked.connect(lambda _, j=i: self.get_attribute_key(j))

    def get_attribute_key(self, iteration):
        button_name = f"pushButton_{iteration}"
        button = getattr(self, button_name)
        
        # Convertir le numéro de bouton en coordonnées (1-16) -> (row, col)
        row = (iteration - 1) // 4
        col = (iteration - 1) % 4
        
        if not self.player_one.is_clicked:
            # Joueur humain (X) joue
            button.setFont(QFont("Arial", 50))
            button.setStyleSheet("color: red;")
            button.setText(self.player_one.label)
            button.setDisabled(True)
            self.player_one.toggle_player()
            
            # Mettre à jour le plateau
            self.board.board[row, col] = "X"
            
            # Vérifier si le joueur humain a gagné
            if evaluate_board(self.board) == 10:
                QMessageBox.information(self, "Victoire!", "Félicitations! Vous avez gagné!")
                self.reset_game()
                return
            
            # Vérifier si le plateau est plein
            if None not in self.board.board:
                QMessageBox.information(self, "Match nul!", "Le match est nul!")
                self.reset_game()
                return
            
            # L'IA joue (O)
            self.ai_play()
            
        elif self.player_one.is_clicked:
            button.setFont(QFont("Arial", 50))
            button.setStyleSheet("color: blue;")
            button.setText(self.player_two.label)
            button.setDisabled(True)
            self.player_one.toggle_player()

    def ai_play(self):
        """L'IA joue son coup."""
        best_move = find_best_move(self.board, "O")
        if best_move:
            row, col = best_move
            button_num = row * 4 + col + 1
            button_name = f"pushButton_{button_num}"
            button = getattr(self, button_name)
            
            button.setFont(QFont("Arial", 50))
            button.setStyleSheet("color: blue;")
            button.setText("o")
            button.setDisabled(True)
            
            # Mettre à jour le plateau
            self.board.board[row, col] = "O"
            
            # Vérifier si l'IA a gagné
            if evaluate_board(self.board) == -10:
                QMessageBox.information(self, "Défaite!", "L'IA a gagné! Plus de chance la prochaine fois.")
                self.reset_game()

    def reset_game(self):
        """Réinitialise le jeu."""
        self.board = Board()
        for i in range(1, 17):
            button = getattr(self, f"pushButton_{i}")
            button.setText("")
            button.setDisabled(False)
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

    def on_reset_triggered(self):
        self.reset_game()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Tictactoe_main()
    window.show()

    app.exec()
