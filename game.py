from board import Board, W
from players import Player, Human, AI

class Game:
    def __init__(self, is_ai1: bool = False, is_ai2: bool = False, config = None) -> None:
        self.board = Board()
        self.player1 = AI() if is_ai1 else Human()
        self.player2 = AI() if is_ai2 else Human()
        self.players = [self.player1, self.player2]
        self.config = config
        self.playing = 0

    def play_game(self):
        end_game = False
        good_move = False
        while not end_game:
            while not good_move:
                row, col, orientation, direction = self.players[self.playing].get_move(self.board)
                good_move = self.board.play_piece(self.playing, row, col, orientation, direction)

            end_game = self.board.end_game() #We need to take account the player here later
            #Maybe return a list of the game winning scenarios and act accordingly

        

    

    def move_diagonal(self, is_left=True):
        pass

    def move_horizontal(sekf, is_left):
        pass

    def move_vertical(self, is_left):
        pass