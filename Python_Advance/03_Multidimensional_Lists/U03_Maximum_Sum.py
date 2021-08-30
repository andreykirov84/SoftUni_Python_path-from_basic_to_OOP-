def read_int_list_input(separator=' '):
    return [int(x) for x in input().split(separator)]


(rows_count, columns_count) = read_int_list_input(', ')

matrix = []

for _ in range(rows_count):
    matrix.append(
        read_int_list_input(',')
    )

# print(matrix)

sub_matrix_max = ()
for i in range(rows_count-1):
    for j in range(columns_count-1):
        sub_matrix = (matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])
        if sum(sub_matrix) > sum(sub_matrix_max):
            sub_matrix_max = sub_matrix


print(f'{sub_matrix_max[0]} {sub_matrix_max[1]}\n{sub_matrix_max[2]} {sub_matrix_max[3]}')
print(sum(sub_matrix_max))

