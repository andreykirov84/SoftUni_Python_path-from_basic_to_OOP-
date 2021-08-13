import re

destinations = []
destination_char_counter = 0
text = input()
pattern = r'(=|\/)(?P<destination>[A-Z][A-Za-z]{2,})(\1)'


matches = re.finditer(pattern, text)
for locations in matches:
    destination_name = locations.group('destination')
    destinations.append(destination_name)
    destination_char_counter += len(destination_name)

print(f'Destinations:', end=' ')
print(*destinations, sep=', ')
print(f'Travel Points: {destination_char_counter}')


