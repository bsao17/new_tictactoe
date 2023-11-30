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

        self.move_player = np.array(self.board)

        self.valid_align_list = [
            self.row_1,
            self.row_2,
            self.row_3,
            self.row_4,
            self.col_1,
            self.col_2,
            self.col_3,
            self.col_4,
            self.diag_1,
            self.diag_2,
            self.diag_3,
            self.diag_4,
        ]

        self.x_valid_align = []
        self.o_valid_align = []

    # Check valid alignement for X or O
    def check_valid_alignment(self):
        # rows check
        for row in self.board:
            if self.is_valid_align(row):
                return True

        # columns check
        for col in self.board.T:  # (numpy method) T -> Transpose or turn the board for rows to cols and cols to rows
            if self.is_valid_align(col):
                return True

        # diagonales check
        if self.is_valid_align(np.diag(self.board)) or \
                self.is_valid_align(np.diag(np.fliplr(self.board))):
            return True

        return False

    def is_valid_align(self, line):
        return None not in line and len(set(line)) == 1


if __name__ == '__main__':
    my_board = Board()
    print(my_board.check_valid_alignment())
