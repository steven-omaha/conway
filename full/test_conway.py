from conway import iterate
import numpy as np
import pytest


def test_dead_cell_stays_dead():
    board = np.array([[0]])
    assert_boards_equal(board, iterate(board))


def test_two_dead_cell_stay_dead():
    board = np.array([[0, 0]])
    assert_boards_equal(board, iterate(board))


def test_living_cell_dies():
    board = np.array([[1]])
    assert_boards_equal(iterate(board), np.array([[0]]))


def test_two_living_cells_die():
    board = np.array([[1, 1]])
    assert_boards_equal(iterate(board), np.array([[0, 0]]))


def test_two_living_cells_die_in_column():
    board = np.array([[1], [1]])
    assert_boards_equal(iterate(board), np.array([[0], [0]]))


def test_three_living_cells_in_a_row():
    board = np.array([[1, 1, 1]])
    assert_boards_equal(iterate(board), np.array([[0, 1, 0]]))


def test_three_living_cells_in_a_column():
    board = np.array([[1], [1], [1]])
    assert_boards_equal(iterate(board), np.array([[0], [1], [0]]))


@pytest.mark.parametrize("in_board, out_board", [
    (np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])),
    (np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]), np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])),
    (np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])),
    (np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]])),
    (np.array([[1, 1, 1], [0, 1, 0], [0, 0, 0]]), np.array([[1, 1, 1], [1, 1, 1], [0, 0, 0]])),
], ids=[
    "all empty",
    "blinker 1",
    "blinker 2",
    "cells die of overpopulation",
    "cell with three neighbors stays alive",
])
def test_three_by_three_board(in_board, out_board):
    assert_boards_equal(iterate(in_board), out_board)


def assert_boards_equal(in_board: np.ndarray, out_board: np.ndarray):
    assert in_board.shape == out_board.shape, "shapes are not equal"

    for row_idx, row in enumerate(in_board):
        for column_idx, column in enumerate(row):
            assert in_board[row_idx, column_idx] == out_board[
                row_idx, column_idx], f"Expected '{out_board[row_idx, column_idx]}' at {row_idx, column_idx}. Got: {in_board[row_idx, column_idx]}"
