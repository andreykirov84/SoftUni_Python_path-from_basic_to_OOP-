matrix_rows = int(input())
ll = []
for _ in range(matrix_rows):
    line = list(map(int, input().split(' ')))
    ll.append(line)
primary_diagonal = 0

for position in range(matrix_rows):
    primary_diagonal += ll[position][position]

print(primary_diagonal)
