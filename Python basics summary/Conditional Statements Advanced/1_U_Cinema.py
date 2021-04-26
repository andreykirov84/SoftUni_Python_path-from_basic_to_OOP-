price = 0
projection_type = input()
raws = int(input())
cols = int(input())
if projection_type == 'Premiere':
    price = 12
elif projection_type == 'Normal':
    price = 7.50
elif projection_type == 'Discount':
    price = 5
print(f'{raws * cols * price:.2f} leva')
