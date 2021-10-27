def outside(command, range):
    row, col = command[0], command[1]
    if 0 <= row < range and 0 <= col < range:
        return False
    return True


player_names = input().split(', ')

players = {
    player_names[0]: [501, 0],
    player_names[1]: [501, 0]
}

matrix = []

for _ in range(7):
    matrix.append(input().split())

is_done = False

command = input()

while command:
    cmd_list = []

    for cmd in command:
        if cmd.isdigit():
            cmd_list.append(int(cmd))
    if not outside(cmd_list, 7):
        row = cmd_list[0]
        col = cmd_list[1]
        for player in player_names:
            current_player = player
            players[current_player][1] += 1
            if matrix[row][col] == 'B':
                players[current_player][0] -= 501
            elif matrix[row][col] == 'T':
                result = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 3
                players[current_player][0] -= result
            elif matrix[row][col] == 'D':
                result = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 2
                players[current_player][0] -= result
            else:
                result = int(matrix[row][col])
                players[current_player][0] -= result
            if players[current_player][0] <= 0:
                print(f'{current_player} won the game with {players[current_player][1]} throws!')
                is_done = True
                break
            if is_done:
                break
            player_names[0], player_names[1] = player_names[1], player_names[0]
            command = input()
            break
    if is_done:
        break