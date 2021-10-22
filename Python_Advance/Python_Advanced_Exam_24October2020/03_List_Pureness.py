def calc_pureness(input_ll):
    ll = [] + input_ll
    pureness = 0
    for i in range(len(ll)):
        pureness += i * ll[i]
    return pureness


def best_list_pureness(ll, number):
    rotations = 0
    max_pureness = 0
    best_rotation = 0

    for _ in range(number):
        result = calc_pureness(ll)
        if result > max_pureness:
            max_pureness = result
            best_rotation = rotations
            rotations += 1
            ll.insert(0, ll.pop())

    return f'Best pureness {max_pureness} after {best_rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
