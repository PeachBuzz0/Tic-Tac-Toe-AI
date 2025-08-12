"""
Script to hold all the functionality
for minimax algorithm
"""

# For now, assume bot is always playing as X
#
# 'board' is a 2-D grid of board state to analys
# 'current_player' is the player whose turn it is

def minimax_score(board: list[list[str | None]], current_player: str) -> int:
    # If board is a terminal state, immediatly
    # Return the appropriate score

    if x_has_won():
        return +10
    elif o_has_won():
        return -10
    elif is_draw
        return 0

    # If board is not a terminal state
    # get all moves that could be played
    legal_moves: list[tuple[int, int]] = get_legal_moves(board)

    # Iterate over moves, calculating a score for them
    # Keep all the scores in a list
    scores: list[int] = []

    for move in legal_moves:
        # First make the move
        new_board = make_board(board, move, current_player)

        # Then get minimax score for the resulting
        # board state, passing in 'current_player''s
        # opponents because it would be their turn

        opponent: str = get_oppenent(current_player)
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
