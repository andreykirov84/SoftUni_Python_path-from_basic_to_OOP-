def read_int_list_input(separator=' '):
    return [int(x) for x in input().split(separator)]


n = int(input())
matrix = []

for _ in range(n):
    matrix.append(
        read_int_list_input()
    )


def primary_diagonal(matrix):
    primary_diagonal_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                primary_diagonal_list.append(matrix[i][j])
    return primary_diagonal_list


def secondary_diagonal(matrix):
    secondary_diagonal_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i+j) == (n-1):
                secondary_diagonal_list.append(matrix[i][j])
    return secondary_diagonal_list


primary = sum(primary_diagonal(matrix))
secondary = sum(secondary_diagonal(matrix))
result = abs(primary - secondary)
print(result)
