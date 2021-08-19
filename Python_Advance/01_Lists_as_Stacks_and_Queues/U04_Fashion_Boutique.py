ll = input().split(' ')
ll = [int(x) for x in ll]
CAPACITY = int(input())
rack_capacity = CAPACITY
racks = 0

while len(ll) > 0:
    piece = ll.pop()
    if piece <= rack_capacity:
        rack_capacity -= piece
    else:
        racks += 1
        ll.append(piece)
        rack_capacity = CAPACITY

racks += 1
print(racks)
