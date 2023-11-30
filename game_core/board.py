import numpy as np


class Board:
    def __init__(self):
        # Initialise the game board
        self.board = np.array([[None, None, None, None],
                               [None, None, None, None],
                               [None, None, None, None],
                               [None, None, None, None]])

        self.move_player = np.array(self.board)

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
