ll = input().split(' ')
for i in range(len(ll)):
    ll[i] = int(ll[i])

left_total = 0
right_total = 0

left_ll = ll[0:len(ll) // 2]
right_ll = ll[len(ll) // 2 + 1::]

for i in range(len(left_ll)):
    if left_ll[i] != 0:
        left_total += left_ll[i]
    else:
        left_total -= 0.2 * left_total

for i in range(len(right_ll)):
    if right_ll[i] != 0:
        right_total += right_ll[i]
    else:
        right_total -= 0.2 * right_total

if left_total < right_total:
    print(f"The winner is left with total time: {left_total:.1f}")
else:
    print(f"The winner is right with total time: {right_total:.1f}")
