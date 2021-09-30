ll = input().split(' ')
ll = [int(x) for x in ll]
target = 0
command = input()

while command != 'End':
    command = int(command)
    if command < len(ll) and ll[command] != -1:
        target_value = ll[command]
        for i in range(len(ll)):
            if ll[i] != -1:
                old_value = ll[i]
                if ll[i] > target_value:
                    ll[i] = old_value - target_value
                elif ll[i] <= target_value:
                    ll[i] = old_value + target_value
        ll[command] = -1
        target += 1
        command = input()
    else:
        command = input()

print(f"Shot targets: {target} -> ", end='')
print(*ll)





