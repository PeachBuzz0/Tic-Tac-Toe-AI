"""
Script to Hold all the logic for the AI Modes
"""

import random


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

    move: tuple[int, int] = None

    for line in lines:
        chars: list[str] = []

        for coord in line:
            if board[coord[0]][coord[1]] is None:
                chars.append('')
            elif isinstance(board[coord[0]][coord[1]], str):
                chars.append(board[coord[0]][coord[1]])

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

    move: tuple[int, int] = None
    losing_move: tuple[int, int] = None
    winning_move: tuple[int, int] = None

    for line in lines:
        chars: list[str] = []

        for coord in line:
            if board[coord[0]][coord[1]] is None:
                chars.append("")
            elif isinstance(board[coord[0]][coord[1]], str):
                chars.append(board[coord[0]][coord[1]])

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
