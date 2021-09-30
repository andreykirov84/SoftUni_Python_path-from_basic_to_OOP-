text = list(input())
remove_ll = []
for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        remove_ll.append(i)

while len(remove_ll) != 0:
    text.pop(remove_ll[-1])
    remove_ll.pop(-1)

final_text = ''.join([str(item) for item in text])
print(final_text)


