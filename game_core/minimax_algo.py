"""Minimax algorithm for Tic-Tac-Toe 'Custom' game."""
import copy as cp


# cells class represent a cell with position in the board, location in the board, max and min value of the cell
class Cells:
    def __init__(self, position, location, max_val, min_val):
        self.position = position
        self.location = location  # NOTE this is a list, [0] is row info and [1] is col info
        self.max_val = max_val
        self.min_val = min_val


def generate_cells(board):
    uboard = cp.deepcopy(board)
    for i in range(len(uboard)):
        for j in range(4):
            if uboard[i][j] == 0:
                uboard[i][j] = Cells(uboard[i][j], (i, j), 0, 0)


def max_value(board, location):
    pass


def min_value(board, location):
    pass


def check_row_align(board, location):
    pass


def check_col_align(board, location):
    pass


def check_diag_align(board, location):
    pass


if __name__ == '__main__':
    generate_cells([[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]])
