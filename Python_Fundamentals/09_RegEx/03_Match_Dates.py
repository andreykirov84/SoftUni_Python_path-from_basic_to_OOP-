import re
pattern = r'\b(?P<day>\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b'
text = input()
matches = re.findall(pattern, text)


for (day, _, month, year) in matches:
    print(f'Day: {day}, Month: {month}, Year: {year}')
