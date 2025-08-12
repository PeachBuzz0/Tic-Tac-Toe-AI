"""
Script to hold all the functionality
for minimax algorithm
"""

# For now, assume bot is always playing as X
#
# 'board' is a 2-D grid of board state to analys
# 'current_player' is the player whose turn it is


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

    for line in lines:
        chars: list[str] = []

        for coord in line:
            if board[coord[0]][coord[1]] is None:
                chars.append('')
            elif isinstance(board[coord[0]][coord[1]], str):
                chars.append(board[coord[0]][coord[1]])  # type: ignore

        if chars.count('O') == 3:
            return 'O'
        elif chars.count('X') == 3:
            return 'X'
        elif chars.count('') == 3:
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


def make_board(board: list[list[str | None]],
               move: tuple[int, int],
               current_player: str) -> list[list[str | None]]:

    new_board: list[list[str | None]] = board.copy()

    new_board[move[0]][move[1]] = current_player.upper()

    return new_board


def get_opponent(current_player: str) -> str:
    current_player = current_player.upper()

    if current_player == 'X':
        return 'O'
    elif current_player == 'O':
        return 'X'
    else:
        raise ValueError('Invalid player')


def minimax_score(board: list[list[str | None]], current_player: str) -> int:
    # If board is a terminal state, immediately
    # Return the appropriate score

    if determine_winner(board) == 'X':
        return +10
    elif determine_winner(board) == 'O':
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
        # First make the move
        new_board: list[list[str | None]] = make_board(board,
                                                       move,
                                                       current_player)

        # Then get minimax score for the resulting
        # board state, passing in 'current_player''s
        # opponents because it would be their turn

        opponent: str = get_opponent(current_player)
        score: int = minimax_score(new_board, opponent)
        scores.append(score)

    # If current_player is our AI (X for now),
    # then we want maximized score
    if current_player == 'X':
        return max(scores)

    # If current_player is our opponent(O for now),
    # then we want to minimize score
    else:
        return min(scores)
