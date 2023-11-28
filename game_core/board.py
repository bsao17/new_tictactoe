import numpy as np


class Board:
    def __init__(self):
        # Initialise the magic_id, the sum of each alignment of four must equal 34
        self.magic_id = np.array([[16, 3, 2, 13],
                                  [5, 10, 11, 8],
                                  [9, 6, 7, 12],
                                  [4, 15, 14, 1]])
        self.board = np.array([[1, None, None, 2],
                               [None, None, None, None],
                               [None, None, None, None],
                               [3, None, None, 4]])
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
        print(self.x_valid_align)
        print(self.o_valid_align)

    def check_win(self):
        pass


if __name__ == '__main__':
    my_board = Board()
    print("row 1", my_board.row_1)
    print("row 2", my_board.row_2)
    print("row 3", my_board.row_3)
    print("row 3", my_board.row_4)
    print("col 1", my_board.col_1)
    print("col 2", my_board.col_2)
    print("col 3", my_board.col_3)
    print("col 4", my_board.col_4)
    print("diag 1 ", my_board.diag_1)
    print("diag 2 ", my_board.diag_2)
    print("diag 3 ", my_board.diag_3)
    print("diag 4 ", my_board.diag_4)
