matches = 0
males = [int(x) for x in input().split(' ')]
females = [int(x) for x in input().split(' ')]

for i in range(len(males) - 1, -1, -1):
    if males[i] <= 0:
        males.pop(i)

for i in range(len(females) - 1, -1, -1):
    if females[i] <= 0:
        females.pop(i)

while males and females:
    if males[-1] <= 0:
        males.pop(-1)
    elif females[0] <= 0:
        females.pop(0)
    elif males[-1] % 25 == 0:
        males.pop(-1)
        if males:
            males.pop(-1)
    elif females[0] % 25 == 0:
        females.pop(0)
        if females:
            females.pop(0)

    if males[-1] == females[0]:
        matches += 1
        males.pop(-1)
        females.pop(0)
    else:
        females.pop(0)
        males[-1] -= 2


males = males[::-1]

print(f'Matches: {matches}')
if not males:
    print('Males left: none')
else:
    print('Males left: ', end='')
    print(*males, sep=', ')

if not females:
    print("Females left: none")
else:
    print('Females left: ', end='')
    print(*females, sep=', ')


