# сума за ракети = брой на ракети(вход) * цена за 1 ракета(вход)
# сума за маратонки = брой на маратонките (вход) * цена за 1 чифт маратонки( 1 /6 от цена за 1 ракета)
# сума за екипировката = 20 % от (сума за ракети + сума за маратонките)
# разходи = сума за ракети + сума за маратонки + сума за екипировката
# Джокович -> 1/7 от разходите
# спонсори -> 7/8 от разходите
import math

price_per_racket = float(input())
count_rackets = int(input())
count_trainers = int(input())

sum_rackets = count_rackets * price_per_racket  # сума за ракети
sum_trainers = count_trainers * (price_per_racket / 6)  # сума за маратонки
sum_equipment = 0.20 * (sum_rackets + sum_trainers)  # сума за екипировката

expenses = sum_rackets + sum_trainers + sum_equipment
sum_djokovic = expenses / 8
sum_sponsors = 7 / 8 * expenses

print(f'Price to be paid by Djokovic {math.floor(sum_djokovic)}')
print(f'Price to be paid by sponsors {math.ceil(sum_sponsors)}')