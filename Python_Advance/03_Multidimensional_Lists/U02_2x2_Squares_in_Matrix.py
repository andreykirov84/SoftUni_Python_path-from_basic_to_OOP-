def read_int_list_input(separator=' '):
    return [int(x) for x in input().split(separator)]


(rows_count, columns_count) = read_int_list_input()

matrix = []

for _ in range(rows_count):
    matrix.append(input().split(' '))

n = 0
sub_matrix_max = []
s = set()
for i in range(rows_count - 1):
    for j in range(columns_count - 1):
        sub_matrix = (matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1])
        # print(sub_matrix)
        if len(set(sub_matrix)) == 1:
            n += 1

print(n)
