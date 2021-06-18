import re

text = input()
regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
matches = re.findall(regex, text)
print(' '.join(matches))

