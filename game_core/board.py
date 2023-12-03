import numpy as np


class Board:
    def __init__(self):
        # Initialise the game board
        self.board = np.array([[None, None, None, None],
                               [None, None, None, None],
                               [None, None, None, None],
                               [None, None, None, None]])

    # Check valid alignement for X or O
    def check_valid_alignment(self):
        # rows check
        for row in self.board:
            if self.is_valid_align(row):
                return True

        # columns check
        for col in self.board.T:  # (numpy method) T -> Transpose or turn the board for rows -> cols and cols -> rows
            if self.is_valid_align(col):
                return True

        # diagonales check
        if self.is_valid_align(np.diag(self.board)) or \
                self.is_valid_align(np.diag(np.fliplr(self.board))):
            return True

        return False


    def is_valid_align(self, line):
        return None not in line and len(set(line)) == 1


    def set_value(self, row, col, value):
        """Set the value ('X' or 'O') at the specified position on the board.

        Args:
            row (int): The row index.
            col (int): The column index.
            value (str): The value to set ('X' or 'O').

        Returns:
            bool: True if the value was set, False if the position is already occupied.
        """
        if self.board[row, col] is None:
            self.board[row, col] = value
            return True
        return False



if __name__ == '__main__':

    my_board = Board()
    print(my_board.check_valid_alignment())


