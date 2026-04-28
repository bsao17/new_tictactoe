"""
Nouveau mode de jeu : Score d'alignements de 3
-----------------------------------------------
- La partie se termine quand le plateau est plein (16 cases).
- Chaque joueur marque un point pour chaque séquence de 3 cases
  consécutives identiques (lignes, colonnes, diagonales).
- Une séquence de 4 d'affilée compte pour 2 alignements de 3.
- Celui qui a le plus d'alignements gagne.

L'IA utilise Minimax avec élagage alpha-bêta.
La fonction d'évaluation est :
    score(X) - score(O)  (en nombre d'alignements de 3)
"""

from game_core.board import Board
import numpy as np
import random


# ---------------------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------------------

def get_available_moves(board):
    """Retourne la liste des cases vides (row, col)."""
    moves = []
    for i in range(4):
        for j in range(4):
            if board.board[i, j] is None:
                moves.append((i, j))
    return moves


def is_board_full(board):
    """Retourne True si le plateau est entièrement rempli."""
    return None not in board.board


# ---------------------------------------------------------------------------
# Fonction d'évaluation — différentiel d'alignements de 3
# ---------------------------------------------------------------------------

def evaluate_board(board):
    """
    Calcule le score différentiel :
        alignements_X - alignements_O

    Positif = avantage pour X, négatif = avantage pour O.
    """
    x_score = board.count_alignments_of_3("X")
    o_score = board.count_alignments_of_3("O")
    return x_score - o_score


def count_scores(board):
    """
    Retourne (score_X, score_O) — le nombre d'alignements de 3
    pour chaque joueur sur le plateau courant.
    """
    return board.count_alignments_of_3("X"), board.count_alignments_of_3("O")


# ---------------------------------------------------------------------------
# Ordonnancement des coups (améliore l'élagage alpha-bêta)
# ---------------------------------------------------------------------------

def _ordered_moves(board, maximizing_player):
    """Trie les coups par score immédiat pour maximiser l'élagage alpha-bêta."""
    moves = get_available_moves(board)
    player = "X" if maximizing_player else "O"
    scored = []
    for move in moves:
        new_board = Board()
        new_board.board = board.board.copy()
        new_board.board[move] = player
        scored.append((evaluate_board(new_board), move))
    scored.sort(key=lambda x: x[0], reverse=maximizing_player)
    return [m for _, m in scored]


# ---------------------------------------------------------------------------
# Algorithme Minimax avec élagage alpha-bêta
# ---------------------------------------------------------------------------

def minimax(board, depth, maximizing_player, alpha=-float('inf'), beta=float('inf')):
    """
    Algorithme Minimax (alpha-bêta) pour le morpion 4x4 en mode score.

    Args:
        board:              instance de Board
        depth:              profondeur de recherche restante
        maximizing_player:  True → joue pour X (maximise), False → joue pour O (minimise)
        alpha, beta:        bornes pour l'élagage alpha-bêta

    Returns:
        int: score différentiel (alignements_X - alignements_O)
    """
    if is_board_full(board) or depth == 0:
        return evaluate_board(board)

    available = _ordered_moves(board, maximizing_player)

    if maximizing_player:
        value = -float('inf')
        for move in available:
            new_board = Board()
            new_board.board = board.board.copy()
            new_board.board[move] = "X"
            value = max(value, minimax(new_board, depth - 1, False, alpha, beta))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = float('inf')
        for move in available:
            new_board = Board()
            new_board.board = board.board.copy()
            new_board.board[move] = "O"
            value = min(value, minimax(new_board, depth - 1, True, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


# ---------------------------------------------------------------------------
# Recherche du meilleur coup
# ---------------------------------------------------------------------------

def find_best_move(board, player="X", difficulty=5):
    """
    Trouve le meilleur coup pour le joueur donné.

    Args:
        board:      instance de Board
        player:     "X" ou "O"
        difficulty: 0 = aléatoire (Facile), 3 = Moyen, 5 = Difficile

    Returns:
        Tuple (row, col) du meilleur coup, ou None si aucun coup disponible.
    """
    available = get_available_moves(board)
    if not available:
        return None

    if difficulty == 0:
        return random.choice(available)

    # Limiter la profondeur au nombre de cases restantes (inutile d'aller plus loin)
    depth = min(difficulty, len(available))

    best_value = -float('inf') if player == "X" else float('inf')
    best_move = None

    for move in available:
        new_board = Board()
        new_board.board = board.board.copy()
        new_board.board[move] = player

        if player == "X":
            move_value = minimax(new_board, depth, False)
            if move_value > best_value:
                best_value = move_value
                best_move = move
        else:
            move_value = minimax(new_board, depth, True)
            if move_value < best_value:
                best_value = move_value
                best_move = move

    return best_move


# ---------------------------------------------------------------------------
# Tests rapides
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    b = Board()
    # Ligne 0 : X X X _
    b.board[0, 0] = "X"
    b.board[0, 1] = "X"
    b.board[0, 2] = "X"
    print(f"Score X: {b.count_alignments_of_3('X')}")   # attendu: 1
    print(f"Évaluation: {evaluate_board(b)}")             # attendu: 1

    # Ligne 0 : X X X X  → 2 alignements de 3
    b.board[0, 3] = "X"
    print(f"Score X (4 d'affilée): {b.count_alignments_of_3('X')}")  # attendu: 2

    print(f"Meilleur coup pour O: {find_best_move(b, 'O', difficulty=4)}")
