# def count_alignments(board, player):
#     count = 0
#     # Check rows, columns, and diagonals for 3-in-a-row
#     # Implementing logic to count alignments and handle deactivated cells
#     for i in range(4):
#         for j in range(4):
#             if board[i][j] == player and (i, j) not in deactivated_cells:
#                 count += 1
#                 if count == 3:
#                     return count
#     return count
#
#
# def minimax(board, depth, is_maximizing, deactivated_cells):
#     # Check for end condition
#     if depth == 0 or all(cell in deactivated_cells for row in board for cell in row):
#         return count_alignments(board, 'O') - count_alignments(board, 'X')
#
#     if is_maximizing:
#         best_score = -float('inf')
#         for i in range(4):
#             for j in range(4):
#                 if board[i][j] == ' ' and (i, j) not in deactivated_cells:
#                     board[i][j] = 'O'
#                     # Update deactivated cells based on new alignment
#                     # TODO: Implement logic to update deactivated cells
#                     score = minimax(board, depth - 1, False, deactivated_cells)
#                     board[i][j] = ' '
#                     best_score = max(score, best_score)
#         return best_score
#     else:
#         best_score = float('inf')
#         for i in range(4):
#             for j in range(4):
#                 if board[i][j] == ' ' and (i, j) not in deactivated_cells:
#                     board[i][j] = 'X'
#                     # TODO: Implement logic to update deactivated cells
#                     score = minimax(board, depth - 1, True, deactivated_cells)
#                     board[i][j] = ' '
#                     best_score = min(score, best_score)
#         return best_score
#
#
# def best_move(board, deactivated_cells):
#     best_score = -float('inf')
#     move = (-1, -1)
#     for i in range(4):
#         for j in range(4):
#             if board[i][j] == ' ' and (i, j) not in deactivated_cells:
#                 board[i][j] = 'O'
#                 # TODO: Implement logic to update deactivated cells
#                 score = minimax(board, depth=4, is_maximizing=False, deactivated_cells=deactivated_cells)
#                 board[i][j] = ' '
#                 if score > best_score:
#                     best_score = score
#                     move = (i, j)
#     return move
#
#
# # Example usage
# board = [[' ', ' ', ' ', ' '],
#          [' ', ' ', ' ', ' '],
#          [' ', ' ', ' ', ' '],
#          [' ', ' ', ' ', ' ']]
# deactivated_cells = []
#
# print("Best move for O:", best_move(board, deactivated_cells))


"""Minimax algorithm for Tic-Tac-Toe 'Custom' game."""

import copy as cp


# cells class represent a cell with position in the board, location in the board, max and min value of the cell
class Cells:
    def __init__(self, position, location, max_val, min_val):
        self.position = position
        self.location = location  # NOTE this is a list, [0] is row info and [1] is col info
        self.max_val = max_val
        self.min_val = min_val

    def check_row_align(self):
        for i in range(4):
            if self.location[i] != 0 and self.location[i]:
                if self.location[i] == self.location[i + 1] == self.location[i + 2]:
                    return True

    def check_col_align(self):
        for i in range(4):
            if self.location[i] != 0:
                if self.location[i] == self.location[i + 4] == self.location[i + 8] == self.location[i + 12]:
                    return True
        return False

    def check_diag_align(self):
        for i in range(4):
            for j in range(4):
                if self.location[i] != 0:
                    if self.location[i] == self.location[i + 5] == self.location[i + 10]:
                        return True
                    elif self.location[i] == self.location[i + 3] == self.location[i + 6]:
                        return True


def generate_cells(board):
    uboard = cp.deepcopy(board)
    for i in range(len(uboard)):
        for j in range(4):
            if uboard[i][j] == 0:
                uboard[i][j] = Cells(uboard[i][j], (i, j), 0, 0)


if __name__ == '__main__':
    generate_cells([[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]])
