"""
adding custom caching functionality
to the minimax algorithm
Writing these manually for learning
and functools caching won't work
because board is inputted as list
which isn't hashable
"""

from copy import deepcopy
from engine import determine_winner, get_opponent, get_legal_moves, new_board


def _test_move(board: list[list[str | None]],
               move: tuple[int, int],
               current_player: str) -> list[list[str | None]]:

    _board: list[list[str | None]] = board.copy()

    _board[move[0]][move[1]] = current_player.upper()

    return _board


_cache: dict = {}


def _caching_minimax_score(board: list[list[str | None]],
                           current_player: str,
                           player_we_want_to_win: str,
                           branch: int = 0) -> float:
    """
    Use the minimax algorithm score next move.
    Also caches results
    """

    # Turn board into a str to use for key
    board_cache_key: str = ''

    for row in range(3):
        row_str: str = ''
        for col in range(3):
            char: str | None = board[row][col]

            if char is None:
                row_str += '-'
            else:
                row_str += char.upper()

        board_cache_key += row_str

    if board_cache_key in _cache:
        return _cache[board_cache_key]

    if determine_winner(board) == player_we_want_to_win:
        _cache[board_cache_key] = 10
        return _cache[board_cache_key]
    elif determine_winner(board) == get_opponent(player_we_want_to_win):
        _cache[board_cache_key] = -10
        return _cache[board_cache_key]
    elif determine_winner(board) == 'draw':
        _cache[board_cache_key] = 0
        return _cache[board_cache_key]

    legal_moves: list[tuple[int, int]] = get_legal_moves(board)

    scores: list[float] = []

    for move in legal_moves:
        _board: list[list[str | None]] = deepcopy(board)

        _board = _test_move(_board, move, current_player)

        opponent: str = get_opponent(current_player)
        score: float = _caching_minimax_score(_board, opponent,
                                              player_we_want_to_win,
                                              branch + 1)
        scores.append(score - (branch * 0.1))

    if current_player == player_we_want_to_win:
        _cache[board_cache_key] = max(scores)
    else:
        _cache[board_cache_key] = min(scores)

    return _cache[board_cache_key]


def caching_minimax_ai(board: list[list[str | None]],
                       current_player: str) -> tuple[int, int]:
    best_score: float = -1000.0
    best_move: tuple[int, int] = (-1, -1)

    legal_moves: list[tuple[int, int]] = get_legal_moves(board)

    for move in legal_moves:
        _board: list[list[str | None]] = deepcopy(board)
        _board = _test_move(_board, move, current_player)

        move_score: float = _caching_minimax_score(_board,
                                                   get_opponent(current_player),
                                                   current_player)

        if move_score >= best_score:
            best_score = move_score
            best_move = move

    return best_move


if __name__ == '__main__':
    board1 = new_board()

    print(caching_minimax_ai(board1, 'X'))
    print(_cache)
