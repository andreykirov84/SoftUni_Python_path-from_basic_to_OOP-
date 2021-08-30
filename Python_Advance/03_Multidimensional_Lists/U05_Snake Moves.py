from collections import deque


def read_int_list_input(separator=' '):
    return [int(x) for x in input().split(separator)]


def print_matrix_row_by_row(input_matrix):
    for i in range(len(input_matrix)):
        print(''.join(input_matrix[i]))


(rows_count, columns_count) = read_int_list_input()
matrix = [[0 for x in range(columns_count)] for y in range(rows_count)]

snake = deque(input())

for i in range(rows_count):
    if i == 0 or (i % 2) == 0:
        for j in range(columns_count):
            x = snake.popleft()
            snake.append(x)
            matrix[i][j] = x
    else:
        for j in range(columns_count-1, -1, -1):
            x = snake.popleft()
            snake.append(x)
            matrix[i][j] = x

print_matrix_row_by_row(matrix)