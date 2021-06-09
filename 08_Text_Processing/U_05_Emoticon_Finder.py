def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


text = input()
coordinates = find(text, ':')
for number in coordinates:
    print(text[number: number+2])
