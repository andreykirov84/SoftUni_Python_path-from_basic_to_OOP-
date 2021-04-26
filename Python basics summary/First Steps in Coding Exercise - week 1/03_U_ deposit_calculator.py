def deposit_calc(number, period, interest_rate):
    result = number + period * ((number * interest_rate * 0.01) / 12)
    return result


suma = deposit_calc(float(input()), int(input()), float(input()))
print(f'{suma:.2f}')
