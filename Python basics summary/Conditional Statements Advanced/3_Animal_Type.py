mammal = ['dog']

reptile = ['crocodile', 'tortoise', 'snake']

animal = input()

if animal in mammal:
    print("mammal")
elif animal in reptile:
    print("reptile")
else:
    print("unknown")
