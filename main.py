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
        3, 0, 4,
        1, 5, 9,
        0, 0, 2
    ]
    # board = [
    #     3, 0, 4, 11,
    #     1, 5, 9, 13,
    #     0, 0, 2, 10,
    #     0, 0, 2
    # ]

    board = Board(board)
    print(board.has_winning_sum)

    # stub_fn(board)


def stub_fn(board):
    possible_moves = []
    for i, num in enumerate(board):
        if num == 0:
            possible_moves.append(i)
    for move in possible_moves:
        print(move)


if __name__ == '__main__':
    main()
