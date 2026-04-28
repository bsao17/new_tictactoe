from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMessageBox, QComboBox, QLabel
from PySide6 import QtWidgets

from tictactoe_ui import Ui_MainWindow
import sys
from players.players import Players

from game_core.board import Board
from game_core.minimax_algo import find_best_move, count_scores


# ---------------------------------------------------------------------------
# Entrée principale du programme
# ---------------------------------------------------------------------------

class Tictactoe_main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Tictactoe_main, self).__init__()
        self.setupUi(self)

        self.player_one = Players("player_one", "x")
        self.player_two = Players("player_two", "o")

        self.board = Board()
        self.difficulty = 5  # Par défaut: difficile
        self.game_mode = "ia"  # Par défaut: mode IA

        # --- Sélecteur de difficulté ---
        self.difficulty_label = QLabel("Difficulté:", self)
        self.difficulty_label.setGeometry(720, 10, 100, 25)

        self.difficulty_combo = QComboBox(self)
        self.difficulty_combo.setGeometry(720, 35, 120, 25)
        self.difficulty_combo.addItems(["Facile", "Moyen", "Difficile"])
        self.difficulty_combo.setCurrentIndex(2)
        self.difficulty_combo.currentIndexChanged.connect(self.change_difficulty)

        # --- Indicateur du tour du joueur ---
        self.turn_label = QLabel("À vous de jouer (X)", self)
        self.turn_label.setGeometry(10, 920, 880, 40)
        self.turn_label.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")
        self.turn_label.setAlignment(QtCore.Qt.AlignCenter)

        # --- Signaux ---
        self.pushButton_stop.clicked.connect(self.on_close_triggered)
        self.pushButton_reset.clicked.connect(self.on_reset_triggered)
        self.player_choice.currentIndexChanged.connect(self.change_game_mode)

        for i in range(1, 17):
            button = getattr(self, f"pushButton_{i}")
            button.clicked.connect(lambda _, j=i: self.get_attribute_key(j))

        # Affichage initial du score
        self._update_title()

    # -----------------------------------------------------------------------
    # Clic joueur humain
    # -----------------------------------------------------------------------

    def get_attribute_key(self, iteration):
        button = getattr(self, f"pushButton_{iteration}")

        row = (iteration - 1) // 4
        col = (iteration - 1) % 4

        if self.player_one.is_clicked:
            # Tour du joueur X (rouge)
            button.setFont(QFont("Arial", 50))
            button.setStyleSheet("color: red;")
            button.setText(self.player_one.label)
            button.setDisabled(True)
            self.player_one.toggle_player()

            self.board.board[row, col] = "X"
            self._update_title()
            self._update_turn_label()

            # Vérifier fin de partie
            if self.board.is_full():
                self._end_game()
                return

            # L'IA joue seulement en mode IA
            if self.game_mode == "ia":
                self.ai_play()

        else:
            # Tour du joueur O (bleu) — mode 2 joueurs
            button.setFont(QFont("Arial", 50))
            button.setStyleSheet("color: blue;")
            button.setText(self.player_two.label)
            button.setDisabled(True)
            self.player_one.toggle_player()

            self.board.board[row, col] = "O"
            self._update_title()
            self._update_turn_label()

            # Vérifier fin de partie
            if self.board.is_full():
                self._end_game()

    # -----------------------------------------------------------------------
    # Tour de l'IA
    # -----------------------------------------------------------------------

    def ai_play(self):
        """L'IA (O) joue le meilleur coup selon Minimax."""
        best_move = find_best_move(self.board, "O", self.difficulty)
        if best_move is None:
            return

        row, col = best_move
        button_num = row * 4 + col + 1
        button = getattr(self, f"pushButton_{button_num}")

        button.setFont(QFont("Arial", 50))
        button.setStyleSheet("color: blue;")
        button.setText("o")
        button.setDisabled(True)

        self.board.board[row, col] = "O"
        self._update_title()
        self._update_turn_label()

        if self.board.is_full():
            self._end_game()

    # -----------------------------------------------------------------------
    # Fin de partie — on compare les scores
    # -----------------------------------------------------------------------

    def _end_game(self):
        """Détermine le vainqueur selon le nombre d'alignements de 3."""
        score_x, score_o = count_scores(self.board)

        if score_x > score_o:
            if self.game_mode == "ia":
                msg = (f"🎉 Vous gagnez !\n\n"
                       f"Vos alignements (X) : {score_x}\n"
                       f"Alignements IA (O)  : {score_o}")
                title = "Victoire !"
            else:
                msg = (f"🎉 Le joueur X gagne !\n\n"
                       f"Alignements X : {score_x}\n"
                       f"Alignements O : {score_o}")
                title = "Victoire du joueur X !"
        elif score_o > score_x:
            if self.game_mode == "ia":
                msg = (f"😢 L'IA gagne !\n\n"
                       f"Alignements IA (O)  : {score_o}\n"
                       f"Vos alignements (X) : {score_x}")
                title = "Défaite !"
            else:
                msg = (f"🎉 Le joueur O gagne !\n\n"
                       f"Alignements O : {score_o}\n"
                       f"Alignements X : {score_x}")
                title = "Victoire du joueur O !"
        else:
            msg = (f"🤝 Match nul !\n\n"
                   f"Alignements X : {score_x}\n"
                   f"Alignements O : {score_o}")
            title = "Égalité !"

        QMessageBox.information(self, title, msg)
        self.reset_game()

    # -----------------------------------------------------------------------
    # Affichage du score en temps réel dans le titre de la fenêtre
    # -----------------------------------------------------------------------

    def _update_title(self):
        score_x, score_o = count_scores(self.board)
        mode_text = "vs IA" if self.game_mode == "ia" else "2 joueurs"
        self.setWindowTitle(
            f"Tic Tac Toe — {mode_text}  |  Alignements de 3  |  X : {score_x}  •  O : {score_o}"
        )

    # -----------------------------------------------------------------------
    # Reset
    # -----------------------------------------------------------------------

    def reset_game(self):
        """Réinitialise le plateau et l'interface."""
        self.board = Board()
        for i in range(1, 17):
            button = getattr(self, f"pushButton_{i}")
            button.setText("")
            button.setDisabled(False)
            button.setStyleSheet("")
        self.player_one.is_clicked = True  # C'est au tour du joueur X de commencer
        self._update_title()
        self._update_turn_label()

    # -----------------------------------------------------------------------
    # Mise à jour du label de tour
    # -----------------------------------------------------------------------

    def _update_turn_label(self):
        """Met à jour le texte indiquant quel joueur doit jouer."""
        if self.game_mode == "ia":
            # En mode IA, c'est toujours le joueur humain qui joue en premier (X)
            if self.player_one.is_clicked:
                self.turn_label.setText("À vous de jouer (X)")
                self.turn_label.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")
            else:
                self.turn_label.setText("L'IA réfléchit...")
                self.turn_label.setStyleSheet("font-size: 18px; font-weight: bold; color: blue;")
        else:
            # En mode 2 joueurs
            if self.player_one.is_clicked:
                self.turn_label.setText("Joueur X à vous de jouer")
                self.turn_label.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")
            else:
                self.turn_label.setText("Joueur O à vous de jouer")
                self.turn_label.setStyleSheet("font-size: 18px; font-weight: bold; color: blue;")

    # -----------------------------------------------------------------------
    # Événements fenêtre
    # -----------------------------------------------------------------------

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Quitter", "Souhaitez-vous vraiment quitter le jeu ?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def on_close_triggered(self):
        self.close()

    def on_reset_triggered(self):
        self.reset_game()

    def change_game_mode(self, index):
        """0 = 1 joueur (IA), 1 = 2 joueurs."""
        self.game_mode = ["ia", "2_players"][index]
        # Activer/désactiver le sélecteur de difficulté selon le mode
        self.difficulty_combo.setEnabled(self.game_mode == "ia")
        self.reset_game()

    def change_difficulty(self, index):
        """0 = aléatoire (Facile), 3 = Moyen, 5 = Difficile."""
        self.difficulty = [0, 3, 5][index]


# ---------------------------------------------------------------------------

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Tictactoe_main()
    window.show()
    app.exec()
