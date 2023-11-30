import numpy as np

from game_core.board import Board


def test_board():
    board = Board()
    my_board = np.array([[None, None, None, None],
                         [None, None, None, None],
                         [None, None, None, None],
                         [None, None, None, None]])
    assert np.array_equal(board.board, my_board)


def test_board_check_valid_alignment():
    board = Board()
    assert board.check_valid_alignment() == False


def test_valid_align():
    board = Board()
    board.board = np.array([['x', "x", "x", "x"],
                            [None, None, None, None],
                            [None, None, None, None],
                            [None, None, None, None]])
    assert board.check_valid_alignment() == True
