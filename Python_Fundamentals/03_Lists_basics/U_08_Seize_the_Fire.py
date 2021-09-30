effort = 0
result = []
fire = input().split('#')
water = float(input())
for i in range(len(fire)):
    ll = fire[i].split(' = ')

    if ll[0] == 'High' and 81 <= float(ll[1]) <= 125 and water >= float(ll[1]):
        effort += 0.25 * float(ll[1])
        water -= float(ll[1])
        result.append(int(ll[1]))

    elif ll[0] == 'Medium' and 51 <= float(ll[1]) <= 80 and water >= float(ll[1]):
        effort += 0.25 * float(ll[1])
        water -= float(ll[1])
        result.append(int(ll[1]))

    elif ll[0] == 'Low' and 1 <= float(ll[1]) <= 50 and water >= float(ll[1]):
        effort += 0.25 * float(ll[1])
        water -= float(ll[1])
        result.append(int(ll[1]))

print('Cells:')
for i in range(len(result)):
    print(f' - {result[i]}')
print(f'Effort: {round(effort, 2):.2f}')
print(f'Total Fire: {sum(result)}')
