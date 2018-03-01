def main():
    print("hello world!")

    # 15 is a win

    board = [
        3, 0, 4,
        1, 5, 9,
        0, 0, 2
    ]

    is_win(board)


def is_win(board):
    print(board)
    num_columns = 3
    num_rows = 3
    winning_sum = 15

    # check rows
    for i in range(num_columns):
        start_idx = i * num_columns
        end_idx = start_idx + num_columns
        row = board[start_idx:end_idx]
        if sum(row) == winning_sum:
            return True

    # check columns
    for i in range(num_rows):
        column = board[i::num_rows]
        if sum(column) == winning_sum:
            return True

    # check diagonals
    diagonals = []

    top_left_to_bottom_right = board[::num_columns + 1]
    diagonals.append(top_left_to_bottom_right)

    first_idx_of_last_row = len(board) - num_columns
    last_idx_of_first_row = num_columns - 1
    top_right_to_bottom_left = board[last_idx_of_first_row:first_idx_of_last_row + 1:num_columns - 1]
    diagonals.append(top_right_to_bottom_left)

    for diagonal in diagonals:
        if sum(diagonal) == 15:
            return True


if __name__ == '__main__':
    main()
