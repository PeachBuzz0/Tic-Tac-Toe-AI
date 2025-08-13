"""
Tic Tac Toe AI
Created by: Gabe(Peach)
Created on: Aug 1, 2025 01:30 AM
"""

# flake8: noqa F403, F405

import sys

from engine import *
from simple_algorithms import *
from minimax import minimax_ai
from sly_minimax import sly_minimax_ai

if __name__ == "__main__":
    # Dictionary to store player info
    # "Player mark" : [move function/algorithm, name]
    players: dict[str, list[str]] = {
        "O": ['...', 'Player 1'],
        "X": ["...", 'Player 2']
    }

    # Get move function
    move_funcs: list[str] = sys.argv[1:]

    if not move_funcs:
        move_funcs = ['human_player', "human_player"]

    # Test if move algorithm exist
    class AINotFound(Exception):
        """
        Descriptive error for when a move algorithm/AI is not defined
        """

        def __init__(self):
            super().__init__("AI not found. Make sure to "
                             "import the algorithm in main.py, "
                             "\nand function name is spelled correctly")

    for i, func in enumerate(move_funcs):
        if func in dir():
            pass
        else:
            raise AINotFound

        # Get players name if they are a Human Player
        if i == 0:
            player_mark = "O"
        else:
            player_mark = "X"

        if func == "human_player":
            inputted_name: str = input(f"Enter name for "
                                       f"{players[player_mark][1]}: ")

            players[player_mark][1] = inputted_name

        players['O'][0] = move_funcs[0]
        players['X'][0] = move_funcs[1]

    board: list[list[str | None]] = new_board()  # type: ignore

    turn: int = 1

    while True:
        render(board)

        winner: str | None = determine_winner(board)

        if determine_winner(board) is not None:
            break

        player: str
        if (turn % 2) == 0:
            player = 'X'
        else:
            player = 'O'

        # Make sure move function is imported into main
        move_func = getattr(sys.modules[__name__], players[player][0])

        make_move(board, move_func, player)

        turn += 1

    assert isinstance(winner, str)

    if winner.lower() == 'draw':
        print("Draw! Maybe play again.")
    else:
        player_name: str = players[winner][1]
        player_algorithm: str = players[winner][0]
        print(f'{player_name}({player_algorithm}) wins!')
