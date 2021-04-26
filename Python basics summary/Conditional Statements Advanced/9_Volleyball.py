from math import floor

year = input()
p = int(input())  # holidays
h = int(input())  # weekends home

free_weekends = 48 - h
weekends_sofia = free_weekends * 0.75
games_home = h
games_sofia = p * (2 / 3)
games_sum = weekends_sofia + games_sofia + games_home

if year == "leap":
    games_sum *= 1.15

print(floor(games_sum))
