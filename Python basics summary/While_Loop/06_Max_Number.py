max_number = None

while True:
    number = input()
    if number == 'Stop':
        break
    number = int(number)
    if max_number is None:
        max_number = number
    elif number > max_number:
        max_number = number

print(max_number)
