def odd_even_sum(x):
    odd_sum = 0
    even_sum = 0
    ll = [int(ch) for i in x for ch in str(i)]

    for i in range(len(ll)):
        ll[i] = int(ll[i])

    for i in range(len(ll)):
        if ll[i] % 2 == 0:
            even_sum += ll[i]
        else:
            odd_sum += ll[i]
    return odd_sum, even_sum


x, y = odd_even_sum(input())
print(f'Odd sum = {x}, Even sum = {y}')

