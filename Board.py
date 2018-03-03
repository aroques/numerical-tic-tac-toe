from itertools import product, combinations


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
    def rows(self):
        rows = []
        for i in range(self.num_columns):
            start_idx = i * self.num_columns
            end_idx = start_idx + self.num_columns
            rows.append(self.board[start_idx:end_idx])
        return rows

    @property
    def columns(self):
        columns = []
        for i in range(self.num_rows):
            column = self.board[i::self.num_rows]
            columns.append(column)
        return columns

    @property
    def row_has_winning_sum(self):
        for row in self.rows:
            if sum(row) == self.winning_sum:
                return True
        return False

    @property
    def column_has_winning_sum(self):
        for column in self.columns:
            if sum(column) == self.winning_sum:
                return True
        return False

    @property
    def major_diagonal(self):
        return self.board[::self.num_columns + 1]

    @property
    def minor_diagonal(self):
        last_idx_of_first_row = self.num_columns - 1
        first_idx_of_last_row = len(self.board) - self.num_columns
        return self.board[last_idx_of_first_row:first_idx_of_last_row + 1:self.num_columns - 1]

    @property
    def diagonals(self):
        return [self.major_diagonal, self.minor_diagonal]

    @property
    def diagonal_has_winning_sum(self):
        for diagonal in self.diagonals:
            if sum(diagonal) == self.winning_sum:
                return True
        return False

    @property
    def is_maxes_turn(self):
        even = odd = 0
        for val in self.board:
            if val % 2 == 0:
                even += 1
            else:
                odd += 1
        if even == odd:
            return True
        elif odd == 0:
            return True
        else:
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

    @property
    def winning_sums(self):
        return [v for v in combinations(self.all_numbers, self.length) if sum(v) == self.winning_sum]

    @property
    def two_even_two_odd_winning_sums(self):
        return [v for v in self.winning_sums if equal_even_odd(v)]

    @property
    def all_even_all_odd_winning_sums(self):
        return [v for v in self.winning_sums if v not in self.two_even_two_odd_winning_sums]


def equal_even_odd(vector):
    even, odd = count_even_odd(vector)
    if even == odd:
        return True
    else:
        return False


def count_even_odd(vector):
    even_cnt = odd_cnt = 0
    for val in vector:
        if val % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    return even_cnt, odd_cnt