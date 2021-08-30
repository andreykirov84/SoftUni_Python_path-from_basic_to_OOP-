def read_int_list_input(separator=' '):
    return [int(x) for x in input().split(separator)]


(rows_count, columns_count) = list(map(int, input().split(' ')))
matrix = []

for _ in range(rows_count):
    matrix.append(
        read_int_list_input(' ')
    )


sub_matrix_max = ()
for i in range(rows_count-2):
    for j in range(columns_count-2):
        sub_matrix = (matrix[i][j], matrix[i][j+1], matrix[i][j+2], matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2], matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2])
        if sum(sub_matrix) > sum(sub_matrix_max):
            sub_matrix_max = sub_matrix

print(f'Sum = {sum(sub_matrix_max)}')
print(f'{sub_matrix_max[0]} {sub_matrix_max[1]} {sub_matrix_max[2]}')
print(f'{sub_matrix_max[3]} {sub_matrix_max[4]} {sub_matrix_max[5]}')
print(f'{sub_matrix_max[6]} {sub_matrix_max[7]} {sub_matrix_max[8]}')



