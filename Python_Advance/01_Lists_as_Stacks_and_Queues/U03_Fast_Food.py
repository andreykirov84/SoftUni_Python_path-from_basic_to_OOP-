from collections import deque

food_quantity = int(input())
ll = input().split(' ')
ll = [int(x) for x in ll]
ll_deque = deque(ll)

print(max(ll))
while True:
    if len(ll_deque) > 0 and ll_deque[0] <= food_quantity:
        food_quantity -= ll_deque.popleft()
    elif len(ll_deque) == 0:
        print('Orders complete')
        break
    else:
        print('Orders left: ', end='')
        print(*ll_deque)
        break
