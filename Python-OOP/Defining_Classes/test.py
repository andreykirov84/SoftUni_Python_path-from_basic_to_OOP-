def draw_rhombus(number):
    for i in range(number):
        indent = ' ' * (number - i - 1)
        stars = '* ' * (i + 1)
        print(f'{indent}{stars}')
    for i in range(number, 0, -1):
        indent = ' ' * (number - i + 1)
        stars = '* ' * (i - 1)
        print(f'{indent}{stars}')


draw_rhombus(10)