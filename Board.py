from math import sqrt
from itertools import product


class Board:
    def __init__(self, length=4):
        """Pass in a list of numbers that represent the board.
            The length of the board must be a perfect square.
            Zeroes represent empty spaces."""
        self.length = length
        self.board = [0 for _ in range(pow(self.length, 2))]
        self.num_columns = self.num_rows = int(self.length)
        self.all_numbers = range(1, len(self.board) + 1)
        self.winning_sum = int(sum(self.all_numbers) / self.length)
        print(self.winning_sum)

    def __str__(self):
        out = ''
        for i, val in enumerate(self.board):
            out += '{} '.format(val)
            if ((i + 1) % self.num_columns) == 0:
                out += '\n'
        return out

    @property
    def has_winning_sum(self):
        """Returns True if the values of a row, column or diagonal sum to the winning sum value"""
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
    def all_possible_move_locations(self):
        """Returns all indexes that contain the value zero"""
        return [i for i, val in enumerate(self.board) if val == 0]

    @property
    def all_possible_move_values(self):
        """Returns all possible values that can be placed on the board"""
        used_values = [val for val in self.board if val != 0]
        return [val for val in self.all_numbers if val not in used_values]

    @property
    def all_possible_moves(self):
        """Returns all possible moves. A move is a tuple. The move[0] is the location
            (index) of the move and move[1] is the value."""
        return product(self.all_possible_move_locations, self.all_possible_move_values)

    @property
    def all_odd_moves(self):
        """Returns all possible odd moves. A move is a tuple. The move[0] is the location
            (index) of the move and move[1] is the value."""
        return [move for move in self.all_possible_moves if move[1] % 2 == 1]

    @property
    def all_even_moves(self):
        """Returns all possible even moves. A move is a tuple. The move[0] is the location
            (index) of the move and move[1] is the value."""
        return [move for move in self.all_possible_moves if move[1] % 2 == 0]

