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
