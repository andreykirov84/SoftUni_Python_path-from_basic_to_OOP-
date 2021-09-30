import re

text = input()
real_match = []
counter = 0
word_separator = ' <=> '
pattern = r'((@|#)(?P<word1>[A-Za-z]{3,})(\2)(\2)(?P<word2>[A-Za-z]{3,})(\2))'

matches = re.finditer(pattern, text)
for match in matches:
    word_one = match.group('word1')
    word_two = match.group('word2')
    counter += 1
    if word_one == word_two[::-1]:
        real_match.append(word_one + word_separator + word_two)

if counter == 0:
    print("No word pairs found!")
else:
    print(f"{counter} word pairs found!")

if len(real_match) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(*real_match, sep=', ')



