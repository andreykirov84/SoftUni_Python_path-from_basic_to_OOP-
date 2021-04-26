skumria_price = float(input())
caca_price = float(input())
palamud_price = skumria_price * 1.60
safrid_price = caca_price * 1.80
midi_price = 7.50
palamud_quantity = float(input())
safrid_quantity = float(input())
midi_quantity = int(input())
total_price = palamud_quantity * palamud_price + safrid_quantity * safrid_price + midi_quantity * midi_price
print(f'{total_price:.2f}')

