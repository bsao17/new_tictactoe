import numpy as np


class Board:
    def __init__(self):
        # Initialise the game board
        self.board = np.array([["x", "x", "x", "x"],
                               ["o", None, None, None],
                               ["o", None, None, None],
                               ["o", None, None, None]])
        self.row_1 = self.board[0]
        self.row_2 = self.board[1]
        self.row_3 = self.board[2]
        self.row_4 = self.board[3]
        self.col_1 = self.board[:, 0]
        self.col_2 = self.board[:, 1]
        self.col_3 = self.board[:, 2]
        self.col_4 = self.board[:, 3]
        self.diag_1 = np.diag(self.board)
        self.diag_2 = np.diag(np.fliplr(self.board))
        self.diag_3 = np.flip(self.diag_1, 0)
        self.diag_4 = np.flip(self.diag_2, 0)
        self.x_valid_align = []
        self.o_valid_align = []

    # Check valid alignement for X or O
    def check_valid_alignment(self):
        for row in range(1, 5):
            for col in range(1, 5):
                print(f"row: {row}, column: {col}")

    def is_valid_align(self, line):
        if "x" in line:
            return True
        else:
            False


if __name__ == '__main__':
    my_board = Board()
    my_board.check_valid_alignment()
