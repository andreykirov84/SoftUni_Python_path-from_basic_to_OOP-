def read_int_list_input(separator=' '):
    return [int(x) for x in input().split(separator)]


def print_matrix_row_by_row(input_matrix):
    for i in range(len(input_matrix)):
        print(' '.join(input_matrix[i]))


(rows_count, columns_count) = read_int_list_input()

matrix = []

for _ in range(rows_count):
    matrix.append(input().split(' '))

range_row = range(0, rows_count)
range_col = range(0, columns_count)

while True:
    command = input().split(' ')
    if command[0] == 'END':
        break
    elif command[0] == 'swap' and len(command) == 5:
        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])
        if row1 in range_row and row2 in range_row and col1 in range_col and col2 in range_col:
            row_col1 = matrix[row1][col1]
            row_col2 = matrix[row2][col2]
            matrix[row1][col1] = row_col2
            matrix[row2][col2] = row_col1
            print_matrix_row_by_row(matrix)
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
