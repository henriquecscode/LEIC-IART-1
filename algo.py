from operator import is_
from board import Board
from game import Game
from math import inf
from copy import copy
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
        if depth:
            # check this later
            return is_maximizer * self.heuristic(game), None

        moves = game.board.get_viable_moves(game.playing)

        value = -inf
        best_move = None
        for move in moves:
            child = copy(game)
            child.play_move(move[0], move[1], move[2], move[3])
            new_val, _ = -self.negamax(child, depth -1, -b, -a, -is_maximizer)
            if new_val > value:
                best_move = move
                new_val = value
            a = max(a, value)
            if a >= b:
                break # cut off branches (pruning)
        return value, best_move

# heuristics are always viewed from the point of view of player 0
# color variable dictates how that will affect the choosing algorithm
# need to find a way to return a copy of the object, not the same, so we can branch out? 
def heuristic_1(game: Game):
    #number of pieces friendly is good
    #number of pieces enemy is bad
    pass

def heuristic_2(game: Game):
    #number of connections + center + bridges
    #Number of pieces groups - the less number of groups, the better.
    #One could add the expected number of plays needed to connect X groups to the heuristic.
    #Since a group could be a single piece, if we have n groups,
    #the best/minimum number of plays needed to connect them is n - 1.
    pass

def heuristic_3(game: Game):
    #check how many pieces a player captured (12-number of pieces the player has on the board)
    #and how many pieces of theirs got captured by the oponent
    pass

def heuristic_4(game: Game):
    #check if there are possible moves that will result in a capture
    pass

def heuristic_5(game: Game):
    #check how many changes in direction the biggest group / path of pieces has
    #a change in direction is basically a "corner" (it's, like, perpendicular)
    pass
 
def heuristic_6 (game: Game):
    #check how many pieces are in a straight line (opponent pieces that is)
    pass

def heuristic_7(game: Game): #Might not be the best idea
    #Another heuristic: "The Quad Heuristic - https://www.researchgate.net/profile/Jos-Uiterwijk/publication/220174487_The_Quad_Heuristic_in_Lines_of_Action/links/02e7e529a55a472bcc000000/The-Quad-Heuristic-in-Lines-of-Action.pdf?origin=publication_detail"
    pass

