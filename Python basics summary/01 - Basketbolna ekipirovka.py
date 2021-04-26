annual_fee = int(input())
kecove_price = annual_fee - 0.4 * annual_fee
ekip_price = kecove_price - 0.2 * kecove_price
topka_price = 0.25 * ekip_price
aksesoari_price = 0.2 * topka_price
total_fee = annual_fee + kecove_price + ekip_price + topka_price + aksesoari_price
print(f'{total_fee:.2f}')