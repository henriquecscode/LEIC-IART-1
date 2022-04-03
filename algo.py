from operator import is_, ne
import typing as ty
from board import Board
from game import Game
from math import inf
from copy import copy, deepcopy
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

    def __call__(self, game: Game, is_maximizer):
        _, move = self.negamax(game, self.depth, -inf, inf, is_maximizer)
        row, col, new_row, new_col, orientation, direction = move
        return (row, col, orientation, direction)
    
    def negamax(self, game: Game, depth, a, b, is_maximizer): 
        if game.winner != -1:
            if game.winner == 0:
                return is_maximizer * inf, None
            elif game.winner == 1:
                return is_maximizer * -inf, None
        if not depth:
            # check this later
            return is_maximizer * self.heuristic(game), None

        moves = game.board.get_viable_moves(game.playing)

        value = -inf
        best_move = None #moves[0]
        for move in moves:
            child = deepcopy(game)
            child.play_move(move[0], move[1], move[2], move[3])
            new_val, _ = self.negamax(child, depth -1, -b, -a, -is_maximizer)
            new_val = - new_val
            if new_val > value:
                best_move = move
                value = new_val
            a = max(a, value)
            if a >= b:
                break # cut off branches (pruning)
        return value, best_move


PIECES_MULTIPLIER = 1
GROUPS_MULTIPLIER = 5
CAPTURABLE_MULTIPLIER = 5
FOOTPRINT_MULTIPLIER = 2
# heuristics are always viewed from the point of view of player 0
# color variable dictates how that will affect the choosing algorithm
# need to find a way to return a copy of the object, not the same, so we can branch out? 
def heuristic_1(game: Game):
    return PIECES_MULTIPLIER * (len(game.board.players[0]) - len(game.board.players[1]))
    #number of pieces friendly is good
    #number of pieces enemy is bad
    pass

def heuristic_2(game: Game):
    #number of connections + center + bridges
    #Number of pieces groups - the less number of groups, the better.
    #One could add the expected number of plays needed to connect X groups to the heuristic.
    #Since a group could be a single piece, if we have n groups,

    
    player1_groups = game.board.get_connected_groups(0)
    player2_groups = game.board.get_connected_groups(1)
    return GROUPS_MULTIPLIER * (player1_groups[1] - player2_groups[1])

def heuristic_3(game: Game):
    #check if there are possible moves that will result in a capture
    #We can capture the same as we can be captured? I think so

    moves = game.board.get_viable_moves(game.playing)
    n_capturable = len((_ for _, _, new_row, new_col, _, _ in moves if game.board[new_row][new_col] == game.board._player_symbols[not game.playing]))
    n_capturable = n_capturable if game.playing == 0 else - n_capturable
    return CAPTURABLE_MULTIPLIER * n_capturable
 
def heuristic_4(game: Game):
    def calculate_footprint(group: ty.List[tuple(int,int)]):
        footprint = set(group)
        for row, col in group:
            footprint |= {(r, c) for r in range(row-1, row+2) for c in range(col-1, col+2) if game.board._is_different_valid_pos(row, col, r, c)}
        return len(footprint)

    player1_groups = game.board.get_connected_groups(0)
    player2_groups = game.board.get_connected_groups(1)

    groups = [[piece for piece in player1_groups[0] if player1_groups[0][piece] == n_group ] for n_group in range(player1_groups[1])]
    footprint1 = sum(calculate_footprint(group) for group in groups)

    groups = [[piece for piece in player2_groups[1] if player2_groups[1][piece] == n_group] for n_group in range(player2_groups[1])]
    footprint2 = sum(calculate_footprint(group) for group in groups)
    return FOOTPRINT_MULTIPLIER * (footprint1 - footprint2)

