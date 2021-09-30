elements = input().split(' ')
storage = {}
for i in range(0, len(elements), 2):
    storage[elements[i]] = int(elements[i + 1])


search_elements = input().split(' ')
for product in search_elements:
    if product in storage.keys():
        print(f"We have {storage[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")



