from collections import deque
storage = {'Palm': 0, 'Willow': 0, 'Crossette': 0}

effect_ll = [int(x) for x in input().split(', ')]
power_ll = [int(x) for x in input().split(', ')]

while len(effect_ll) > 0 and len(power_ll) > 0:
    effect = effect_ll.pop(0)
    power = power_ll.pop()
    if effect <= 0:
        power_ll.insert(0, power)
    elif power <= 0:
        effect_ll.append(effect)
    else:
        product = effect + power
        if product % 3 == 0 and product % 5 != 0:
            storage['Palm'] += 1
        elif product % 3 != 0 and product % 5 == 0:
            storage['Willow'] += 1
        elif product % 3 == 0 and product % 5 == 0:
            storage['Crossette'] += 1
        else:
            effect_ll.append(effect - 1)
            power_ll.insert(0, power)

success_flag = True
for elem in storage.values():
    if elem < 3:
        print("Sorry. You can't make the perfect firework show.")
        success_flag = False
        break

if success_flag:
    print("Congrats! You made the perfect firework show!")

if len(effect_ll) > 0:
    print('Firework Effects left: ', end=' ')
    print(*effect_ll, sep=', ')

if len(power_ll) > 0:
    print('Explosive Power left: ', end=' ')
    print(*power_ll, sep=', ')

for item, quantity in storage.items():
    print(f'{item} Fireworks: {quantity}')

