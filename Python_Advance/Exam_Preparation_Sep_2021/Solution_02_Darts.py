def change_player(flag):
    if flag is True:
        flag = False
    else:
        flag = True
    return flag


winner = None
turns_counter = 0
player1_points = 501
player2_points = 501
players= input().split(', ')
player1 = players[0]
player2 = players[1]
matrix_size = 7
matrix = []
player1_turn = True
while matrix_size > 0:
    matrix.append(input().split(' '))
    matrix_size -= 1

# print(player1, player2)
# for row in matrix:
#     print(row)

while player1_points > 0 and player2_points > 0:
    row, column = [int(x) for x in input()[1: -1].split(', ')]
    if row not in range(0, 7) and column not in range(0, 7):
        turns_counter += 1
        player1_turn = change_player(player1_turn)
        continue
    hit = matrix[row][column]
    point_border_sum = int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][column]) + int(matrix[-1][column])
    turns_counter += 1
    if hit == 'B':
        if player1_turn:
            player1_points = 0
        else:
            player2_points = 0
    elif hit == 'D':
        if player1_turn:
            player1_points -= 2 * point_border_sum
        else:
            player2_points -= 2 * point_border_sum
    elif hit == 'T':
        if player1_turn:
            player1_points -= 3 * point_border_sum
        else:
            player2_points -= 3 * point_border_sum
    else:
        if player1_turn:
            player1_points -= int(hit)
        else:
            player2_points -= int(hit)
    player1_turn = change_player(player1_turn)

if player1_points == 0:
    winner = player1
else:
    winner = player2

print(f'{winner} won the game with {round(turns_counter / 2) + 1} throws!')






