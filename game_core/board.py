import numpy as np


class Board:
    def __init__(self):
        # Initialise the magic_id, the sum of each alignment of four must equal 34
        self.magic_id = np.array([[16, 3, 2, 13],
                                  [5, 10, 11, 8],
                                  [9, 6, 7, 12],
                                  [4, 15, 14, 1]])
        self.board = np.array([[1, None, None, None],
                               [2, None, None, None],
                               [3, None, None, None],
                               [4, None, None, None], ])
        self.row_1 = self.board[: 1, : 4]
        self.row_2 = self.board[1 : 2, 0 : 4]
        self.x_valid_align = []
        self.o_valid_align = []

    # Check valid alignement for X or O
    def check_valid_alignment(self):
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == "X":
                    self.x_valid_align.append(self.magic_id[row][col])
                elif self.board[row][col] == "O":
                    self.o_valid_align.append(self.magic_id[row][col])
        print(self.x_valid_align)
        print(self.o_valid_align)

    def check_win(self):
        pass


if __name__ == '__main__':
    my_board = Board()
    print(my_board.row_2)
