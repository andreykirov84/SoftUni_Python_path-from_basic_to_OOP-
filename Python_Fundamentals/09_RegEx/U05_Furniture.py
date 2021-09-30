import re

total_money = 0

pattern = r'>>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'
print('Bought furniture:')

while True:
    text = input()
    if text == 'Purchase':
        break
    else:
        matches = re.finditer(pattern, text)
        for purchase in matches:
            furniture_name = purchase.group('furniture')
            price = float(purchase.group('price'))
            quantity = int(purchase.group('quantity'))
            total_money += price * quantity
            print(furniture_name)

print(f'Total money spend: {total_money:.2f}')



# ">>{furniture_name}<<{price}!{quantity}".