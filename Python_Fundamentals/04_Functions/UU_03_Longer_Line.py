def side_length(a, b):
    if a > 0 and b > 0:
        c = abs(a + b)
    elif a < 0 and b < 0:
        c = abs(a + b)
    else:
        c = abs(a - b)
    return c


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    z1 = side_length(x1, x2)
    z2 = side_length(y1, y2)
    z3 = side_length(x3, x4)
    z4 = side_length(y3, y4)
    ll = []
    final = ''
    if z1 ** 2 + z2 ** 2 >= z3 ** 2 + z4 ** 2:
        if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
            ll.append(x1)
            ll.append(y1)
            ll.append(x2)
            ll.append(y2)
        else:
            ll.append(x2)
            ll.append(y2)
            ll.append(x1)
            ll.append(y1)
    else:
        if abs(x3) + abs(y3) <= abs(x4) + abs(y4):
            ll.append(x3)
            ll.append(y3)
            ll.append(x4)
            ll.append(y4)
        else:
            ll.append(x4)
            ll.append(y4)
            ll.append(x3)
            ll.append(y3)

    final1 = '(' + str(ll[0]) + ', ' + str(ll[1]) + ')'
    final2 = '(' + str(ll[2]) + ', ' + str(ll[3]) + ')'
    final = final1 + final2
    return final


print(longer_line(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())))






