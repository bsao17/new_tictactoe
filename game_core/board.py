import copy as cp


class Board:
    def __init__(self):
        # Initialise the magic_id, the sum of each alignment of four must equal 34
        self.magic_id = [[16, 3, 2, 13],
                         [5, 10, 11, 8],
                         [9, 6, 7, 12],
                         [4, 15, 14, 1]]
        self.board = [[None, None, None, None],
                      ["X", "X", "X", "X"],
                      [None, None, None, None],
                      [None, "O", None, None], ]
        self.x_valid_align = []
        self.o_valid_align = []

    # Align list of valid lists
    def check_valid_alignment(self):
        x_valid_alignement = []
        o_valid_alignement = []
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == "X":
                    self.x_valid_align.append(self.magic_id[row][col])
                elif self.board[row][col] == "O":
                    self.o_valid_align.append(self.magic_id[row][col])
        print(self.x_valid_align)
        print(self.o_valid_align)

    def check_win(self):
        x_win = print("X Winner") if sum(self.x_valid_align) == 34 else print("X Loser")
        o_win = print("O Winner") if sum(self.o_valid_align) == 34 else print("O Loser")

    def children_score(self, player):
        children = []
        if player == "X":
            for i in range(4):
                for j in range(4):
                    if self.board[i][j] == 0:
                        child = Board()
                        child.board = [x[:] for x in self.board]
                        child.board[i][j] = 1
                        children.append(child)
        else:
            for i in range(4):
                for j in range(4):
                    if self.board[i][j] == 0:
                        child = Board()
                        child.board = [x[:] for x in self.board]
                        child.board[i][j] = 2
                        children.append(child)
        return children


if __name__ == '__main__':
    my_board = Board()
    my_board.check_valid_alignment()
    my_board.check_win()
