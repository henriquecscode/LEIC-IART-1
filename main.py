from algo import Minimax
from game import Game
from players import Human, AI
from algo import *

if __name__ == "__main__":
    player1 = Human("player1")
    player2 = Human("player2")
    player1 = AI(Minimax(3, heuristic_1), 1)
    player2 = AI(Minimax(3, heuristic_2), -1)
    game = Game(player1, player2)
    game.play_game()
    player1.algorithm.export()
    player2.algorithm.export()