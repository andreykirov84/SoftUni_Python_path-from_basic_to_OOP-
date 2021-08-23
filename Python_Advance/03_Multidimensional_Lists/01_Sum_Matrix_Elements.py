
matrix_rows, matrix_cols = list(map(int, input().split(', ')))
# ll = [[] for _ in range(matrix_rows)]
ll = []
total_sum = 0

for _ in range(matrix_rows):
    line = list(map(int, input().split(', ')))
    ll.append(line)
    total_sum += sum(line)

print(total_sum)
print(ll)
