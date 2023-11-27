import copy as cp


class Board:
    def __init__(self):
        # Initialise the magic_id, the sum of each alignment of four must equal 34
        self.magic_id = [[16, 3, 2, 13],
                         [5, 10, 11, 8],
                         [9, 6, 7, 12],
                         [4, 15, 14, 1]]
        self.board = [[None, None, None, None],
                      [None, None, "X", None],
                      [None, None, None, None],
                      [None, "O", None, None], ]

    # Align list of valid lists
    def check_valid_alignment(self):
        x_valid_alignement = []
        o_valid_alignement = []
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == "X":
                    x_valid_alignement.append(self.magic_id[row][col])
                elif self.board[row][col] == "O":
                    o_valid_alignement.append(self.magic_id[row][col])
        print(x_valid_alignement)
        print(o_valid_alignement)


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
