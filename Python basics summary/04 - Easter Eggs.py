eggs_number = int(input())
n = 0
eggs = {
    "red": 0,
    "orange": 0,
    "blue": 0,
    "green": 0
}

while n < eggs_number:
    eggs_colour = input()
    if eggs_colour in eggs:
        eggs[eggs_colour] += 1
    n += 1

numbers = list(eggs.values())
numbers.sort()
max_colours = []
for key, value in eggs.items():
    if numbers[-1] == value:
        max_colours.append(key)

# print(numbers)
print(f'Red eggs: {int(eggs["red"])}')
print(f'Orange eggs: {int(eggs["orange"])}')
print(f'Blue eggs: {int(eggs["blue"])}')
print(f'Green eggs: {int(eggs["green"])}')
print(f'Max eggs: {max(numbers)} -> ' + ', '.join(max_colours)) # конкатениране на 2 стринга
