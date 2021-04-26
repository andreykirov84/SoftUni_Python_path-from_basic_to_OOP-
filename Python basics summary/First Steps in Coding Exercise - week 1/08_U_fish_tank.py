length = int(input())
width = int(input())
height = int(input())
occupied_percent = float(input()) * 0.01
full_volume = length * width * height * 0.001
water_needed = full_volume - full_volume * occupied_percent
print(water_needed)
