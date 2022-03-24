from game import Game
from players import Human

if __name__ == "__main__":
    player1 = Human("player1")
    player2 = Human("player2")
    game = Game(player1, player2)
    game.play_game()