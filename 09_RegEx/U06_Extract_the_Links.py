import re

pattern = r'(?P<mail>w{3}\.[A-Za-z0-9]+(-[A-Za-z0-9]+)*(\.[a-z]+)+)'
while True:
    text = input()
    if len(text) == 0:
        break
    else:
        matches = re.finditer(pattern, text)
        for site in matches:
            print(site.group('mail'))

