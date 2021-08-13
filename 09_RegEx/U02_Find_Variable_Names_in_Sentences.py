import re

pattern = r'\b_{1}(?P<variable>[A-Za-z0-9]+)\b'

text = input()
variable_ll = []
matches = re.finditer(pattern, text)
for match in matches:
    word = match.group('variable')
    variable_ll.append(word)

print(*variable_ll, sep=',')
