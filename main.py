from Board import Board
# from Player import Player
# from itertools import combinations


def main():
    # human_player_first = int(input('Please enter a 1 or 2 to choose to go first or second:'))
    #
    # if human_player_first == 1:
    #     human_player = Player(is_human=1, is_max=1)
    #     ai_player = Player(is_human=0, is_max=0)
    # else:
    #     human_player = Player(is_human=1, is_max=0)
    #     ai_player = Player(is_human=0, is_max=1)

    # players = [human_player, ai_player]
    # max_, min_ = get_max_and_min(players)

    board = Board(4)

    print(len(board.winning_sums))
    print(len(board.two_even_two_odd_winning_sums))
    print(len(board.all_even_all_odd_winning_sums))

    twoandtwo = []
    for sum_ in board.winning_sums:
        even_count = odd_count = 0
        for num in sum_:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        if even_count == 2 and odd_count == 2:
            twoandtwo.append(sum_)
        else:
            pass
            #print(sum_)

    print('length of 2 and 2 = {}'.format(len(twoandtwo)))


    minimax(board)

    # while True:
    #     max_move = max_.get_move(board)
    #     board = max_.perform_move(*max_move, board)
    #     print(board)
    #     if board.has_winning_sum:
    #         print('Max wins!')
    #         break
    #
    #     min_move = min_.get_move(board)
    #     board = min_.perform_move(*min_move, board)
    #     print(board)
    #     if board.has_winning_sum:
    #         print('Min wins!')
    #         break


def get_max_and_min(players):
    for player in players:
        if player.is_max:
            max_ = player
        else:
            min_ = player
    return max_, min_


def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:  # need function to give all children nodes
            stack.append(neighbor)

    return path


def minimax(board):
    """Returns the utility values for max"""
    vectors = board.diagonals + board.columns + board.rows

    if board.is_maxes_turn:
        for vector in vectors:
            print(vector)

    else:
        pass


    # Defensive moves Rank: 4
    # IF 3 evens on major or minor diagonal or actually anywhere
    #   Put an odd to block the last spot in the diagonal
    #   Rank these moves very high
    # IF 2 odds and 1 even
    #   Put an odd to block the even from winning
    #   Rank these moves equally high

    # Offensive moves Rank: 4
    # IF 3 odds on major or minor diagonal
    #   Put an odd to in last spot in the diagonal to win
    #   Rank these moves very high
    # IF 2 evens and 1 odd
    #   Put an odd to win
    #   Rank these moves equally high

    # IF 1 even Rank: 3
    # Then put an odd that could win


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


if __name__ == '__main__':
    main()
