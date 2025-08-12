"""
Script to Hold all the logic for the AI Modes

All move functions(funcs that use an algorithm to determine a move)
    take a board and player as an input and return a move in the
    form of coordinates on the board
"""

import random


class MoveTaken(Exception):
    """
    Exception raised when a move would be illegal
    because it has already been made.
    """

    def __init__(self):
        super().__init__()


def is_valid_move(board: list[list[str | None]],
                  move: tuple[int, int],) -> bool:
    """
    Check if a user inputted move is legal or not.
    """
    try:
        if move[0] < 0 or move[1] < 0:  # Dont let players negative index
            raise IndexError
        elif board[move[0]][move[1]] is None:
            return True
        else:
            raise MoveTaken

    except IndexError:
        error_msg = "Invalid move. Row or Column does not exist."
    except MoveTaken:
        error_msg = f"Invalid move! {move} is already taken, try again."

    print(error_msg)

    return False


def human_player(board: list[list[str | None]],
                 current_player: str) -> tuple[int, int]:
    user_move = input("Enter your move(row col): ")

    split_user_move: list[str] = user_move.split()

    user_coords: tuple[int, int] = (int(split_user_move[0]),
                                    int(split_user_move[1]))

    while True:
        if is_valid_move(board, user_coords):
            break
        else:
            user_coords = human_player(board, current_player)

    return user_coords


def random_ai(board: list[list[str | None]],
              current_player: str) -> tuple[int, int]:
    row: int = random.randint(0, len(board) - 1)
    column: int = random.randint(0, len(board[0]) - 1)

    while board[row][column] is not None:
        row = random.randint(0, len(board) - 1)
        column = random.randint(0, len(board[0]) - 1)

    move: tuple[int, int] = (row, column)

    return move


def finds_winning_moves_ai(board: list[list[str | None]],
                           current_player: str) -> tuple[int, int]:
    """
    Finds a winning move by analysing all possible
    lines to make 3 in a row and checks if any line
    is 3 of the same character, resulting in a win.
    """
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

    move: tuple[int, int] = None  # type: ignore

    for line in lines:
        chars: list[str] = []

        for coord in line:
            if board[coord[0]][coord[1]] is None:
                chars.append('')
            elif isinstance(board[coord[0]][coord[1]], str):
                chars.append(board[coord[0]][coord[1]])  # type: ignore

        if (chars.count(current_player) == 2) and ('' in chars):
            # Determine if blank space is the 1st, 2nd, or 3rd coord in line
            blank_space = chars.index('')

            # line[blank_space] should return the coord par
            move = line[blank_space]

    if move is None:
        move = random_ai(board, current_player)

    return move


def finds_winning_and_losing_moves_ai(board: list[list[str | None]],
                                      current_player: str) -> tuple[int, int]:
    """
    See if the opponent has a wining move, and block it
    If we have a wining move do that instead
    If neither of us have a wining move, do a random move
    """

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
        [(0, 2), (1, 1), (2, 0)],
    ]

    # Determine opponent mark
    opponent_player: str = ''
    if current_player.upper() == 'X':
        opponent_player = "O"
    elif current_player.upper() == "O":
        opponent_player = "X"

    move: tuple[int, int] = None  # type: ignore
    losing_move: tuple[int, int] = None  # type: ignore
    winning_move: tuple[int, int] = None  # type: ignore

    for line in lines:
        chars: list[str] = []

        for coord in line:
            if board[coord[0]][coord[1]] is None:
                chars.append("")
            elif isinstance(board[coord[0]][coord[1]], str):
                chars.append(board[coord[0]][coord[1]])  # type: ignore

        # Find is opponent has a winning move
        if (chars.count(opponent_player) == 2) and ("" in chars):
            blank_space = chars.index("")

            losing_move = line[blank_space]

        # See if we have a winning move
        if (chars.count(current_player) == 2) and ("" in chars):
            # Determine if blank space is the 1st, 2nd, or 3rd coord in line
            blank_space = chars.index("")

            # line[blank_space] should return the coord par
            winning_move = line[blank_space]

    if losing_move is not None:
        move = losing_move

    if winning_move is not None:
        move = winning_move

    if move is None:
        move = random_ai(board, current_player)

    return move
