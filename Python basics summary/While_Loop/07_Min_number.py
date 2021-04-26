min_number = None

while True:
    number = input()
    if number == 'Stop':
        break
    number = int(number)
    if min_number is None:
        min_number = number
    elif number < min_number:
        min_number = number

print(min_number)
