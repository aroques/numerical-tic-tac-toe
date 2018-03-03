from random import choice


class Player:
    def __init__(self, is_human, is_max=False):
        self.is_human = is_human
        self.is_max = is_max

    def all_legal_moves(self, board):
        if self.is_max:
            return board.all_odd_moves
        else:
            return board.all_even_moves

    def all_legal_move_locations(self, board):
        if self.is_max:
            return set([move[0] for move in board.all_odd_moves])
        else:
            return set([move[0] for move in board.all_even_moves])

    def all_legal_move_values(self, board):
        if self.is_max:
            return set([move[1] for move in board.all_odd_moves])
        else:
            return set([move[1] for move in board.all_even_moves])

    @staticmethod
    def perform_move(move_location, move_value, board):
        board.board[move_location] = move_value
        return board

    def get_move(self, board):
        if self.is_human:
            return self.get_move_from_user(board)
        else:
            # Call alpha beta cutoff search here
            return choice(self.all_legal_moves(board))

    def get_move_from_user(self, board):
        while True:
            move_location = int(input('Enter move location {}: '.format(self.all_legal_move_locations(board))))
            if move_location not in self.all_legal_move_locations(board):
                print('Not a valid move location')
            else:
                break
        while True:
            move_value = int(input('Enter move value {}: '.format(self.all_legal_move_values(board))))
            if move_value not in self.all_legal_move_values(board):
                print('Not a valid move value')
            else:
                break

        return move_location, move_value

    def print_all_legal_moves(self, board):
        print('All moves:')
        for i, move in enumerate(self.all_legal_moves(board)):
            if i % 5 == 0 and i != 0:
                print()
            print('{} '.format(move), end='')
        print()

