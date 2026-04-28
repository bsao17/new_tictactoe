import numpy as np
from itertools import combinations


class Board:
    def __init__(self):
        # Initialise the game board
        self.board = np.array([[None, None, None, None],
                               [None, None, None, None],
                               [None, None, None, None],
                               [None, None, None, None]])

    # ---------- Legacy (kept for compatibility) ----------

    def check_valid_alignment(self):
        """Retourne True si un alignement de 4 existe (ancien mode)."""
        for row in self.board:
            if self._is_full_align(row):
                return True
        for col in self.board.T:
            if self._is_full_align(col):
                return True
        if self._is_full_align(np.diag(self.board)) or \
                self._is_full_align(np.diag(np.fliplr(self.board))):
            return True
        return False

    def _is_full_align(self, line):
        """Alignement complet (toute la ligne, même symbole, sans None)."""
        return None not in line and len(set(line)) == 1

    # ---------- Nouveau mode : score d'alignements de 3 ----------

    def count_alignments_of_3(self, player):
        """
        Compte le nombre d'alignements de exactement 3 cases consécutives
        appartenant à 'player' sur la grille 4x4.

        Une séquence de 3 consécutive dans une ligne/colonne/diagonale de 4
        peut commencer à l'indice 0 ou 1, donc il y a 2 fenêtres par ligne/colonne
        et 1 fenêtre par diagonale principale (de longueur 4).

        Returns:
            int: nombre d'alignements de 3 trouvés pour ce joueur
        """
        count = 0

        # Lignes : 4 lignes × 2 fenêtres de 3 = 8 fenêtres
        for row in self.board:
            count += self._count_windows(row, player)

        # Colonnes : 4 colonnes × 2 fenêtres de 3 = 8 fenêtres
        for col in self.board.T:
            count += self._count_windows(col, player)

        # Diagonales principales (haut-gauche → bas-droite) de longueur 4
        # Diagonale principale
        count += self._count_windows(np.diag(self.board), player)
        # Diagonale anti-principale
        count += self._count_windows(np.diag(np.fliplr(self.board)), player)

        return count

    def _count_windows(self, line, player):
        """
        Compte les fenêtres de taille 3 dans une ligne (tableau numpy 1D)
        où toutes les cases valent 'player'.
        """
        count = 0
        for start in range(len(line) - 2):  # 0 et 1 pour une ligne de 4
            window = line[start:start + 3]
            if all(cell == player for cell in window):
                count += 1
        return count

    def is_full(self):
        """Retourne True si toutes les cases sont remplies."""
        return None not in self.board


if __name__ == '__main__':
    my_board = Board()
    my_board.board[0, 0] = "X"
    my_board.board[0, 1] = "X"
    my_board.board[0, 2] = "X"
    print("Alignements X:", my_board.count_alignments_of_3("X"))  # attendu: 1
    my_board.board[0, 3] = "X"
    print("Alignements X (4 d'affilée):", my_board.count_alignments_of_3("X"))  # attendu: 2
