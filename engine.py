"""
All the function to make and run the tic-tac-toe game
"""

from collections.abc import Callable


def new_board() -> list[list[None]]:
    empty_board = [[None for _ in range(3)] for _ in range(3)]
    return empty_board


def render(board: list[list[str | None]]) -> None:
    # PRINT COL NUMS TO TOP OF BOARD
    print("   0 1 2 ")
    print(" ---------")

    for row in range(3):
        print(f'{row}|', end=" ")
        for col in range(3):
            char: str | None = board[row][col]

            if char is None:
                print(".", end=" ")
            elif char.lower() == "o":
                print("\033[31mO\033[0m", end=" ")
            elif char.lower() == "x":
                print("\033[34mX\033[0m", end=" ")
            else:
                print(".", end=" ")
        print('|')

    print(" ---------")


def make_move(board: list[list[str | None]],
              move_func: Callable[[list[list[str | None]], str],
              tuple[int, int]],
              player_mark: str) -> list[list[str | None]]:

    _board = board.copy()

    move_coords: tuple[int, int] = move_func(_board, player_mark)

    if _board[move_coords[0]][move_coords[1]] is None:
        _board[move_coords[0]][move_coords[1]] = player_mark.upper()

    return _board


def determine_winner(board: list[list[str | None]]) -> str | None:
    winner: str

    lines: list[list[tuple[int, int]]] = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    open_spaces: int = 0

    for line in lines:
        chars: list[str] = []

        for coord in line:
            if board[coord[0]][coord[1]] is None:
                chars.append('')
                open_spaces += 1
            elif isinstance(board[coord[0]][coord[1]], str):
                chars.append(board[coord[0]][coord[1]])  # type: ignore

        if (chars.count(chars[0]) == len(chars)) and (chars[0] != ''):
            winner = chars[0]
            return winner

    if open_spaces == 0:
        return "draw"

    return None


def get_legal_moves(board: list[list[str | None]]) -> list[tuple[int, int]]:
    all_moves: list[tuple[int, int]] = [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2),
    ]

    legal_moves: list[tuple[int, int]] = []

    for move in all_moves:
        row: int = move[0]
        col: int = move[1]

        if board[row][col] is None:
            legal_moves.append((row, col))

    return legal_moves


def get_opponent(current_player: str) -> str:
    current_player = current_player.upper()

    if current_player == 'X':
        return 'O'
    elif current_player == 'O':
        return 'X'
    else:
        raise ValueError('Invalid player')
