"""
testing script for certain functions
"""

# flake8: noqa F403, F405

from engine import *
from simple_algorithms import *


def render_test() -> None:  # Passed
    board: list[list] = new_board()
    board[0][1] = "X"
    board[1][1] = "O"

    render(board)


def illegal_move_test() -> None:  # Passed
    board = new_board()

    def test_move(board: list[list[str | None]], current_player: str) -> tuple[int, int]:
        return (2, 0)

    board = make_move(board, test_move, player_mark="X")  # type: ignore
    board = make_move(board, test_move, player_mark="O")  # type: ignore


def determine_winner_test() -> None:  # Passed
    board_1 = [["X", "X", "O"],
               ["O", "X", None],
               ["O", "O", "X"]]

    board_2 = [["X", "X", "O"],
               ["O", None, "X"],
               ["O", "O", "X"]]

    print(determine_winner(board_1))  # type: ignore
    print(determine_winner(board_2))  # type: ignore


def test_find_winning_moves() -> None:  # Passed
    board = [
        ['X', 'O', None],
        [None, 'O', None],
        ['X', None, None]
    ]
    print(finds_winning_moves_ai(board, 'X'))
    print(finds_winning_moves_ai(board, 'X'))

    print(finds_winning_moves_ai(board, 'O'))
    print(finds_winning_moves_ai(board, 'O'))


def test_find_winning_and_losing_moves() -> None:  # Passed
    board = [
        ['X', 'O', None],
        [None, 'O', None],
        ['X', None, None]
    ]

    print(finds_winning_and_losing_moves_ai(board, 'X'))
    print(finds_winning_and_losing_moves_ai(board, 'X'))

    print(finds_winning_and_losing_moves_ai(board, 'O'))
    print(finds_winning_and_losing_moves_ai(board, 'O'))

    board = [
        ['O', 'X', None],
        [None, 'X', None],
        ['O', None, None]
    ]

    print(finds_winning_and_losing_moves_ai(board, 'X'))
    print(finds_winning_and_losing_moves_ai(board, 'X'))

    print(finds_winning_and_losing_moves_ai(board, 'O'))
    print(finds_winning_and_losing_moves_ai(board, 'O'))

    board = [
        ['X', 'O', None],
        [None, 'X', None],
        ['O', None, None]
    ]

    print(finds_winning_and_losing_moves_ai(board, 'X'))
    print(finds_winning_and_losing_moves_ai(board, 'X'))

    print(finds_winning_and_losing_moves_ai(board, 'O'))
    print(finds_winning_and_losing_moves_ai(board, 'O'))

    board = [
        ['X', 'O', None],
        ["X", 'O', None],
        [None, None, None]
    ]

    print(finds_winning_and_losing_moves_ai(board, 'X'))
    print(finds_winning_and_losing_moves_ai(board, 'X'))

    print(finds_winning_and_losing_moves_ai(board, 'O'))
    print(finds_winning_and_losing_moves_ai(board, 'O'))

    board = [
        ["X", "O", "O"],
        [None, "X", None],
        [None, None, None]
    ]

    print(finds_winning_and_losing_moves_ai(board, 'O'))
    print(finds_winning_and_losing_moves_ai(board, 'O'))


if __name__ == "__main__":
    test_find_winning_and_losing_moves()
