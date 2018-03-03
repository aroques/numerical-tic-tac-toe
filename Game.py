#
#  Adapted from https://github.com/aimacode/aima-python/blob/master/games.py
#


class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""

    @staticmethod
    def actions(state):
        """Return a list of the allowable moves at this point.
        :rtype: list of moves (location, value)
        """
        if state.is_maxes_turn:
            return state.all_odd_moves
        else:
            return state.all_even_moves

    @staticmethod
    def result(state, move):
        """Return the state that results from making a move from a state."""
        location, value = move[0], move[1]
        state.board[location] = value
        return state

    @staticmethod
    def utility(state, player):
        """Return the value of this final state to player."""
        if player == 'MAX':
            return state.utility
        else:
            return -state.utiility

    @staticmethod
    def is_terminal(state):
        """Return True if this is a final state for the game."""
        return state.has_winning_sum

    @staticmethod
    def to_move(state):
        """Return the player whose move it is in this state."""
        if state.is_maxes_turn:
            return 'MAX'
        else:
            return 'MIN'

    @staticmethod
    def display(state):
        """Print or otherwise display the state."""
        print(state)

