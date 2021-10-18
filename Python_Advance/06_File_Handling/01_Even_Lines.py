symbols_for_replace = ("-", ",", ".", "!", "?")
replace_symbol = "@"

with open('text.txt', 'r') as file:
    is_even = True

    while True:
        line = file.readline().strip()
        if not line:
            break
        if is_even:
            for symbol in symbols_for_replace:
                line = line.replace(symbol, replace_symbol)
            line = ' '.join(line.split()[::-1])
            print(line)
        is_even = not is_even











