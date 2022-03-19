class Player:
    def __init__(self):
        pass

    def play(self, board):
        return self.get_move(board)

class Human(Player):
    def __init__(self):
        super().__init__()

    def get_move(self, board):
        self.print_move_options()
        move = Human._get_move("What's your move?")
        return move

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

    def print_move_options(self):
        print("1-2-3")
        print("-----")
        print("8-X-4")
        print("-----")
        print("7-6-5")

class AI(Player):

    def __init__(self, algorithm):
        super().__init__()
        self.algorithm = algorithm

    def get_move(self, board):
        move = self.algorithm(board)
        return move