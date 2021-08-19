stado = input()
ll = stado.split(', ')
wolf_index = 0
sheep_index = 0


if ll[-1] != 'wolf':
    for i in range(len(ll)):
        if ll[i] == 'wolf':
            wolf_index = i
            sheep_index = len(ll) - wolf_index - 1
            break
    print(f'Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!')

else:
    print("Please go away and stop eating my sheep")





