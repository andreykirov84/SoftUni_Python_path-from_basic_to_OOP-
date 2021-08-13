import re


def sorted_by_value(dd):
    return dict(sorted(dd.items(), key=lambda x:(x[1], x[0]), reverse=True))


pattern = r'((\*{2}|:{2})[A-Z][a-z]{2,}(\2))'
text = input()
matches = re.findall(pattern, text)
result_match = []
ascii_result = {}
for match in matches:
    result_match.append(match[0])

for element in result_match:
    ascii_text = element[2:-2]
    ascii_value = 0
    for char in ascii_text:
        ascii_value += ord(char)
    ascii_result.update({element: ascii_value})

number_pattern = r'\d'

number_matches = re.findall(number_pattern, text)
cool_threshold = 1
for number in number_matches:
    cool_threshold *= int(number)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(ascii_result)} emojis found in the text. The cool ones are:')
for emoji in ascii_result:
    if ascii_result[emoji] > cool_threshold:
        print(emoji)
