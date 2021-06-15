import re
names = input().split(', ')
regex = r'[A-Z]'
matches = re.findall(regex, names)
