import re
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
text = input()
matches = re.finditer(pattern, text)

for item in matches:
    print(item.group(0), end=' ')
