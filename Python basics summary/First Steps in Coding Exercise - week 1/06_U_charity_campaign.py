torta_price = 45
gofreta_price = 5.80
palachinka_price = 3.20

days = int(input())
confectioners = int(input())
torta_numbers = int(input())
gofreta_numbers = int(input())
palachinka_numbers = int(input())
torta_production = torta_price * torta_numbers
palachinka_production = palachinka_numbers * palachinka_price
gofreta_production = gofreta_numbers * gofreta_price
confectioner_production = torta_production + palachinka_production + gofreta_production
total_income = days * confectioners * confectioner_production
final_income = total_income - (1 / 8 * total_income)
print(final_income)
