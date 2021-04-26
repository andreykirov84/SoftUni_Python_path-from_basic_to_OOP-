import math

price_gpu = int(input())
price_connector = int(input())
price_power = float(input())
gpu_profit = float(input())

total_cost = price_gpu * 13 + price_connector * 13 + 1000
profit_per_day = (gpu_profit - price_power) * 13
days = math.ceil(total_cost / profit_per_day)

print(f'{total_cost}')
print(f'{days}')
