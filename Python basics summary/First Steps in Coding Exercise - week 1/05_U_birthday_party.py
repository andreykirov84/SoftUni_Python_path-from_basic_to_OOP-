def birthday_party(rent):
    torta = 0.2 * rent
    drinks = torta - (torta * 0.45)
    animator = rent * (1 / 3)
    total = torta + drinks + animator + rent
    return total


print(birthday_party(float(input())))
