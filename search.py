#
#  Adapted from https://github.com/aimacode/aima-python/blob/master/games.py
#
import time
from Game import Game
from sys import maxsize
from copy import deepcopy

infinity = float('inf')


class TimeoutReached(Exception):
    pass


def iterative_deepening_alphabeta(state):
    game = Game
    start_time = time.time()
    try:

        for depth in range(0, maxsize):
            best_action = alphabeta_cutoff_search(state, game, start_time, depth)

    except TimeoutReached:
        print('timeout reached')
        print('best action found at depth {}: {}'.format(depth, best_action))
        return best_action


def alphabeta_cutoff_search(state, game, start_time, d=4, reached_cutoff=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""
    player = game.to_move(state)  # will return 'MAX' or 'MIN'

    def max_value(state, alpha, beta, depth):
        if reached_cutoff(state, depth):
            return eval_fn(state)
        elif time.time() - start_time >= 100:
            raise TimeoutReached('Two seconds have passed')
        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if reached_cutoff(state, depth):
            return eval_fn(state)
        elif time.time() - start_time >= 2:
            raise TimeoutReached('Two seconds have passed')
        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    reached_cutoff = (reached_cutoff or
                      (lambda state, depth: depth > d or
                       game.is_terminal(state)))
    eval_fn = eval_fn or (lambda state: game.utility(state, player))
    best_score = -infinity
    beta = infinity
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action
