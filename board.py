EMPTY = 0
WHITE = 2
BLACK = 1

# TODO Make so player1 and player2 are dicts so O(1) in search. The value can be the moving values (number of pieces in the lines)
# Each movement will therefore update the values for every piece so taht the AI can just look up instead of having to calculate for each
# Piece{ coord: (int, int), no_in_same_horizontal: int, no_in_same_vertical: int, no_in_b13_dia: int, no_in_b24_dia: int}
# Each player is a list of their pieces
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
    n = 8
    _player_1_symbol = B()
    _player_2_symbol = W()
    _player_symbols = [_player_1_symbol, _player_2_symbol]

    def __init__(self):
        self.board = self.create_board()
        self.players = {0: self.get_player_pieces(
            0), 1: self.get_player_pieces(1)}

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

    def __getitem__(self, index):
        return self.board[index]

    def __repr__(self) -> str:
        rep = '\n'
        for line in self.board:
            rep += ' '.join(map(str, line)) + '\n'
            # str += ' '.join(map(str, line))
        return rep

    def _count_line(self, line):
        return len([x for x in line if x != E()])
        # return len(list(filter(lambda x: x != E(), line)))

    def get_horizontal_n_pieces(self, row, col):
        line = self.board[row]
        return self._count_line(line)

    def get_vertical_n_pieces(self, row, col):
        line = [x[col] for x in self.board]
        return self._count_line(line)

    def get_b24_diagonal_n_pieces(self, row, col):
        # Left to right
        line = [self.board[i][col-row+i]
                for i in range(self.n) if 0 <= (col - row + i) < self.n]
        return self._count_line(line)

    def get_b13_diagonal_n_pieces(self, row, col):
        # Right to left
        line = [self.board[i][col+row-i]
                for i in range(self.n) if 0 <= (col+row-i) < self.n]
        return self._count_line(line)

    def get_player_pieces(self, player):
        return [(row, col) for row in range(self.n) for col in range(self.n) if self.board[row][col] == self._player_symbols[player]]

    def _update_move(self):
        for i in range(2):
            self.players[i] = self.get_player_pieces(i)

    def end_game(self, playing):
        """
        
        Returns
        -----
        -1 No end game
        0 or 1 Player that wins
        """

        # Both can be affected by a play
        capture_ending = False
        group_ending = False
        end1 = self._no_pieces(0)
        end2 = self._no_pieces(1)

        if end1 or end2:
            capture_ending = True

        # Only the one of the player that played can be affected (towards better)
        conn1 = self._connected(0)
        conn2 = self._connected(1)

        if conn1 or conn2:
            group_ending = True

        if group_ending and not capture_ending:
            return playing
        elif group_ending and capture_ending:
            return not playing
        else:
            return -1

    def _no_pieces(self, player):
        return len(self.players[player]) == 1

    def _connected(self, player):
        if len(self.players[player]) == 1:
            return True

        else:
            return self._calculate_connected(player)

    def _calculate_connected(self, player):
        # Hard stuff
        pieces = self.players[player]
        n_pieces = len(pieces)

        if n_pieces == 0:
            raise Exception

        cur_n_pieces = 1
        states = {pieces[0]}
        queue = [pieces[0]]
        while queue:
            row, col = queue[0]
            queue.pop(0)
        # while cur_n_pieces < n_pieces:
            neighbours = self._get_neighbours(row, col)
            for neigh in neighbours:
                if neigh not in states:
                    states.add(neigh)
                    queue.append(neigh)
                    cur_n_pieces += 1

        if cur_n_pieces == n_pieces:
            return True
        elif cur_n_pieces < n_pieces:
            return False
        else:
            raise Exception

    def get_connected_groups(self, player):
        """
        Returns
        -----
        found: dict([row,col]: number_of_group)
            A dictionary with the pieces and the group they belong to
        no_groups: int
            The number of groups
        """
        pieces = self.players[player]
        n_pieces = len(pieces)
        not_found = set(pieces)
        found = dict()
        no_groups = 0

        while not_found:
            # Shouldn't need a `states` variable per group. Found does that job too
            cur = not_found.pop()
            found[cur] = no_groups
            queue = {cur}
            while queue:
                row,col = queue.pop()
                neighbours = self._get_neighbours(row, col)
                for neigh in neighbours:
                    if neigh not in found:
                        found[neigh] = no_groups
                        # queue.add(neigh)
                        not_found.remove(neigh)
            no_groups += 1

        return found, no_groups

    def _get_neighbours(self, row, col):
        return [(r, c) for r in range(row-1, row+2) for c in range(col-1, col+2) if self._is_different_valid_pos(row, col, r, c) and self.board[row][col] == self.board[r][c]]

    def _is_different_valid_pos(self, row, col, new_row, new_col):
        return 0 <= new_row < self.n and 0 <= new_col < self.n and (row, col) != (new_row, new_col)

    def play_piece(self, player, row, col, orientation, direction):
        """
        Parameters
        -----
        player: int
        orientation: int
            0 vertical
            1 horizontal
            2 diagonal 13
            3 diagonal 24
        direction: int
            0 if to top or left, 1 if to bottom or right
        """

        is_viable, new_row, new_col = self.is_viable_move(
            player, row, col, orientation, direction)
        if not is_viable:
            return is_viable

        self._move_piece(row, col, new_row, new_col)
        return True

    def is_viable_move(self, player, row, col, orientation, direction):
        """
        Parameters
        -----
        player: int
        orientation: int
            0 vertical
            1 horizontal
            2 diagonal 13
            3 diagonal 24
        direction: int
            0 if to top or left, 1 if to bottom or right
        """
        s = self._player_symbols[player]
        if self.board[row][col] != s:
            return False, None, None

        if orientation == 0:
            no_moves = self.get_vertical_n_pieces(row, col)
        elif orientation == 1:
            no_moves = self.get_horizontal_n_pieces(row, col)
        elif orientation == 2:
            no_moves = self.get_b13_diagonal_n_pieces(row, col)
        elif orientation == 3:
            no_moves = self.get_b24_diagonal_n_pieces(row, col)
        else:
            raise Exception
        

        vector = self._get_line_vector(orientation, direction)
        new_row, new_col = row, col
        
        while no_moves:

            blocking = self._is_opponent_blocking(s, new_row, new_col)
            if blocking:
                return False, None, None

            new_row += vector[0]
            new_col += vector[1]

            if not 0 <= new_row < self.n or not 0 <= new_col < self.n:
                # Too many pieces in the direction will go out of bounds
                return False, None, None

            no_moves -= 1

        if self.board[new_row][new_col] == self._player_symbols[player]:
            #Friendly piece already there
            return False, None, None

        return True, new_row, new_col

    def _get_line_vector(self, orientation, direction):
        """
        Parameters
        -----
        orientation: int
            0 vertical
            1 horizontal
            2 diagonal 13
            3 diagonal 24
        direction: int
            0 if to top or left, 1 if to bottom or right
        """
        if orientation == 0:
            vector = (1, 0)
        elif orientation == 1:
            vector = (0, 1)
        elif orientation == 2:
            vector = (1, -1)
        elif orientation == 3:
            vector = (1, 1)
        else:
            raise Exception

        if direction == 0:
            vector = tuple(-x for x in vector)
        elif direction == 1:
            pass
        else:
            raise Exception

        return vector

    def _is_opponent_blocking(self, s, row, col):
        """
        Verifies every piece (including start) but for the last one
        If the last is of the opponent doesn't matter
        If any of the intermediary is different, then it must not be the least
        """
        new_s = self.board[row][col]
        if new_s != E() and new_s != s:
            return True
        return False

    def _move_piece(self, row, col, new_row, new_col):
        s = self.board[row][col]
        self.board[row][col] = E()
        self.board[new_row][new_col] = s

        self._update_move()

    def get_viable_moves(self, player):
        moves = []
        for row, col in self.players[player]:
            for orientation in range(4):
                for direction in range(2):
                    is_viable, new_row, new_col = self.is_viable_move(player, row, col, orientation, direction)
                    if is_viable:
                        moves.append([row, col, new_row, new_col, orientation, direction])

        return moves