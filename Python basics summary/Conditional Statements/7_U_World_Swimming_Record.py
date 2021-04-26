from math import floor

record_time = float(input())
distance = float(input())
time_per_meter = float(input())
water_resistance_slowdown = floor(distance / 15) * 12.5
player_time = distance * time_per_meter + water_resistance_slowdown
difference_time = player_time - record_time
if player_time < record_time:
    print(f'Yes, he succeeded! The new world record is {player_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference_time:.2f} seconds slower.')
