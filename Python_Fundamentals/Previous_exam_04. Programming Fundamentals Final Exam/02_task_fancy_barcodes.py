import re

number = int(input())
for _ in range(number):
    # pattern = r'^@#+(?=[A-Z])([A-Za-z0-9]{6,})(?<=[A-Z])@#+$'
    pattern = r'^@#+([A-Z])([A-Za-z0-9]{4,})([A-Z])@#+$'
    text = input()
    matches = re.search(pattern, text)  # return None if no match exists
    if matches is not None:
        number_pattern = r'\d'
        number_matches = re.findall(number_pattern, matches[0])
        if len(number_matches) > 0:
            product_group_str = ''
            for char in number_matches:
                product_group_str += char

        else:
            product_group_str = '00'
        print(f'Product group: {product_group_str}')
    else:
        print('Invalid barcode')
