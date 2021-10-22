MATRIX_SIZE = 8
KING_SYMBOL = 'K'
QUEEN_SYMBOL = 'Q'
queens = []


def in_range(value, max_value):
    return 0 <= value < max_value


def read_board(size):
    matrix = []
    for _ in range(size):
        matrix.append(list(input().split(' ')))
    return matrix


def find_king_position(matrix):
    king_row = 0
    king_column = 0
    for i in range(len(matrix)):
        if 'K' in matrix[i]:
            king_row = i
            king_column = matrix[i].index(KING_SYMBOL)
    return (king_row, king_column)


def search_with_deltas(board, king, deltas):
    row_index, column_index = king
    rows_count = len(board)
    column_count = len(board[0])
    delta_row, delta_column = deltas
    while in_range(row_index, rows_count) and in_range(column_index, column_count):
        if board[row_index][column_index] == QUEEN_SYMBOL:
            return [row_index, column_index]

        row_index += delta_row
        column_index += delta_column


def get_capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1)
    ]
    return [search_with_deltas(board, king, delta) for delta in deltas]


def print_result(queens):
    for i in range(len(queens) - 1, -1, -1):
        if queens[i] is None:
            queens.pop(i)

    if queens:
        print(*queens, sep='\n')
    else:
        print('The king is safe!')


board = read_board(MATRIX_SIZE)
king = find_king_position(board)
queens = get_capturing_queens(board, king)
print_result(queens)


