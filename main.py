from random import choice
from Board import Board
from Player import Player


def main():
    human_player = Player()
    ai_player = Player()
    human_player_first = int(input('Please enter a 1 or 2 to choose to go first or second:'))

    if human_player_first == 1:
        human_player.is_max = True
    else:
        human_player.is_max = False

    board = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]

    board = Board(board)

    while True:
        if human_player.is_max:
            print('All moves:')
            print(board.all_odd_moves)
            max_move = get_move_from_user()
            board = human_player.perform_move(max_move, board)
            print(board)
            if board.has_winning_sum:
                print('Max wins!')
                break
            min_move = choice(board.all_even_moves)
            board = ai_player.perform_move(min_move, board)
            print(board)
            if board.has_winning_sum:
                print('Min wins!')
                break
        else:
            max_move = choice(board.all_odd_moves)
            board = ai_player.perform_move(max_move, board)
            print(board)
            if board.has_winning_sum:
                print('Max wins!')
                break
            print('All moves:')
            print(board.all_even_moves)
            min_move = get_move_from_user()
            board = human_player.perform_move(min_move, board)
            print(board)
            if board.has_winning_sum:
                print('Min wins!')
                break


def get_move_from_user(board):
    move = [-1, -1]
    while True:
        move[0] = int(input('Enter move location: '))
        if move[0] not in board.all_possible_move_locations:
            print('Not a valid move location')
        else:
            break
    while True:
        move[1] = int(input('Enter move value: '))
        if move[1] not in board.all_possible_move_values:
            print('Not a valid move value')
        else:
            break
    return move


if __name__ == '__main__':
    main()


