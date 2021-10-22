def numbers_searching(*args):
    max_number = max(args)
    min_number = min(args)
    numbers = {}
    missing_values = []
    duplicate_values = []
    output_ll = []

    for key in range(min_number, max_number + 1):
        numbers[key] = 0

    for number in args:
        numbers[number] += 1

    for key in numbers:
        if numbers[key] == 0:
            missing_values.append(key)
        elif numbers[key] > 1:
            duplicate_values.append(key)

    for mis_val in missing_values:
        output_ll.append(mis_val)
    output_ll.append(duplicate_values)

    return output_ll


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
