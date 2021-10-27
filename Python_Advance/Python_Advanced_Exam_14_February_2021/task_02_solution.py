from math import floor

directions = {
    'left': [0, -1],
    'up': [-1, 0],
    'right': [0, 1],
    'down': [1, 0]
}

MATRIX_SIZE = int(input())
WALL_SYMBOL = 'X'
PLAYER_SYMBOL = 'P'
matrix = []
total_coins = 0
path = []
win_game = True


def in_range(value, max_value):
    return 0 <= value < max_value


def get_player_coordinates(matrix):
    player_row = 0
    player_col = 0
    for i in range(len(matrix)):
        if PLAYER_SYMBOL in matrix[i]:
            player_row = i
            player_col = matrix[i].index(PLAYER_SYMBOL)
            break
    return(player_row, player_col)


for _ in range(MATRIX_SIZE):
    line = input().split(' ')
    result = []
    for char in line:
        if char.isnumeric():
            result.append(int(char))
        else:
            result.append(char)
    matrix.append(result)

player_row, player_column = get_player_coordinates(matrix)


while True:
    command = input()
    if command in directions.keys():
        row_delta, column_delta = directions[command]

        player_row += row_delta
        player_column += column_delta

        if in_range(player_row, MATRIX_SIZE) \
                and in_range(player_column, MATRIX_SIZE) \
                and matrix[player_row][player_column] != WALL_SYMBOL:
            path.append([player_row, player_column])
            total_coins += matrix[player_row][player_column]
            if total_coins >= 100:
                break
        else:
            total_coins = floor(total_coins * 0.5)
            win_game = False
            break


if total_coins < 100 and not win_game:
    win_game = False

if win_game:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")

print('Your path:')
print(*path, sep='\n')
