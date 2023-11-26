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


def minimax(board, depth, maximizing_player):
    if depth == 0 or board.valid_alignment():
        return board.evaluate()
    if maximizing_player:
        value = -float('inf')
        for child in board.children("X"):
            value = max(value, minimax(child, depth - 1, False))
        return value
    else:
        value = float('inf')
        for child in board.children("O"):
            value = min(value, minimax(child, depth - 1, True))
        return value


def board_evaluation(board):
    pass


if __name__ == '__main__':
    pass
