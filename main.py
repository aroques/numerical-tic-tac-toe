from Board import Board
from Player import Player


def main():
    human_player_first = int(input('Please enter a 1 or 2 to choose to go first or second:'))

    if human_player_first == 1:
        human_player = Player(is_human=1, is_max=1)
        ai_player = Player(is_human=0, is_max=0)
    else:
        human_player = Player(is_human=1, is_max=0)
        ai_player = Player(is_human=0, is_max=1)

    players = [human_player, ai_player]
    max_, min_ = get_max_and_min(players)
    board = Board(4)

    while True:
        max_move = max_.get_move(board)
        board = max_.perform_move(*max_move, board)
        print(board)
        if board.has_winning_sum:
            print('Max wins!')
            break

        min_move = min_.get_move(board)
        board = min_.perform_move(*min_move, board)
        print(board)
        if board.has_winning_sum:
            print('Min wins!')
            break


def get_max_and_min(players):
    for player in players:
        if player.is_max:
            max_ = player
        else:
            min_ = player
    return max_, min_


if __name__ == '__main__':
    main()
