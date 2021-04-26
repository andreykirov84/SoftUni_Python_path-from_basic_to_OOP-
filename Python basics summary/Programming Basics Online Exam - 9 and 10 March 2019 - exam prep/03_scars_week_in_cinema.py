# приходи = бр. билетите(вход) * цена за 1 билет(определя се от филма и залата)
movie_name = input()
type_hall = input()
count_tickets = int(input())

price_per_ticket = 0
# ("A Star Is Born", "Bohemian Rhapsody","Green Book" или "The Favourite"
if movie_name == "A Star Is Born":
    if type_hall == "normal":
        price_per_ticket = 7.50
    elif type_hall == "luxury":
        price_per_ticket = 10.50
    elif type_hall == "ultra luxury":
        price_per_ticket = 13.50
elif movie_name == "Bohemian Rhapsody":
    if type_hall == "normal":
        price_per_ticket = 7.35
    elif type_hall == "luxury":
        price_per_ticket = 9.45
    elif type_hall == "ultra luxury":
        price_per_ticket = 12.75
elif movie_name == "Green Book":
    if type_hall == "normal":
        price_per_ticket = 8.15
    elif type_hall == "luxury":
        price_per_ticket = 10.25
    elif type_hall == "ultra luxury":
        price_per_ticket = 13.25
elif movie_name == "The Favourite":
    if type_hall == "normal":
        price_per_ticket = 8.75
    elif type_hall == "luxury":
        price_per_ticket = 11.55
    elif type_hall == "ultra luxury":
        price_per_ticket = 13.95

profit = count_tickets * price_per_ticket
print(f'{movie_name} -> {profit:.2f} lv.')