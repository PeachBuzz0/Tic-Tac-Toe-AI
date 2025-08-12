"""
Script to hold all the functionality
for minimax algorithm
"""

from copy import deepcopy
from engine import determine_winner, get_opponent, get_legal_moves


def _test_move(board: list[list[str | None]],
               move: tuple[int, int],
               current_player: str) -> list[list[str | None]]:

    _board: list[list[str | None]] = board.copy()

    _board[move[0]][move[1]] = current_player.upper()

    return _board


def _minimax_score(board: list[list[str | None]],
                   current_player: str,
                   player_we_want_to_win: str,
                   branch: int = 0) -> float:
    """
    Use the minimax algorithm score next move.
    Score is a float between -10 and 10.
    A tenth of a point is taken off per branch,
    which represents the amount of moves to get
    to that move.
    """

    # If board is a terminal state, immediately
    # Return the appropriate score

    if determine_winner(board) == player_we_want_to_win:
        return 10
    elif determine_winner(board) == get_opponent(player_we_want_to_win):
        return -10
    elif determine_winner(board) == 'draw':
        return 0

    # If board is not a terminal state
    # get all moves that could be played
    legal_moves: list[tuple[int, int]] = get_legal_moves(board)

    # Iterate over moves, calculating a score for them
    # Keep all the scores in a list
    scores: list[float] = []

    for move in legal_moves:
        _board: list[list[str | None]] = deepcopy(board)

        # First make the move
        _board = _test_move(_board, move, current_player)

        # Then get minimax score for the resulting
        # board state, passing in 'current_player''s
        # opponents because it would be their turn

        opponent: str = get_opponent(current_player)
        score: float = _minimax_score(_board, opponent,
                                      player_we_want_to_win,
                                      branch + 1)
        scores.append(score - (branch * 0.1))

    # If current_player is our AI,
    # then we want maximized score
    if current_player == player_we_want_to_win:
        return max(scores)

    # If current_player is our opponent,
    # then we want to minimize score
    else:
        return min(scores)


def minimax_ai(board: list[list[str | None]],
               current_player: str) -> tuple[int, int]:
    best_score: float = -1000.0
    best_move: tuple[int, int] = (-1, -1)

    legal_moves: list[tuple[int, int]] = get_legal_moves(board)

    for move in legal_moves:
        _board: list[list[str | None]] = deepcopy(board)
        _board = _test_move(_board, move, current_player)

        move_score: float = _minimax_score(_board,
                                           get_opponent(current_player),
                                           current_player)

        if move_score >= best_score:
            best_score = move_score
            best_move = move

    return best_move


# Unit testing
if __name__ == '__main__':
    # X should win with (0, 1), (1, 2), or (2, 1)
    # O should block one of those
    board = [
        ["X", None, "X"],
        ["O", None, None],
        ["X", None, "X"],
    ]

    # X should move to either
    # (0, 1), (0, 2), or (1, 1)
    board_2 = [
        ['X', None, None],
        ['O', None, None],
        [None, None, None],
    ]

    # X should win
    # O should block
    # should always return (1, 1)
    board_3 = [
        ['X', None, None],
        ['O', None, None],
        [None, None, 'X']
    ]

    print(minimax_ai(board, "X"))
    print(minimax_ai(board, "O"))
    print(minimax_ai(board_2, 'X'))  # type: ignore
    print(minimax_ai(board_3, 'X'))
    print(minimax_ai(board_3, 'O'))
