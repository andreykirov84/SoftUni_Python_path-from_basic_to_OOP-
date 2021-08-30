matrix_rows, matrix_cols = list(map(int, input().split(', ')))
ll = []
for _ in range(matrix_rows):
    line = list(map(int, input().split(' ')))
    ll.append(line)

for col in range(matrix_cols):
    sum_col = 0
    for row in range(matrix_rows):
        sum_col += ll[row][col]
    print(sum_col)

