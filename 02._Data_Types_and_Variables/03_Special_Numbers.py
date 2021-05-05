def sum_of_digits_in_number(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit
        number = number // 10

    return total_sum


number = int(input())
state = False
for i in range(1, number + 1):
    total = sum_of_digits_in_number(i)
    if total == 5 or total == 7 or total == 11:
        state = True
    print(f'{i} -> {state}')
    state = False
