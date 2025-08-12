"""
Script to hold all the functionality
for minimax algorithm
"""

from copy import deepcopy


def determine_winner(board: list[list[str | None]]) -> str:
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

        if chars.count('O') == 3:
            return 'O'
        elif chars.count('X') == 3:
            return 'X'

    if open_spaces == 0:
        return 'draw'

    return ''


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


def make_move(board: list[list[str | None]],
               move: tuple[int, int],
               current_player: str) -> list[list[str | None]]:

    _board: list[list[str | None]] = board.copy()

    _board[move[0]][move[1]] = current_player.upper()

    return _board


def get_opponent(current_player: str) -> str:
    current_player = current_player.upper()

    if current_player == 'X':
        return 'O'
    elif current_player == 'O':
        return 'X'
    else:
        raise ValueError('Invalid player')


def _minimax_score(board: list[list[str | None]], current_player: str, player_we_want_to_win: str) -> int:
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
        _board = make_move(_board, move, current_player)

        # Then get minimax score for the resulting
        # board state, passing in 'current_player''s
        # opponents because it would be their turn

        opponent: str = get_opponent(current_player)
        score: int = _minimax_score(_board, opponent, player_we_want_to_win)
        scores.append(score)

    # If current_player is our AI (X for now),
    # then we want maximized score
    if current_player == player_we_want_to_win:
        return max(scores)

    # If current_player is our opponent(O for now),
    # then we want to minimize score
    else:
        return min(scores)

def minimax_ai(board: list[list[str | None]], current_player: str) -> tuple[int, int]:
    best_score: int = -1000
    best_move: tuple[int, int] = (-1, -1)

    legal_moves: list[tuple[int, int]] = get_legal_moves(board)

    for move in legal_moves:
        _board: list[list[str | None]] = deepcopy(board)
        _board = make_move(_board, move, current_player)

        move_score = _minimax_score(_board, get_opponent(current_player), current_player)

        if move_score >= best_score:
            best_score = move_score
            best_move = move

    return best_move


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
    print(minimax_ai(board_2, 'X'))
    print(minimax_ai(board_3, 'X'))
    print(minimax_ai(board_3, 'O'))