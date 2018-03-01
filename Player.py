class Player:
    def __init__(self):
        pass

    @staticmethod
    def perform_move(self, move, board):
        board[move[0]] = move[1]
        return board
