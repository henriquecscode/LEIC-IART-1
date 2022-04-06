from algo import Minimax
from game import Game
from players import Human, AI
from algo import *
from menu import menu

if __name__ == "__main__":
    # Create for debug parse args
    debug = False
    if debug:
        pass
        """
            player1 = Human("player1")
            player2 = Human("player2")
            player1 = AI(Minimax(3, heuristic_1), 1)
            player2 = AI(Minimax(3, heuristic_2), -1)
        """
    else:
        player1, player2 = menu()

    game = Game(player1, player2)
    game.play_game()

    #Make an if here so only ais do
    player1.algorithm.export()
    player2.algorithm.export()