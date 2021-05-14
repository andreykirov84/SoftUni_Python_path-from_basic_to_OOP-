def tri_seq(number):
    ll = [1, 1, 2]
    result = []
    if number <= 3:
        result = ll[0: number]
    else:
        result = ll
        for i in range(3, number):
            next_number = sum(result[i - 3:i])
            result.append(next_number)

    return result


res_ll = tri_seq(int(input()))
for i in range(len(res_ll)):
    print(res_ll[i], end=' ')
