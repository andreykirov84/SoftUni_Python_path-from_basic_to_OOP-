import re

pattern = r'^(%|\$)(?P<tag_name>[A-Z][a-z]{2,})(\1):\s\[(?P<number_one>\d+)\]\|\[(?P<number_two>\d+)\]\|\[(?P<number_three>\d+)\]\|$'

number = int(input())
for _ in range(number):
    is_valid_command = False
    text = input()
    matches = re.finditer(pattern, text)
    # print(matches)
    for match in matches:
        is_valid_command = True
        tag_name = match.group('tag_name')
        number_one = chr(int(match.group('number_one')))
        number_two = chr(int(match.group('number_two')))
        number_three = chr(int(match.group('number_three')))
        print(f'{tag_name}: {number_one}{number_two}{number_three}')
    if not is_valid_command:
        print('Valid message not found!')



