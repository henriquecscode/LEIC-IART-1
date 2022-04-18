import itertools
from board import Board
from utils import outcolors, _print_board

class Game:
    def __init__(self, player1, player2, config = None) -> None:
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]
        self.config = config
        self.playing = 0
        self.winner = -1

    def play_game(self):
        end_game = -1
        while end_game == -1:
            good_move = False
            while not good_move:
                row, col, orientation, direction = self.players[self.playing].get_move(self)
                print("Played the piece that was in (" + str(row) + ", " + str(col) + ").\n")
                good_move, new_row, new_col = self.board.is_viable_move(self.playing, row, col, orientation, direction)

            end_game = self.play_move(row, col, new_row, new_col)
        print('\033[38;5;135m' + "Winner is", self.players[self.winner].name + '\n') 
        _print_board(self.board)

    def play_move(self, row, col, new_row, new_col):
        if self.winner != -1:
            return self.winner
        self.board._move_piece(row, col, new_row, new_col)
        end_game = self.board.end_game(self.playing)
        self.playing = not self.playing
        if end_game != -1:
            self.winner = end_game
        return end_game

    def move_diagonal(self, is_left=True):
        pass

    def move_horizontal(sekf, is_left):
        pass

    def move_vertical(self, is_left):
        pass