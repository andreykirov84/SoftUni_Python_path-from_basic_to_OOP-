def find_palindrome(ll):
    result = []
    for i in range(len(ll)):
        if ll[i] == ll[i][::-1]:
            result.append(True)
        else:
            result.append(False)
    return result


# ll = input().split(', ')
x = find_palindrome(input().split(', '))
for i in x:
    print(i)
