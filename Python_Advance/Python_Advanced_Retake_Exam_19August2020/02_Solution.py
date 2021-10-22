bomb_mark = '*'
matrix_size = int(input())
matrix = []

# generate the matrix
for i in range(matrix_size):
    matrix.append([])
    for j in range(matrix_size):
        matrix[i].append(0)

# place the bombs
bombs_number = int(input())
for _ in range(bombs_number):
    bomb_row, bomb_col = [int(x) for x in input()[1:-1].split(', ')]
    matrix[bomb_row][bomb_col] = bomb_mark

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] != '*':
            submatrix_row_min = 0
            submatrix_row_max = 0
            submatrix_col_min = 0
            submatrix_col_max = 0
            submatrix_sum = 0

            if row - 1 < 0:
                submatrix_row_min = 0
                submatrix_row_max = row + 1
            elif row + 1 >= matrix_size:
                submatrix_row_max = matrix_size - 1
                submatrix_row_min = row - 1
            else:
                submatrix_row_min = row - 1
                submatrix_row_max = row + 1

            if col - 1 < 0:
                submatrix_row_min = 0
                submatrix_col_max = col + 1
            elif col + 1 >= matrix_size:
                submatrix_col_max = matrix_size - 1
                submatrix_col_min = col - 1
            else:
                submatrix_col_min = col - 1
                submatrix_col_max = col + 1

            for i in range(submatrix_row_min, submatrix_row_max + 1):
                for j in range(submatrix_col_min, submatrix_col_max + 1):
                    if matrix[i][j] == '*':
                        submatrix_sum += 1

            matrix[row][col] = submatrix_sum

for line in matrix:
    print(*line, sep=' ')






