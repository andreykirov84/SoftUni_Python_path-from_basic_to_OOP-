number = float(input())
number_input = input()
number_output = input()
millimeters = 1000
centimeters = 100

if number_input == 'mm':
    number = number / millimeters
elif number_input == 'cm':
    number = number / centimeters

if number_output == 'mm':
    number = number * millimeters
elif number_output == 'cm':
    number = number * centimeters

print(f'{number:.3f}')
