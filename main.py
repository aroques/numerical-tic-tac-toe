from random import choice
from Board import Board


def main():
    # player_first = int(input('Please enter a 1 or 2 to choose to go first or second:'))
    #
    # if player_first == 1:
    #     print('the player is max')
    # else:
    #     print('the player is min')

    board = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]

    board = Board(board)

    while not board.has_winning_sum:
        max_move = choice(board.all_odd_moves)

        min_move = choice(board.all_even_moves)


if __name__ == '__main__':
    main()
