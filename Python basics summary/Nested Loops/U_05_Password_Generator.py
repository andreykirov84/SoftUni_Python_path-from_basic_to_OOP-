number_one = int(input())
number_two = int(input())
ll = []
password_ll = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(1, number_one + 1):
    for j in range(1, number_one + 1):
        for k in range(number_two):
            for z in range(number_two):
                for m in range(1, number_one + 1):
                    ll.append(str(i))
                    ll.append(str(j))
                    ll.append(alphabet[k])
                    ll.append(alphabet[z])
                    if m > i and m > j:
                        ll.append(str(m))
                    if len(ll) == 5:
                        password_string = ''.join(ll)
                        password_ll.append(password_string)
                    password_string = ''
                    ll = []
print(' '.join(password_ll))
