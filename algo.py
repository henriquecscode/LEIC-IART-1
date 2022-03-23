from board import Board
from game import Game
from math import inf
class Algorithm:

    def __init__(self):
        pass

    def __call__(self, board):
        """
        move (row, col, new_row, new_col, orientation, direction)
        return move
        pass
        """

class Minimax(Algorithm):

    def __init__(self, depth, heuristic):
        super().__init__()
        self.depth = depth
        self.heuristic = heuristic

    def __call__(self, board):
        pass
    
    def negamax(self, game: Game, depth, a, b, color):
        if depth == 0 or game.board.end_game():
            # check this later
            return color * self.heuristic(game)

        child_nodes = game.board.get_viable_moves(game.playing)

        value = -inf
        for child in child_nodes:
            value = max(value, -self.negamax(child, depth -1, -b, -a, -color))
            a = max(a, value)
            if a >= b:
                break # cut off branches (pruning)
        return value
