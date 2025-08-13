"""
A minimax algorith that uses
a more heuristic approach with
tiebreakers and trying to
catch the opponent making a mistake
"""

from enum import Enum
from copy import deepcopy
from engine import determine_winner, get_opponent, get_legal_moves


_lines: list[list[tuple[int, int]]] = [
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


def _test_move(board: list[list[str | None]],
               move: tuple[int, int],
               current_player: str) -> list[list[str | None]]:

    _board: list[list[str | None]] = board.copy()

    _board[move[0]][move[1]] = current_player.upper()

    return _board


def _minimax_score(board: list[list[str | None]],
                   current_player: str,
                   player_we_want_to_win: str) -> int:

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
    scores: list[int] = []

    for move in legal_moves:
        _board: list[list[str | None]] = deepcopy(board)

        # First make the move
        _board = _test_move(_board, move, current_player)

        # Then get minimax score for the resulting
        # board state, passing in 'current_player''s
        # opponents because it would be their turn

        opponent: str = get_opponent(current_player)
        score: int = _minimax_score(_board, opponent,
                                    player_we_want_to_win)
        scores.append(score)

    # If current_player is our AI,
    # then we want maximized score
    if current_player == player_we_want_to_win:
        return max(scores)

    # If current_player is our opponent,
    # then we want to minimize score
    else:
        return min(scores)


def _blocks(board: list[list[str | None]],
            move: tuple[int, int],
            current_player: str) -> bool:
    _board: list[list[str | None]] = deepcopy(board)

    _board = _test_move(_board, move, current_player)

    opponent: str = get_opponent(current_player)

    for line in _lines:

        if move not in line:
            continue

        chars: list[str] = []

        for coord in line:
            if _board[coord[0]][coord[1]] is None:
                chars.append("")
            elif isinstance(_board[coord[0]][coord[1]], str):
                chars.append(_board[coord[0]][coord[1]])  # type: ignore

        if (chars.count(opponent) == 2) and (chars.count(current_player) == 1):
            return True

    return False


def _count_trap_lines(board: list[list[str | None]],
                      move: tuple[int, int],
                      current_player: str) -> int:
    _board: list[list[str | None]] = deepcopy(board)

    _board = _test_move(_board, move, current_player)

    trap_lines: int = 0

    for line in _lines:
        chars: list[str] = []

        for coord in line:
            if _board[coord[0]][coord[1]] is None:
                chars.append('')
            elif isinstance(_board[coord[0]][coord[1]], str):
                chars.append(_board[coord[0]][coord[1]])  # type: ignore

        if (chars.count(current_player) == 2) and ('' in chars):
            trap_lines += 1

    return trap_lines


def _in_corner(move: tuple[int, int]) -> bool:
    corners: list[tuple[int, int]] = [
        (0, 0), (0, 2),
        (2, 0), (2, 2)
    ]

    if move in corners:
        return True
    else:
        return False


def _in_center(move: tuple[int, int]) -> bool:
    if move == (1, 1):
        return True
    else:
        return False


def _get_tiebreaker_score(board: list[list[str | None]],
                          move: tuple[int, int],
                          current_player: str) -> int:
    # TODO decide rules for tie breaking
    class KeyIndex(Enum):
        BLOCKS = 0
        TRAP_LINES = 1
        IN_CORNER = 2
        IN_CENTER = 3

    score_dict: dict[KeyIndex, int] = {
        KeyIndex.BLOCKS: 0,
        KeyIndex.TRAP_LINES: 0,
        KeyIndex.IN_CORNER: 0,
        KeyIndex.IN_CENTER: 0
    }

    _board: list[list[str | None]] = deepcopy(board)

    if _blocks(_board, move, current_player):
        score_dict[KeyIndex.BLOCKS] = 1

    for i in range(_count_trap_lines(_board, move, current_player)):
        score_dict[KeyIndex.TRAP_LINES] += 1

    if _in_corner(move):
        score_dict[KeyIndex.IN_CORNER] = 1

    if _in_center(move):
        score_dict[KeyIndex.IN_CENTER] = 1

    raise NotImplementedError


def minimax_ai(board: list[list[str | None]],
               current_player: str) -> tuple[int, int]:
    best_score: float = -1000
    best_move: tuple[int, int] = (-1, -1)

    best_moves: list[tuple[int, int]] = []

    legal_moves: list[tuple[int, int]] = get_legal_moves(board)

    # TODO store moves that result in best score in a list
    #  and have some function to determin best one from there
    for move in legal_moves:
        _board: list[list[str | None]] = deepcopy(board)
        _board = _test_move(_board, move, current_player)

        move_score: float = _minimax_score(_board,
                                           get_opponent(current_player),
                                           current_player)

        if move_score > best_score:
            best_score = move_score
            best_move = move
            best_moves = [move]

        if move_score == best_score:
            best_moves.append(move)

    if len(best_moves) == 1:
        have_best_move = True
    else:
        have_best_move = False

    while not have_best_move:

        for move in best_moves:
            _tie_board: list[list[str | None]] = deepcopy(board)
            tb_score = _get_tiebreaker_score(_tie_board, move, current_player)

            if tb_score > best_score:
                best_score = tb_score
                best_move = move
                best_moves = [move]

            if tb_score == best_score:
                best_moves.append(move)

        if len(best_moves) == 1:
            have_best_move = True

    return best_move


# Unit testing
if __name__ == '__main__':
    ...
