row1 = input().split(' ')
row2 = input().split(' ')
row3 = input().split(' ')
ll = [row1, row2, row3]
for i in range(3):
    for j in range(3):
        ll[i][j] = int(ll[i][j])

flag = 0
for i in range(3):
    if ll[i][0] == ll[i][1] == ll[i][1] == 1:
        flag = 1

for i in range(3):
    if ll[i][0] == ll[i][1] == ll[i][1] == 2:
        flag = 2

for j in range(3):
    if ll[0][j] == ll[1][j] == ll[2][j] == 1:
        flag = 1

for j in range(3):
    if ll[0][j] == ll[1][j] == ll[2][j] == 2:
        flag = 2

if ll[0][0] == ll[1][1] == ll[2][2] == 1:
    flag = 1

if ll[0][0] == ll[1][1] == ll[2][2] == 2:
    flag = 2

if ll[0][2] == ll[1][1] == ll[2][0] == 1:
    flag = 1

if ll[0][2] == ll[1][1] == ll[2][0] == 2:
    flag = 2

if flag == 0:
    print("Draw!")
elif flag == 1:
    print("First player won")
elif flag == 2:
    print("Second player won")
