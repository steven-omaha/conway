import numpy as np

THRESHOLD_STAY_ALIVE_MIN = 2
THRESHOLD_STAY_ALIVE_MAX = 3
THRESHOLD_BECOME_ALIVE = 3


def iterate(board: np.ndarray) -> np.ndarray:
    new_board = np.zeros_like(board)

    for row_idx, row in enumerate(board):
        for column_idx, column in enumerate(row):
            alive_neighbors_count = get_alive_neighbors_count(board, row_idx, column_idx)
            if board[row_idx, column_idx] == 1:
                if THRESHOLD_STAY_ALIVE_MIN <= alive_neighbors_count <= THRESHOLD_STAY_ALIVE_MAX:
                    new_board[row_idx, column_idx] = 1
            else:
                if alive_neighbors_count == THRESHOLD_BECOME_ALIVE:
                    new_board[row_idx, column_idx] = 1
    return new_board


def get_alive_neighbors_count(board: np.ndarray, row_idx: int, column_idx: int):
    cell_sum = np.sum(board[max(row_idx - 1, 0):row_idx + 2, max(column_idx - 1, 0):column_idx + 2])
    return cell_sum - board[row_idx, column_idx]
