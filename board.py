EMPTY = 0
WHITE = 1
BLACK = 2


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
        self.n = 8
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

    def _count_line(line):
        return len(x != E() for x in line)
    def get_horizontal_n_pieces(self, row, col):
        line = self.board[row]
        return self._count_line(line)

    def get_vertical_n_pieces(self, row, col):
        line = [x[col] for x in self.board]
        return self._count_line(line)

    def get_b24_diagonal_n_pieces(self, row, col):
        # Left to right
        line = [x[col-row+i] for i,x in self.board.enumerate() if 0 <= col - row + i < self.n] 
        return self._count_line(line)

    def get_b13_diagonal_n_pieces(self, row, col):
        # Right to left
        line = [x[col+row-i] for i,x in self.board.enumerate() if 0 <= col - row + i < self.n] 
        return self._count_line(line)
