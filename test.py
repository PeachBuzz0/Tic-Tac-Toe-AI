"""
testing script for certain functions
"""
from main import *
from bot_logic import *


def render_test() -> None: #Passed
    board: list[list] = new_board()
    board[0][1] = "X"
    board[1][1] = "O"

    render(board)


def make_move_test() -> None: #Passed
    board = new_board()

    move_cords_1: tuple[int, int] = (2, 0)
    board = make_move(board, move_cords_1, player_mark="X")
    render(board)

    move_cords_2: tuple[int, int] = (1, 1)
    board = make_move(board, move_cords_2, player_mark="O")
    render(board)


def illegal_move_test() -> None: #Passed
    board = new_board()

    move_coords: tuple[int, int] = (2, 0)
    board = make_move(board, move_coords, player_mark="X")
    board = make_move(board, move_coords, player_mark="O")


def get_winner_test() -> None: # Passed
    board_1 = [["X", "X", "O"],
               ["O", "X", None],
               ["O", "O", "X"]]
    print(get_winner(board_1))

    board_2 = [["X", "X", "O"],
               ["O", None, "X"],
               ["O", "O", "X"]]
    print(get_winner(board_2))

def test_find_winning_moves() -> None:
    board = [
        ['X', 'O', None],
        [None, 'O', None],
        ['X', None, None]
    ]
    print(finds_winning_moves_ai(board, 'X'))
    print(finds_winning_moves_ai(board, 'X'))

    print(finds_winning_moves_ai(board, 'O'))
    print(finds_winning_moves_ai(board, 'O'))


if __name__ == "__main__":
    test_find_winning_moves()
