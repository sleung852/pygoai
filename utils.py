from pygoai import gotypes

COLS = 'ABCDEFGHIJKLMNOPQRST'
STONE_TO_CHAR = {
    None: ' . ',
    gotypes.Player.black: ' x ',
    gotypes.Player.white: ' o ',
}

def print_move(player, move):
    if move.is_pass:
        move_str = 'passes'
    elif move.is_resign:
        move_str = 'resigns'
    else:
        move_str = '{}{}'.format(COLS[move.point.col - 1], move.point.row)
    print('{} {}'.format(player, move_str))

def print_board(board):
    for r in range(board.num_rows, 0, -1):
        bump = " " if r <= 9 else ""
        line = []
        for c in range(1, board.num_cols + 1):
            stone = board.get(gotypes.Point(row=r, col=c))
            line.append(STONE_TO_CHAR[stone])
        print("{}{} {}".format(bump, r, "".join(line)))
    print("    " + "  ".join(COLS[:board.num_cols]))
