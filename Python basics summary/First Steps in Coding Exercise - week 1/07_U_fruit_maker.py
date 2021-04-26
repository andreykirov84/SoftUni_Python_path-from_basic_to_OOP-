iagodi_price = float(input())
malini_price = iagodi_price * 0.5
portokali_price = malini_price - malini_price * 0.4
banani_price = malini_price - malini_price * 0.8
banani_quantity = float(input())
portokali_quantity = float(input())
malini_quantity = float(input())
iagodi_quantity = float(input())
total_sum = iagodi_quantity * iagodi_price + banani_quantity * banani_price + portokali_quantity * portokali_price + malini_quantity * malini_price
print(total_sum)