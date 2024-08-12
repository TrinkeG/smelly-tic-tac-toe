class Tile:
    def __init__(self, x: int, y: int, symbol: str):
        self.x = x
        self.y = y
        self.symbol = symbol


class Board:
    def __init__(self):
        self._plays = [Tile(i, j, " ") for i in range(3) for j in range(3)]

    def tile_at(self, x: int, y: int) -> Tile:
        return next(t for t in self._plays if t.x == x and t.y == y)

    def add_tile_at(self, symbol: str, x: int, y: int) -> None:
        self.tile_at(x, y).symbol = symbol


class TicTacToe:
    def __init__(self):
        self._last_symbol = ' '
        self._board = Board()

    def play(self, symbol: str, x: int, y: int) -> None:
        # If first move
        if self._last_symbol == ' ':
            # If player is O
            if symbol == 'O':
                raise ValueError("Invalid first player")
        # If not first move but player repeated
        elif symbol == self._last_symbol:
            raise ValueError("Invalid next player")
        # If not first move but play on an already played tile
        elif self._board.tile_at(x, y).symbol != ' ':
            raise ValueError("Invalid position")

        # Update game state
        self._last_symbol = symbol
        self._board.add_tile_at(symbol, x, y)

    def winner(self) -> str:
        # Check rows for a winner
        for i in range(3):
            if (self._board.tile_at(i, 0).symbol != ' ' and
                    self._board.tile_at(i, 0).symbol == self._board.tile_at(i, 1).symbol and
                    self._board.tile_at(i, 0).symbol == self._board.tile_at(i, 2).symbol):
                return self._board.tile_at(i, 0).symbol

        # Check columns for a winner
        for i in range(3):
            if (self._board.tile_at(0, i).symbol != ' ' and
                    self._board.tile_at(0, i).symbol == self._board.tile_at(1, i).symbol and
                    self._board.tile_at(0, i).symbol == self._board.tile_at(2, i).symbol):
                return self._board.tile_at(0, i).symbol

        # Check diagonals for a winner
        if (self._board.tile_at(0, 0).symbol != ' ' and
                self._board.tile_at(0, 0).symbol == self._board.tile_at(1, 1).symbol and
                self._board.tile_at(0, 0).symbol == self._board.tile_at(2, 2).symbol):
            return self._board.tile_at(0, 0).symbol

        if (self._board.tile_at(0, 2).symbol != ' ' and
                self._board.tile_at(0, 2).symbol == self._board.tile_at(1, 1).symbol and
                self._board.tile_at(0, 2).symbol == self._board.tile_at(2, 0).symbol):
            return self._board.tile_at(0, 2).symbol

        return ' '
