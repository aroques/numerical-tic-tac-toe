from math import sqrt


class Board:
    def __init__(self, board):
        """Pass in a list of numbers that represent the board.
            The length of the board must be a perfect square.
            Zeroes represent empty spaces."""
        self.length = sqrt(len(board))
        if not self.length.is_integer():
            raise ValueError('Board length is not a perfect square!')
        self.board = board
        self.num_columns = self.num_rows = int(self.length)
        all_numbers = range(1, len(board) + 1)
        self.winning_sum = int(sum(all_numbers) / self.length)

    @property
    def has_winning_sum(self):
        winning_sums = [
            self.row_has_winning_sum,
            self.column_has_winning_sum,
            self.diagonal_has_winning_sum
        ]
        return any(winning_sums)

    @property
    def row_has_winning_sum(self):
        for i in range(self.num_columns):
            start_idx = i * self.num_columns
            end_idx = start_idx + self.num_columns
            row = self.board[start_idx:end_idx]
            if sum(row) == self.winning_sum:
                return True
        return False

    @property
    def column_has_winning_sum(self):
        for i in range(self.num_rows):
            column = self.board[i::self.num_rows]
            if sum(column) == self.winning_sum:
                return True
        return False

    @property
    def diagonal_has_winning_sum(self):
        diagonals = []

        top_left_to_bottom_right = self.board[::self.num_columns + 1]
        diagonals.append(top_left_to_bottom_right)

        first_idx_of_last_row = len(self.board) - self.num_columns
        last_idx_of_first_row = self.num_columns - 1
        top_right_to_bottom_left = self.board[last_idx_of_first_row:first_idx_of_last_row + 1:self.num_columns - 1]
        diagonals.append(top_right_to_bottom_left)

        for diagonal in diagonals:
            if sum(diagonal) == self.winning_sum:
                return True
        return False

    @property
    def all_possible_moves(self):
        """Returns all indexes that contain the value zero"""
        return [i for i, val in enumerate(self.board) if val == 0]

    def paint(self):
        for i, val in enumerate(self.board):
            print('{} '.format(val), end='')
            if ((i + 1) % self.num_columns) == 0:
                print()

