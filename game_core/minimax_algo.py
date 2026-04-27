"""
---pseudocode minimax algorithm for tic-tac-toe game---

function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
    return value
"""

from game_core.board import Board
import numpy as np


def get_available_moves(board):
    """Retourne les positions vides sur le plateau."""
    moves = []
    for i in range(4):
        for j in range(4):
            if board.board[i, j] is None:
                moves.append((i, j))
    return moves


def evaluate_board(board):
    """
    Évalue le plateau.
    Retourne 10 si X gagne, -10 si O gagne, 0 sinon.
    """
    # Vérifier les lignes
    for row in board.board:
        if row[0] is not None and len(set(row)) == 1:
            return 10 if row[0] == "X" else -10
    
    # Vérifier les colonnes
    for col in board.board.T:
        if col[0] is not None and len(set(col)) == 1:
            return 10 if col[0] == "X" else -10
    
    # Vérifier les diagonales
    diag = np.diag(board.board)
    if diag[0] is not None and len(set(diag)) == 1:
        return 10 if diag[0] == "X" else -10
    
    diag2 = np.diag(np.fliplr(board.board))
    if diag2[0] is not None and len(set(diag2)) == 1:
        return 10 if diag2[0] == "X" else -10
    
    return 0


def is_board_full(board):
    """Vérifie si le plateau est plein."""
    return None not in board.board


def minimax(board, depth, maximizing_player):
    """
    Algorithme minimax pour le morpion 4x4.
    
    Args:
        board: instance de Board
        depth: profondeur de recherche
        maximizing_player: True pour X (joueur max), False pour O (joueur min)
    
    Returns:
        Score de la position
    """
    score = evaluate_board(board)
    
    # Cas terminal : victoire ou profondeur nulle
    if score != 0 or depth == 0 or is_board_full(board):
        return score
    
    if maximizing_player:
        value = -float('inf')
        for move in get_available_moves(board):
            new_board = Board()
            new_board.board = board.board.copy()
            new_board.board[move] = "X"
            value = max(value, minimax(new_board, depth - 1, False))
        return value
    else:
        value = float('inf')
        for move in get_available_moves(board):
            new_board = Board()
            new_board.board = board.board.copy()
            new_board.board[move] = "O"
            value = min(value, minimax(new_board, depth - 1, True))
        return value


def find_best_move(board, player="X", difficulty=3):
    """
    Trouve le meilleur coup pour le joueur actuel.
    
    Args:
        board: instance de Board
        player: "X" ou "O"
        difficulty: profondeur de recherche (1=facile, 2=moyen, 3=difficile)
    
    Returns:
        Tuple (row, col) du meilleur coup
    """
    best_value = -float('inf') if player == "X" else float('inf')
    best_move = None
    
    for move in get_available_moves(board):
        new_board = Board()
        new_board.board = board.board.copy()
        new_board.board[move] = player
        
        if player == "X":
            move_value = minimax(new_board, difficulty, False)
            if move_value > best_value:
                best_value = move_value
                best_move = move
        else:
            move_value = minimax(new_board, difficulty, True)
            if move_value < best_value:
                best_value = move_value
                best_move = move
    
    return best_move


if __name__ == '__main__':
    # Test
    b = Board()
    b.board[0, 0] = "X"
    b.board[1, 1] = "X"
    b.board[2, 2] = "X"
    print(f"Évaluation: {evaluate_board(b)}")
    print(f"Meilleur coup pour X: {find_best_move(b, 'X')}")
