symbols = {}
symbol = list(input())

for i in range(len(symbol)):
    x = symbol[i]
    if x in symbols.keys():
        symbols[x] += 1
    else:
        symbols[x] = 1
# print(symbols)


for key in sorted(symbols.keys()):
    value = symbols[key]
    print(f'{key}: {value} time/s')
