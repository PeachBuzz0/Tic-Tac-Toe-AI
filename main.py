"""
Tic Tac Toe AI
Created by: Gabe(Peach)
Created on: Aug 1, 2025 01:30 AM
"""


def new_board() -> list[list[None]]:
    empty_board = [[None for _ in range(3)] for _ in range(3)]
    return empty_board


def render(board: list[list[str | None]]) -> None:
    # PRINT COL NUMS TO TOP OF BOARD
    print("   0 1 2 ")
    print(" ---------")

    for row in range(3):
        print(f'{row}|', end=" ")
        for col in range(3):
            if board[row][col] is None:
                print(".", end=" ")
            elif board[row][col].lower() == "o":
                print("O", end=" ")
            elif board[row][col].lower() == "x":
                print("X", end=" ")
            else:
                print(".", end=" ")
        print('|')

    print(" ---------")


def get_move() -> tuple[int, int]:
    user_move = input("Enter your move(row col): ")

    split_user_move: list[str] = user_move.split()

    user_cords: tuple[int, int] = (int(split_user_move[0]), int(split_user_move[1]))

    return user_cords


def is_valid_move(board: list[list[str | None]], move: tuple[int, int]) -> bool:
    try:
        if move[0] < 0 or move[1] < 0:  # Dont let players negative index
            raise IndexError
        elif board[move[0]][move[1]] is None:
            return True
        else:
            print(f"Invalid move! {move} is already taken, try again.")
            return False
    except IndexError:
        print("Invalid move. Row or Column does not exist.")
        return False


def make_move(board: list[list[str | None]],
              move_coords: tuple[int, int],
              player_mark: str) -> list[list[str | None]]:
    next_board: list[list[str | None]] = board.copy()

    while True:
        if is_valid_move(board, move_coords):
            break
        else:
            move_coords = get_move()

    next_board[move_coords[0]][move_coords[1]] = player_mark
    return next_board


def get_winner(board: list[list[str | None]]) -> str | None:
    winner: str

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
                chars.append(board[coord[0]][coord[1]])

        if (chars[0] == chars[1]) == (chars[0] == chars[2]) is True:
            winner = chars[0]
            return winner

    if open_spaces == 0:
        return "draw"

    return None


if __name__ == "__main__":
    # Initialize Board
    board: list[list[str | None]] = new_board()

    # Pick a Player To Go First
    turn: int = 1

    while True:
        render(board)

        if get_winner(board):
            break

        player: str
        if (turn % 2) == 0:
            player = 'x'
        else:
            player = 'o'

        make_move(board, get_move(), player)

        turn += 1
