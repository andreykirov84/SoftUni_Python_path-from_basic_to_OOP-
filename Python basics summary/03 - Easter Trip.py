destination_country = input()
dates = input()
nights_number = int(input())
price_per_night = None
i = None
# if destination_country == "France":   #solution using only if statement
#     if dates == "21-23":
#         price_per_night = 30
#     elif dates == "24-27":
#         price_per_night = 35
#     elif dates == "28-31":
#         price_per_night = 40
#
# if destination_country == "Italy":
#     if dates == "21-23":
#         price_per_night = 28
#     elif dates == "24-27":
#         price_per_night = 32
#     elif dates == "28-31":
#         price_per_night = 39
#
# if destination_country == "Germany":
#     if dates == "21-23":
#         price_per_night = 32
#     elif dates == "24-27":
#         price_per_night = 37
#     elif dates == "28-31":
#         price_per_night = 43

price_dictionary = {
    "France": [30, 35, 40],
    "Italy": [28, 32, 39],
    "Germany": [32, 37, 43]
}
if dates == "21-23":
    i = 0
elif dates == "24-27":
    i = 1
elif dates == "28-31":
    i = 2

total_price = float(nights_number * price_dictionary.get(destination_country)[i])
print(f'Easter trip to {destination_country} : {total_price:.2f} leva.')
