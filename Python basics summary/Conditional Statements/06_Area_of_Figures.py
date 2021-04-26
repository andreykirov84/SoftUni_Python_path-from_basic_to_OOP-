from math import pi

figure = input()
if figure == 'square':
    side = float(input())
    print(f'{side * side}')

elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    print(f'{side_a * side_b}')

elif figure == 'circle':
    radius = float(input())
    print(f'{pi * radius * radius}')

elif figure == 'triangle':
    side = float(input())
    height = float(input())
    print(f'{side * height / 2}')
