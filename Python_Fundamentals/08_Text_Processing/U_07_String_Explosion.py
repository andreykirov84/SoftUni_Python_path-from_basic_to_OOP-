ll = input().split('>')
addition = 0
for i in range(1, len(ll)):
    number = int(ll[i][0])
    if len(ll[i]) >= number + addition:
        ll[i] = ll[i][number + addition:]
    else:
        addition += number - len(ll[i])
        ll[i] = ''

final_text = '>'.join([str(item) for item in ll])
print(final_text)
