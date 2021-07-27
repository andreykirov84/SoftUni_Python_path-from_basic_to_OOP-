days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
real_plunder = 0

for day in range(1, days + 1):
    if day % 3 == 0 and day % 5 == 0:
        real_plunder += 1.5 * daily_plunder
        real_plunder -= 0.3 * real_plunder
    elif day % 3 == 0:
        real_plunder += 1.5 * daily_plunder
    elif day % 5 == 0:
        real_plunder += daily_plunder
        real_plunder -= 0.3 * real_plunder
    else:
        real_plunder += daily_plunder

if real_plunder >= expected_plunder:
    print(f"Ahoy! {real_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {real_plunder / expected_plunder * 100:.2f}% of the plunder.")
