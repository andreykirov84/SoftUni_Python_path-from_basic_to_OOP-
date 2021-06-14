import re

string = input().upper()
result = []
unique_chars = []
matches = re.finditer(r"(\D+)(\d+)", string)
for match in matches:
    num = int(match.group(2))
    text = match.group(1)
    if num == 0:
        continue
    for i in range(num):
        result.append(text)
    for char in text:
        unique_chars.append(char)
print(f"Unique symbols used: {len(set(unique_chars))}\n{''.join(result)}")
