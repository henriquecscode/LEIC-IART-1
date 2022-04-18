from algo import Algorithm
from board import Board
from game import Game
from utils import outcolors, _print_board
    
class Player:
    def __init__(self, name):
        self.name = name

    def play(self, board):
        return self.get_move(board)

    @staticmethod
    def _get_orientation_direction(move):
        orientation = move%4
        direction = (move-1)//4
        return (orientation, direction)

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, game: Game):
        row, col = Human._get_piece(game)
        orientation, direction  = Human._get_orientation_direction()
        return row, col, orientation, direction

    @staticmethod
    def _get_piece(game: Game):
        board = game.board
        while True:
            print()
            _print_board(board)
            print(outcolors.INPUT_TEXT + "\nWhat piece to move (row col)? " + outcolors.NORMAL)
            move = input()
            list = move.strip().split(' ')
            row = list[0]
            col = list[1]
            if row.isdigit() and col.isdigit():
                row = int(row)
                col = int(col)
                if 0 <= row < board.n  and 0 <= col < board.n:
                    return (row, col)

    @staticmethod
    def _get_orientation_direction():
        while True:
            Human.print_move_options()
            move = input(outcolors.INPUT_TEXT + "What direction to move: " + outcolors.NORMAL)
            if move.isdigit():
                move = int(move)
                if 1 <= move <= 8:
                    return Player._get_orientation_direction(move)

    @staticmethod
    def _get_move(prompt):
        # https://gist.github.com/cglosser/6893097
        valid = False
        while not (valid and 1 < move < 8):
            move = input(prompt)   
            valid = move.isdigit()
            if valid:
                move = int(move)
        return move

    @staticmethod
    def print_move_options():
        print(outcolors.INPUT_TEXT + "3-4-2")
        print("-----")
        print("1-X-5")
        print("-----")
        print("6-8-7")

class AI(Player):
    def __init__(self, algorithm: Algorithm = None, is_maximizer = 1, name: str = None):        
        name = name if name else algorithm.__class__.__name__ + ' ' + algorithm.heuristic.__name__
        super().__init__(name)
        self.algorithm = algorithm
        self.maximizer = is_maximizer

    def get_move(self, game: Game):
        if(game.playing):
           print(outcolors.INPUT_TEXT + "NOW PLAYING: 1" + outcolors.NORMAL + '\n')
        else:
            print(outcolors.INPUT_TEXT + "NOW PLAYING: 0" + outcolors.NORMAL + '\n')
        _print_board(game.board)
        move = self.algorithm(game, self.maximizer)
        return move