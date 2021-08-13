import re

pattern = r'\d+'
final_text = ''

while True:
    text = input()
    if len(text) == 0:
        break
    final_text += ' ' + text

matches = re.findall(pattern, final_text)

print(*matches, sep=' ')
