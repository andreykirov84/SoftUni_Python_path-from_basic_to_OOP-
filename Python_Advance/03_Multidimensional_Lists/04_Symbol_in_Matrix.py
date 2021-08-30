matrix_rows = int(input())
ll = []
for _ in range(matrix_rows):
    line = list(input())
    ll.append(line)
target_symbol = input()
find_flag = False

for row in range(matrix_rows):
    for col in range(matrix_rows):
        if ll[row][col] == target_symbol and not find_flag:
            find_flag = True
            print(f'({row}, {col})')
            break


if not find_flag:
    print(f"{target_symbol} does not occur in the matrix")
