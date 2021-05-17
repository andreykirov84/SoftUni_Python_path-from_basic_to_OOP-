ll = list(map(lambda x: int(x), input().split(', ')))
min_wealth = int(input())
if sum(ll) < min_wealth * len(ll):
    print('No equal distribution possible')
else:
    for i in range(len(ll)):
        max_value = max(ll)
        max_index = ll.index(max_value)
        if ll[i] < min_wealth:
            ll[max_index] = max_value - min_wealth + ll[i]
            ll[i] = min_wealth

    print(ll)



