from multiprocessing import connection
from board import Board

class Player:
    def __init__(self):
        pass

    def play(self, board):
        return self.get_move(board)

    @staticmethod
    def _get_orientation_direction(move):
        orientation = move%4
        direction = (move-1)//4
        return (orientation, direction)

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_move(self, board):
        print("Please input a valid move", self.name)
        row, col = Human._get_piece(board)
        orientation, direction  = Human._get_orientation_direction()
        return row, col, orientation, direction

    @staticmethod
    def _get_piece(board: Board):
        while True:
            print("What piece to move? row-col")
            print(board)
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
            move = input("What direction to move\n")
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
        print("3-4-2")
        print("-----")
        print("1-X-5")
        print("-----")
        print("6-8-7")

class AI(Player):

    def __init__(self, algorithm = None):
        super().__init__()
        self.algorithm = algorithm

    def get_move(self, board):
        move = self.algorithm(board)
        return move