a_team = 11
b_team = 11
command = input()
ll = command.split(' ')
ll = set(ll)
ll = list(ll)
if len(ll) > 0:
    for i in range(len(ll)):
        if 'A' in ll[i]:
            a_team -= 1
        if 'B' in ll[i]:
            b_team -= 1
        if a_team < 7 or b_team < 7:
            break
print(f'Team A - {a_team}; Team B - {b_team}')
if a_team < 7 or b_team < 7:
    print("Game was terminated")
