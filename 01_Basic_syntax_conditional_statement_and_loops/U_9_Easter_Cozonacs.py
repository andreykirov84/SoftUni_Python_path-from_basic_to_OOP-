budget = float(input())
flour = float(input())
eggs = 0.75 * flour
milk = ((0.25 * flour) + flour) / 4

cozonac_price = flour + eggs + milk

eggsCount = 0
cozonacs_count = 0

while budget >= cozonac_price:
    budget -= cozonac_price
    eggsCount += 3
    cozonacs_count += 1

    if cozonacs_count % 3 == 0:
        eggsCount -= cozonacs_count - 2

print(f"You made {cozonacs_count} cozonacs! Now you have {eggsCount} eggs and {budget:.2f}BGN left.")
