import re
pattern = r'(^|(?<=\s))([+-]?(\d+(\.\d+)?))+\s($|(?<=\s))'
text = input()
matches = re.findall(pattern, text)

for item in matches:
    print(item[1], end=' ')



