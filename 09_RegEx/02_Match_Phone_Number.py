import re

text = input()
regex = r'\+359-2-[\d]{3}-[\d]{4}\b|\+359 2 \d{3} [\d]{4}\b'
matches = re.findall(regex, text)
print(', '.join(matches))


