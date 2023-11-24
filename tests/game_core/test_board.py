from game_core.board import Board


def test_board():
    board = Board()
    assert board.board == [[0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0]]
