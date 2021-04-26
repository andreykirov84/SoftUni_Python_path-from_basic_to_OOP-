name = input()
graduate = True
ll = []
klas = 1
average_mark = 0

while klas < 13:
    mark = float(input())
    if mark < 4:
        graduate = False
        break
    ll.append(mark)
    klas += 1

if not graduate:
    print(f"{name} has been excluded at {klas} grade")
else:
    average_mark = sum(ll) / len(ll)
    print(f"{name} graduated. Average grade: {average_mark:.2f}")
