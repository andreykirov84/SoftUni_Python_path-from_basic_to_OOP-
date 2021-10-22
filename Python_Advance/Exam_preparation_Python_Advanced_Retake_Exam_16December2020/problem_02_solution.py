def correct_move(row, col, matrix_size, command):
    new_col = 0
    new_row = 0
    correct = None
    if command == 'left':
        if col > 0:
            new_col = col - 1
            new_row = row
            correct = True
        else:
            new_col = col
            new_row = row
            correct = False

    elif command == 'right':
        if col != matrix_size - 1:
            new_col = col + 1
            new_row = row
            correct = True
        else:
            new_col = col
            new_row = row
            correct = False

    elif command == 'up':
        if row > 0:
            new_col = col
            new_row = row - 1
            correct = True
        else:
            new_col = col
            new_row = row
            correct = False

    elif command == 'down':
        if row != matrix_size - 1:
            new_col = col
            new_row = row + 1
            correct = True
        else:
            new_col = col
            new_row = row
            correct = False

    return new_row, new_col, correct


matrix = []
row = 0
column = 0
initial_position_mark = 'P'

snake_str = input()
matrix_size = int(input())

for _ in range(matrix_size):
    matrix.append(list(input()))

for i in range(matrix_size):
    if initial_position_mark in matrix[i]:
        row = i
        column = matrix[i].index(initial_position_mark)

number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input()
    new_row, new_col, flag = correct_move(row, column, matrix_size, command)
    if not flag:
        if snake_str:
            snake_str = snake_str[:-1]
        row, column = new_row, new_col
    else:
        if matrix[new_row][new_col] != '-':
            snake_str += matrix[new_row][new_col]
        matrix[row][column] = '-'
        matrix[new_row][new_col] = 'P'
        row, column = new_row, new_col

print(snake_str)
# print(matrix)
for line in matrix:
    print(*line, sep='')
