def enough_fireworks(v1, v2, v3):
    if v1 >= 3 and v2 >= 3 and v3 >= 3:
        return True
    else:
        return False


firework_effects = [int(x) for x in input().split(', ')]
explosive_powers = [int(x) for x in input().split(', ')]
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while not enough_fireworks(palm_fireworks, willow_fireworks, crossette_fireworks) and len(firework_effects) > 0 and len(explosive_powers) > 0:
    if firework_effects[0] <= 0:
        firework_effects.pop(0)
        continue
    elif explosive_powers[-1] <= 0:
        explosive_powers.pop(-1)
        continue
    else:
        firepower = firework_effects[0]
        explosive = explosive_powers[-1]
        result = firepower + explosive
        if result % 3 == 0 and result % 5 == 0:
            crossette_fireworks += 1
            firework_effects.pop(0)
            explosive_powers.pop(-1)
        elif result % 3 == 0:
            palm_fireworks += 1
            firework_effects.pop(0)
            explosive_powers.pop(-1)
        elif result % 5 == 0:
            willow_fireworks += 1
            firework_effects.pop(0)
            explosive_powers.pop(-1)
        else:
            firework_effects.pop(0)
            firework_effects.append(firepower - 1)

if enough_fireworks(palm_fireworks, willow_fireworks, crossette_fireworks):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f'Firework Effects left: ', end='')
    print(*firework_effects, sep=', ')
if explosive_powers:
    print(f'Explosive Power left: ', end='')
    print(*explosive_powers, sep=', ')
print(f'Palm Fireworks: {palm_fireworks}')
print(f'Willow Fireworks: {willow_fireworks}')
print(f'Crossette Fireworks: {crossette_fireworks}')

