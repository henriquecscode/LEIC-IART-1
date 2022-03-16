
EMPTY = 0
WHITE = 1
BLACK = 2

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

class Algorithm:

    def __init__(self):
        pass

    def __call__(self, board):
        pass

class Piece:
    def __init__(self, s) -> None:
        self.symbol = s

    def __call__(self):
        return self.symbol

class Empty(Piece):
    def __init__(self) -> None:
        super().__init__(EMPTY)
E = Empty()

class White(Piece):
    def __init__(self) -> None:
        super().__init__(WHITE)
W = White()

class Black(Piece):
    def __init__(self) -> None:
        super().__init__(BLACK)
B = Black()

class Board:
    def __init__(self):
        self.board = self.create_board()

    @staticmethod
    def create_extreme_lines():
        return [E()] + [B() for _ in range(6)] + [E()]
    @staticmethod
    def create_middle_lines():
        return [W()] + [E() for _ in range(6)] + [W()]
    @staticmethod 
    def create_board():
        board = [Board.create_extreme_lines()] \
        + [Board.create_middle_lines() for _ in range(6)] \
        + [Board.create_extreme_lines()]
        return board
    
    def __repr__(self) -> str:
        rep = '\n'
        for line in self.board:
            rep += ' '.join(map(str,line)) + '\n'
            # str += ' '.join(map(str, line))
        return rep

class Game:
    def __init__(self) -> None:
        self.player = W()
        self.board = Board()

    def move_diagonal(self, is_left=True):
        pass

    def move_horizontal(sekf, is_left):
        pass

    def move_vertical(self, is_left):
        pass

if __name__ == "__main__":
    board = Game()
    print(board.__dict__)
